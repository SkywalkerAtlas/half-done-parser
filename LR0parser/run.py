# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from parse_input import parse_input
from gen_table import gen_table
from collections import deque
from grammer_symbol import get_grammer_symbol
from ItemCollection import getItemCollection
from analyse import do_analyse
from cannonical_collection import get_cannonical_collection
from cannonical_collection import DFA
from pylsy import pylsytable

if __name__ == '__main__':
	file_name = raw_input('input file name which contains grammer(eg:grammer.txt):>').strip()
	# file_name = 'grammer.txt'
	SLR1_tabel = gen_table(file_name)
	items_list,grammer_productions_list = getItemCollection(file_name)
	print 'augmented grammar is:\nG\':'
	for each in grammer_productions_list:
		print each

	
	non_terminals_list = []
	terminals_list = []
	grammer_symbol = get_grammer_symbol(grammer_productions_list)
	C_dict = get_cannonical_collection(items_list,grammer_productions_list,grammer_symbol)
	for each_symbol in grammer_symbol:
		if each_symbol.istitle():
			non_terminals_list.append(each_symbol)
		else:
			terminals_list.append(each_symbol)

	print '==================================================='
	print 'cannonical LR(0) collection:'
	for key,val in C_dict.items():
		print key,val
	print '==================================================='
	print 'DFA:'
	for key,val in DFA.items():
		print key,val
	print '==================================================='
	print 'Parsing table for expression grammar:'
	attributes = ['status']
	terminals_list.append('#')
	attributes.extend(terminals_list)
	non_terminals_list.pop(0)
	attributes.extend(non_terminals_list)
	table = pylsytable(attributes)
	table.add_data('status', SLR1_tabel.keys())
	for key in SLR1_tabel.keys():
		for each in terminals_list+non_terminals_list:
			if SLR1_tabel[key].has_key(each):
				table.append_data(each, SLR1_tabel[key][each])
			else:
				table.append_data(each, ' ')
	print(table)
	print '==================================================='

	inputed_parse = parse_input()
	print 'Moves of an LR parser on '+inputed_parse+':'
	result,analyse_result_array = do_analyse(SLR1_tabel,inputed_parse,grammer_productions_list)

	#保证输出的间隔比该列的最长序列多2
	def x(each_step,next_step):
		return str(each_step[0]) if len(str(each_step[0]))>len(str(next_step[0])) else str(next_step[0]),\
		each_step[1] if len(each_step[1])>len(next_step[1]) else next_step[1],\
		each_step[2] if len(each_step[2])>len(next_step[2]) else next_step[2],\
		each_step[3] if len(each_step[3])>len(next_step[3]) else next_step[3],\
		each_step[4] if len(each_step[4])>len(next_step[4]) else next_step[4]
	# for each_step in analyse_result_array:
	# 	len_1,len_2,len_3,len_4 = x(each_step)
	len_0,len_1,len_2,len_3,len_4 = map(lambda l:len(l)+2,reduce(x,[each_step for each_step in analyse_result_array]))
	output_str = '{0:<'+str(len_0)+'}{1:'+str(len_1)+'}{2:'+str(len_2)+'}{3:>'+str(len_3)+'}  {4:'+str(len_4)+'}'
	for each_step in analyse_result_array:
		print (output_str.format(each_step[0],\
			each_step[1],\
			each_step[2],\
			each_step[3],\
			each_step[4]))

	print result
