from __future__ import annotations

from pathlib import Path

import griffe
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader(Path(__file__).parent / 'templates')
environment = Environment(loader=file_loader, autoescape=True)

template = environment.get_template('page.adoc.j2')

mod = griffe.load('pypalmsens', docstring_parser='numpy')

rendered = template.render(functions=mod.functions, classes=mod.classes)

print(rendered)

f = mod.functions['connect']

for member in mod.members:
    pass
