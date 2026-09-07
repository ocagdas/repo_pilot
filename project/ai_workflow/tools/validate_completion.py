#!/usr/bin/env python3
"""Validate a derived report against the canonical Spec Kit task ledger."""
import argparse
import json
import re
from pathlib import Path


def validate_shape(value, schema, location='$'):
    # Only the keywords used by our bundled schema are supported.
    types = {'object':dict, 'array':list, 'string':str}
    expected = schema.get('type')
    if expected and not isinstance(value, types[expected]):
        raise ValueError(location + ': expected ' + expected)
    if 'const' in schema and value != schema['const']:
        raise ValueError(location + ': invalid constant')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(location + ': invalid value')
    if isinstance(value, str) and len(value) < schema.get('minLength', 0):
        raise ValueError(location + ': empty value')
    if isinstance(value, dict):
        if set(schema.get('required', [])) - value.keys():
            raise ValueError(location + ': missing fields')
        props = schema.get('properties', {})
        if schema.get('additionalProperties') is False and value.keys() - props.keys():
            raise ValueError(location + ': unknown fields')
        for key in value.keys() & props.keys():
            validate_shape(value[key], props[key], location + '.' + key)
    if isinstance(value, list) and 'items' in schema:
        for i, item in enumerate(value):
            validate_shape(item, schema['items'], location + '[' + str(i) + ']')

def validate(feature):
    schema = json.loads((Path(__file__).resolve().parents[1] / 'completion_report.schema.json').read_text(encoding='utf-8'))
    report = json.loads((feature / 'completion.json').read_text(encoding='utf-8'))
    validate_shape(report, schema)
    tasks = re.findall(r'^\s*[-*]\s+\[([ xX])\]\s+(T\d+)\b', (feature / 'tasks.md').read_text(encoding='utf-8'), re.M)
    if not tasks:
        raise ValueError('No canonical T numbered task checkboxes found')
    ids = [task_id for _, task_id in tasks]
    reports = [item['id'] for item in report['tasks']]
    if len(ids) != len(set(ids)) or len(reports) != len(set(reports)):
        raise ValueError('Duplicate task IDs')
    if set(ids) != set(reports):
        raise ValueError('Report must cover exactly the canonical task IDs')
    criteria = set(re.findall(r'\bAC[0-9]+\b', (feature / 'spec.md').read_text(encoding='utf-8')))
    reported_criteria = [item['id'] for item in report['acceptance_criteria']]
    if not criteria or set(reported_criteria) != criteria or len(reported_criteria) != len(set(reported_criteria)):
        raise ValueError('Report must cover exactly the AC numbered acceptance criteria in spec.md')
    checked = {task_id: bool(mark.strip()) for mark, task_id in tasks}
    for item in report['tasks']:
        done = item['status'] == 'completed'
        if done != checked[item['id']]:
            raise ValueError('Task checkbox and report disagree: ' + item['id'])
    for item in report['tasks'] + report['acceptance_criteria']:
        if item['status'] == 'completed' and not item['evidence']:
            raise ValueError('Completed item lacks evidence: ' + item['id'])
        if item['status'] != 'completed' and not item['remaining_work'].strip():
            raise ValueError('Unfinished item lacks remaining work: ' + item['id'])
    print('Report structure and task coverage valid; evidence truth is not certified')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('feature', type=Path)
    args = parser.parse_args()
    try:
        validate(args.feature.resolve())
    except (OSError, ValueError, ImportError) as error:
        parser.exit(1, str(error) + '\n')
