# -*- coding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from os import path

def getBNF(file_name):
    here = path.abspath(path.dirname(__file__))
    grammer_productions_list = []
    each_grammer_strip_list = []
    
    with open(path.join(here,'..', 'grammer',file_name)) as f:
        begin_production_left = f.readline().strip().split('->')[0]
        if not begin_production_left.endswith('\''):
            grammer_productions_list.append(begin_production_left+'\''+'->'+begin_production_left)
        f.seek(0)
        for eachLine in f:
            same_leftPart_strip_list = eachLine.strip().split('|')
            grammer_productions_list.append(same_leftPart_strip_list[0])
            left_part = same_leftPart_strip_list[0].split('->')[0] + '->'
            for each_grammer in same_leftPart_strip_list[1:]:
                grammer_productions_list.append(left_part + each_grammer)

    return grammer_productions_list

if __name__ == '__main__':
    output = getBNF('grammer.txt')
    print output
