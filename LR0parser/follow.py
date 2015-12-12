# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from first import get_first
from grammer_symbol import get_grammer_symbol
from BNF import getBNF

def get_follow_set(X,production_dist,terminals_list,non_terminals_list,follow,first):

	if follow.has_key(X):
		return follow[X]

	follow_set = set()

	#X is start symbol
	if X == non_terminals_list[0]:
		follow_set.add('#')

	for key in production_dist.keys():
		for each_pro in production_dist[key]:
			if each_pro.find(X) != -1:
				if each_pro.endswith(X) and key == X:
					continue
				elif each_pro.endswith(X):
					follow_set = follow_set | (get_follow_set(key,production_dist,terminals_list,non_terminals_list,follow,first))

				else:
					follow_set = follow_set | (first[each_pro[each_pro.index(X)+1]])

	follow[X] = follow_set
	return follow_set

def get_follow(file_name):
	follow = {}
	first = get_first(file_name)
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

	for each_non_symbol in non_terminals_list:
		if follow.has_key(each_non_symbol):
			continue
		else:
			follow_set = get_follow_set(each_non_symbol,production_dist,terminals_list,non_terminals_list,follow,first)
			follow[each_non_symbol] = follow_set

	return follow

if __name__ == '__main__':
	output = get_follow('grammer.txt')
	print output
