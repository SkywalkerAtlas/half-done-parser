# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

import re
import itertools
from ItemCollection import getItemCollection
from grammer_symbol import get_grammer_symbol

DFA = []

def getClouse(item_sets,grammer_productions_list):
	item_cloused = []
	for eachItem in item_sets:
		m = re.search('`[A-Z]', eachItem)
		if m is not None:
			for eachGram in grammer_productions_list:
				if eachGram.split('->')[0] == (m.group()[1]):
					new_item = m.group()[1] + '->`' + eachGram.split('->')[1]
					if new_item not in item_sets:
						item_sets.append(new_item)
	item_cloused = item_sets
	return item_cloused

def move_dot(st):
	m = re.search('(.*)[`](.)(.*)', st)
	new_st = m.group(1) + m.group(2) + '`' + m.group(3)
	return new_st

def GOTO(I,X,grammer_productions_list):
	# print I,X
	item_sets = []
	for eachItem in I[1]:
		# print eachItem
		pattern = '`[' + str(X)+']'
		m = re.search(pattern, eachItem)
		if m is not None:
			moved_item = move_dot(eachItem)
			item_sets.append(moved_item)
			# print item_sets
			# print m.group()
	item_sets = getClouse(item_sets,grammer_productions_list)
	if len(item_sets) == 0:
		return None
	else:
		return item_sets

def get_cannonical_collection(items_list,grammer_productions_list):
	C_dict = {}
	item_sets_n_count = 0
	item_sets_list = []
	item_sets_list.append(items_list[0])
	item_sets_list = getClouse(item_sets_list,grammer_productions_list)
	C_dict['I_'+str(item_sets_n_count)] = item_sets_list
	while True:
		flag = 0
		for each_I,items_in_each_I in C_dict.items():
			# print each_I,items_in_each_I
			for each_grammer_symbol in gram_symbol:
				generated_item = GOTO((each_I,items_in_each_I),each_grammer_symbol,grammer_productions_list)
				if generated_item is not None and generated_item not in C_dict.values():
					item_sets_n_count = item_sets_n_count + 1
					C_dict['I_'+str(item_sets_n_count)] = generated_item
					flag = 1
		if flag == 0:
			break
	return C_dict

if __name__ == '__main__':
	items_list,grammer_productions_list = getItemCollection("grammer.txt")
	gram_symbol = get_grammer_symbol(grammer_productions_list)
	C_dict = get_cannonical_collection(items_list,grammer_productions_list)
	print C_dict
