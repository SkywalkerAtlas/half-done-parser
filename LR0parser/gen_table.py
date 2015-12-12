# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from cannonical_collection import DFA,get_cannonical_collection
from ItemCollection import getItemCollection
from grammer_symbol import get_grammer_symbol
from follow import get_follow
from first import get_first

def gen_table(file_name):
	SLR1_table = {}

	items_list,grammer_productions_list = getItemCollection(file_name)
	gram_symbol = get_grammer_symbol(grammer_productions_list)
	C_dict = get_cannonical_collection(items_list,grammer_productions_list,gram_symbol)
	follow = get_follow(file_name)
	
	non_terminals_list = []
	terminals_list = []
	for each_symbol in gram_symbol:
		if each_symbol.istitle():
			non_terminals_list.append(each_symbol)
		else:
			terminals_list.append(each_symbol)
	terminals_list.append('#')


	for each_statu in C_dict.keys():
		each_statu_for_SLR1_table_key = int(each_statu.split('_')[1])
		SLR1_table[each_statu_for_SLR1_table_key] = {}
		for each_item in C_dict[each_statu]:

			if not each_item.endswith('`'):
				char_behind = each_item[each_item.index('`')+1]
				for each_goto in DFA[each_statu]:
					edge_end = each_goto.strip('--')
					if edge_end.startswith(char_behind):
						end = edge_end.split('->I_')[1]
						if char_behind in terminals_list:
							SLR1_table[each_statu_for_SLR1_table_key][char_behind] = 'S'+end
						else:
							if char_behind not in SLR1_table[each_statu_for_SLR1_table_key].keys():
								SLR1_table[each_statu_for_SLR1_table_key][char_behind] = end

			elif each_item.endswith('`') and each_item.split('->')[0] != non_terminals_list[0]:
				left_part = each_item.split('->')[0]
				if each_item.strip('`') != grammer_productions_list[0]:
					for each_a in follow[left_part]:
						SLR1_table[each_statu_for_SLR1_table_key][each_a] = 'r'+str(grammer_productions_list.index(each_item.strip('`')))

			else:
				SLR1_table[each_statu_for_SLR1_table_key]['#'] = 'acc'

	return SLR1_table

if __name__ == '__main__':
	SLR1_table = gen_table('grammer.txt')
	for key,item in SLR1_table.items():
		print key,item