# -*- coding: utf-8 -*-
# Copyright: Ian Worthington <worthy.vii@gmail.com>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# 
# Port to Anki 2.1 by Mirco Kraenz <mirco@kraenz.eu>

import os
import re

# RTK file path
this_dir, this_filename = os.path.split(__file__)
allRTK = os.path.join(this_dir, "RTK.tsv") 

def readRTK():
    kanjiIndex = dict()
    with open(allRTK, 'r', encoding="utf-8") as f:
        content = f.read().splitlines()
    f.close() 
    for line in content:
        fieldhash = dict(zip(('kanji', 'heisigold', 'heisig2010', 'keyword'),
                            line.split('\t')))
        kanjiIndex[fieldhash['kanji']] = fieldhash
    return kanjiIndex

# testing, note that the usual windows console does not support unicode, so run in powershell to see the actual result
if __name__ == "__main__":
    kanjiIndex = readRTK()
    # print(kanjiIndex)
    if not '一' in kanjiIndex:
        raise Exception('Unit test failed: Expected character for ichi to be contained in the kanjiIndex.')
    if not kanjiIndex['餅'] == {'kanji': '餅', 'heisigold': '1478A', 'heisig2010': '1590', 'keyword': 'mochi'}:
        raise Exception('Unit test failed: Expected value for character mochi does not match ' + str(kanjiIndex['餅']))
    else:
        print('Tests succeeded')
    