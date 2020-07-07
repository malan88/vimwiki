#!/bin/python

import os

files = os.listdir()
files.pop(files.index('index.md'))
files.sort()

with open('index.md', 'wt') as index:
    index.write('# notes\n\n')
    for file in files:
        index.write('- [' +
                    file.split('.')[0] +
                    '](' +
                    file +
                    ')\n')
