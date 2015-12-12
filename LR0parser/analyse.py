# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

from parse_input import parse_input
from gen_table import gen_table
from collections import deque
from ItemCollection import getItemCollection

def ACTION(sm,aj,SLR1_tabel):
	if SLR1_tabel[sm].has_key(aj):
		return SLR1_tabel[sm][aj]
	else:
		return 'error'

def do_GOTO(sm_r,A,SLR1_tabel):
	destination = ACTION(sm_r,A,SLR1_tabel)
	if destination != 'error':
		return int(destination)
	else:
		return destination

def move_in(status_deque,symbol_deque,input_deque,next_action):
	append_status = int(next_action.strip('S'))
	status_deque.append(append_status)
	a = input_deque.popleft()
	symbol_deque.append(a)

def do_reduce(status_deque,symbol_deque,input_deque,next_action,SLR1_tabel,grammer_productions_list):
	production_num = int(next_action.strip('r'))
	r_length = len(grammer_productions_list[production_num].split('->')[1])
	left_part = grammer_productions_list[production_num].split('->')[0]

	#弹出产生式长度的r个状态符号
	for i in range(r_length):
		status_deque.pop()
		symbol_deque.pop()

	destination = do_GOTO(status_deque[-1],left_part,SLR1_tabel)

	if destination != 'error':
		status_deque.append(destination)
		symbol_deque.append(left_part)
		return 'OK'
	else:
		return destination

def do_analyse(SLR1_tabel,inputed_parse,grammer_productions_list):
	row_count = 0
	status_deque = deque([0])
	symbol_deque = deque([])
	input_deque = deque(list(inputed_parse))
	accpet = False
	analyse_result_array = []
	while not accpet:
		row_count = row_count + 1
		analyse_result_array.append([row_count,str(status_deque).strip('deque()'),str(symbol_deque).strip('deque()'),str(input_deque).strip('deque()')])
		# print ('{0:3} {1:28} {2:28} {3:>50}'.format(row_count,\
		# 	str(status_deque).strip('deque()'),\
		# 	str(symbol_deque).strip('deque()'),\
		# 	str(input_deque).strip('deque()')))
		# print row_count,'  ',status_deque,'  ',symbol_deque,'  ',input_deque,'  '
		next_action = ACTION(status_deque[-1],input_deque[0],SLR1_tabel)
		if next_action == 'acc':
			accpet = True
			analyse_result_array[-1].append('accpet')
			return next_action,analyse_result_array
		if next_action == 'error':
			return next_action,0
		if next_action.startswith('S'):
			move_in(status_deque,symbol_deque,input_deque,next_action)
			analyse_result_array[-1].append('move_in')
		elif next_action.startswith('r'):
			destination = do_reduce(status_deque,symbol_deque,input_deque,next_action,SLR1_tabel,grammer_productions_list)
			analyse_result_array[-1].append('reduce:'+grammer_productions_list[int(next_action.strip('r'))])
			if destination == 'error':
				return 'error',0
	return '?'

if __name__ == '__main__':
	inputed_parse = parse_input()
	SLR1_tabel = gen_table('grammer.txt')
	items_list,grammer_productions_list = getItemCollection("grammer.txt")

	result,analyse_result_array = do_analyse(SLR1_tabel,inputed_parse,grammer_productions_list)
	print analyse_result_array
	print result
