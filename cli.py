"""Installed Repo Pilot command; static wheels and editable checkouts share this entry point."""
import importlib.metadata
import json
import os
from pathlib import Path
import runpy
import sys
import sysconfig

ROOT = Path(__file__).resolve().parent
COMMANDS = {'install': 'install.py', 'configure': 'configure.py', 'knowledge': 'knowledge.py',
            'bootstrap': 'project/ai_workflow/tools/repo_bootstrap.py'}


def main():
    args = sys.argv[1:]
    if args == ['--version']:
        distribution = importlib.metadata.distribution('repo-pilot')
        origin = json.loads(distribution.read_text('direct_url.json') or '{}')
        print(json.dumps({'version': distribution.version,
                          'install_mode': 'editable' if origin.get('dir_info', {}).get('editable') else 'static',
                          'code_path': str(ROOT)}, indent=2))
        return 0
    if not args or args[0] in ('-h', '--help'):
        print('Usage: repo-pilot {install,configure,knowledge,bootstrap} [arguments]\n'
              '       repo-pilot --version\nUse repo-pilot COMMAND --help for command options.')
        return 0
    if args[0] not in COMMANDS:
        print('Unknown command: ' + args[0], file=sys.stderr)
        return 2
    # Use this installation's companion tools even when invoked by absolute path
    # without activating the environment. Keep existing direct-script entry points.
    os.environ['PATH'] = sysconfig.get_path('scripts') + os.pathsep + os.environ.get('PATH', '')
    sys.path.insert(0, str(ROOT))
    script = ROOT / COMMANDS[args[0]]
    sys.path.insert(0, str(script.parent))
    sys.argv = [str(script), *args[1:]]
    runpy.run_path(str(script), run_name='__main__')
    return 0
