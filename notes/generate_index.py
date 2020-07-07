#!/bin/python

import os

notesdir = os.path.expanduser('~/vimwiki/notes')

files = os.listdir(notesdir)
files.pop(files.index('index.md'))
files.sort()

with open(f'{notesdir}/index.md', 'wt') as index:
    index.write('# notes\n\n')
    for file in files:
        index.write('- [' +
                    file.split('.')[0] +
                    '](' +
                    file +
                    ')\n')
