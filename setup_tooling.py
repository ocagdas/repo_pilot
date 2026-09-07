#!/usr/bin/env python3
"""Prepare machine tooling separately from project installation."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def commands(mode, env_dir, conda_name):
    requirements = str(ROOT / 'requirements.txt')
    if mode == 'native':
        pip = [sys.executable, '-m', 'pip', 'install']
        if sys.prefix == sys.base_prefix and not os.environ.get('CONDA_PREFIX'):
            pip.append('--user')
        return [pip + ['-r', requirements]]
    if mode == 'venv':
        python = env_dir / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        if env_dir.exists() and not (env_dir / 'pyvenv.cfg').is_file():
            raise ValueError('Existing environment path is not a venv: ' + str(env_dir))
        return [[sys.executable, '-m', 'venv', str(env_dir)],
                [str(python), '-m', 'pip', 'install', '-r', requirements]]
    if not conda_name or conda_name.startswith('-') or any(c in conda_name for c in '/\\ '):
        raise ValueError('Use a simple Conda environment name')
    conda = os.environ.get('CONDA_EXE') or shutil.which('conda') or 'conda'
    return [[conda, 'env', 'create', '--name', conda_name, '--file', str(ROOT / 'environment.yml')]]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['native','venv','conda'], default='venv')
    parser.add_argument('--env-dir', type=Path, default=ROOT / '.venv')
    parser.add_argument('--conda-name', default='spec_kit_engineering')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if sys.version_info < (3,11): parser.error('Python 3.11 or newer is required')
    try:
        plan = commands(args.mode, args.env_dir.resolve(), args.conda_name)
        print(json.dumps({'mode':args.mode,'commands':plan,'apply':args.apply}, indent=2))
        if not args.apply: return
        if args.mode != 'conda' and not shutil.which('git'):
            raise ValueError('Install Git and put it on PATH before installing the official source requirement')
        for command in plan:
            subprocess.run(command, cwd=ROOT, check=True)
        print('Tooling installed. Follow INSTALLATION.md to run install.py for a target repository.')
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + '\n')

if __name__ == '__main__': main()
