from __future__ import annotations

import subprocess as sp
import sys
from datetime import datetime
from pathlib import Path
from textwrap import dedent


def get_changes_since_tag(tag: str):
    cmd = f'git log {tag}..HEAD --reverse --oneline'
    p = sp.run(cmd, capture_output=True)
    lines = p.stdout.decode().splitlines()
    lines = (line.split(maxsplit=1)[1] for line in lines)

    out = []

    for line in lines:
        if '(#' not in line and not line.endswith(')'):
            continue

        if line.startswith('('):
            index = line.index(')')
            line = line[index + 2 :]

        index = line.index('(#')
        pr = line[index + 2 : -1]
        line = line.replace(
            f'#{pr}', f'[#{pr}](https://github.com/PalmSens/PalmSens_SDK/pull/{pr})'
        )
        out.append(f'- {line}')

    return '\n'.join(out)


if __name__ == '__main__':
    component = 'python'

    args = sys.argv[1:]

    assert len(args) == 2

    previous_version, new_version = args
    previous_tag = f'{component}-{previous_version}'
    new_tag = f'{component}-{new_version}'

    time = datetime.today()

    changelog = get_changes_since_tag(previous_tag)

    TEMPLATE_CHANGELOG = dedent("""\
    # PyPalmSens {new_version}

    > :fontawesome-brands-github: <a href="https://github.com/PalmSens/PalmSens_SDK/releases/tag/{new_tag}">{new_tag}</a>
    - :fontawesome-brands-python: <a href="https://pypi.org/project/pypalmsens/{new_version}">pypalmsens-{new_version}</a>
    - :fontawesome-solid-calendar: {time}

    ## What's changed

    {changelog}
    """)

    TEMPLATE_GH_RELEASES = dedent(f"""\
    PyPalmSens {new_tag} is now available on PyPi.

    To upgrade: `pip install pypalmsens -U`.

    For the full changelog, see: https://dev.palmsens.com/python/latest/_attachments/releases/#pypalmsens-{new_tag.replace('.', '')}

    ## What's changed

    {changelog}
    """)

    index_path = Path('index.md')

    lines = index_path.read_text().splitlines()

    index = lines.index('// latest')

    if new_version in lines[index + 1]:
        print('Tag already exists, skipping')
    else:
        new_string = TEMPLATE_CHANGELOG.format(
            new_version=new_version, new_tag=new_tag, time=time.date(), changelog=changelog
        )
        print(new_string)

        lines.insert(index + 1, new_string)
        index_path.write_text('\n'.join(lines) + '\n', encoding='UTF-8')

        print(f'Tag added to {index_path.name}')
