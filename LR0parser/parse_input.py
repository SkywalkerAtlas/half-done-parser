# -*- coding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

def parse_input():
    input_parse = raw_input('input parse to analyse:').strip()
    return input_parse + "#"

if __name__ == '__main__':
    
    inputed_parse = parse_input()
    print inputed_parse
