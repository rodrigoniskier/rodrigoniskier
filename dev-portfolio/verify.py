"""Validate portfolio sources and static review surfaces before deployment."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parent
projects=json.loads((root/'projects.json').read_text())
assert len(projects)==4
for project in projects:
    for name in project['screens']:
        path=root/'screens'/name
        assert path.is_file(),name
        html=path.read_text()
        assert '<html' in html and '</html>' in html
        assert not re.search(r'name="csrf[^>]*value="[^\"]+',html)
        assert '<form' not in html
        assert '<script' not in html
for file in ('style.css','script.js','favicon.svg','index.html'):
    assert (root/file).is_file(),file
html=(root/'index.html').read_text()
assert 'mailto:niskier.rodrigo@gmail.com' in html
assert 'Demonstrações online' not in html
print('Four cases, nine static screens, assets and contact verified.')
