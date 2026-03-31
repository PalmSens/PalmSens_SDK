from __future__ import annotations

import json

name = 'python'
version = '1.6.0'
tag = f'{name}-{version}'

with open(f'{tag}.json') as f:
    data = json.load(f)

TEMPLATE = """
## {name}

{tagName} - {url}
{publishedAt}
pip: https://pypi.org/project/pypalmsens-{version}'

{body}
"""

with open(f'{tag}.md', 'w') as f:
    string = TEMPLATE.format(version=version, **data)
    print(string)
    f.write(string)

# title
# released
# body
# pip link


breakpoint()
