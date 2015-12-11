# -*- encoding: utf-8 -*-

__author__ = 'SkywalkerAtlas'

import BNF

def getItemCollection(file_name):
	grammer_productions_list = BNF.getBNF(file_name)
	items_list = []
	for eachPro in grammer_productions_list:
		left_part = eachPro.split('->')[0] + '->'
		right_part = eachPro.split('->')[1]
		items_list.append(left_part + '`' + right_part)
		right_part_list = list(right_part)

		for eachWord in right_part:
			point_loc = right_part_list.index(eachWord) + 1
			right_part_list.insert(point_loc, '`')
			items_list.append(left_part + ''.join(right_part_list))
			right_part_list.remove('`')
	return items_list,grammer_productions_list

if __name__ == '__main__':
    output = getItemCollection('grammer.txt')
    print output[0]
    print output[1]
