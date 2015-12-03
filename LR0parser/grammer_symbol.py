# -*- coding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from BNF import getBNF

def get_grammer_symbol(grammer_productions_list):
	grammer_symbol = []
	for each_production in grammer_productions_list:
		symbols = each_production.split('->',)
		if symbols[0] not in grammer_symbol:
			grammer_symbol.append(symbols[0])
		for symbol in symbols[1]:
			if symbol not in grammer_symbol:
				grammer_symbol.append(symbol)
	return grammer_symbol


if __name__ == '__main__':
    grammer_productions_list = getBNF('grammer.txt')
    grammer_symbol = get_grammer_symbol(grammer_productions_list)
    print grammer_symbol