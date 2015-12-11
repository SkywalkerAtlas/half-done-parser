# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from grammer_symbol import get_grammer_symbol
from BNF import getBNF


def find_first_set(X,production_dist,terminals_list,first_set,first):
	for each_pro in production_dist[X]:
		if each_pro[0] in terminals_list:
			first_set.add(each_pro[0])
		elif each_pro[0] != X:
			first_set = find_first_set(each_pro[0],production_dist,terminals_list,first_set,first)
	if first.has_key(X):
		print '??????????'
		pass
	else:
		first[X] = first_set
	return first_set

def get_first(file_name):
	first = {}
	grammer_productions_list = getBNF(file_name)
	production_dist = {}
	for each_production in grammer_productions_list:
		left,right = each_production.split('->')
		if production_dist.has_key(left):
			production_dist[left].append(right)
		else:
			production_dist[left] = [right,]
	grammer_symbol = get_grammer_symbol(grammer_productions_list)
	#print grammer_symbol
	non_terminals_list = []
	terminals_list = []
	
	for each_symbol in grammer_symbol:
		if each_symbol.istitle():
			non_terminals_list.append(each_symbol)
		else:
			terminals_list.append(each_symbol)

	for each_symbol in non_terminals_list:
		if first.has_key(each_symbol):
			continue
		else:
			null_first_set = set()
			first_set = find_first_set(each_symbol,production_dist,terminals_list,null_first_set,first)
			first[each_symbol] = first_set
	
	for each_symbol in terminals_list:
		first[each_symbol] = set([each_symbol])
	return first

if __name__ == '__main__':
	output = get_first('grammer.txt')
	print output
