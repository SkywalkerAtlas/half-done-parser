# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

import re
from ItemCollection import getItemCollection

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

def GOTO(I,X):

	return

def get_cannonical_collection(items_list,grammer_productions_list):
	C_dict = {}
	item_sets_n_count = 0
	item_sets_list = []
	item_sets_list.append(items_list[0])
	item_sets_list = getClouse(item_sets_list,grammer_productions_list)
	C_dict['I_'+str(item_sets_n_count)] = item_sets_list
	for each_set_of_items in C_dict:
		for each_grammer_symbol in gram_symbol
	return C_dict

if __name__ == '__main__':
	items_list,grammer_productions_list = getItemCollection("grammer.txt")
	C_dict = get_cannonical_collection(items_list,grammer_productions_list)
	print C_dict
