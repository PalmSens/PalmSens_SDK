#!/bin/bash

# https://unix.stackexchange.com/a/49917
shopt -s globstar

pdoc pypalmsens -o docs/modules/python/pages/api/ --template docs/pdoc-template/ --force

for f in ./docs/modules/python/pages/api/**/*.md
do
    [ -f "$f" ] && mv "$f" "${f%md}adoc"
done

npx antora antora-playbook.yml
