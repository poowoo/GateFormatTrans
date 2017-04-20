# -*- coding: utf8 -*-
import sys
import os
import xml
import node_process

def find_line_node_index(begin,size,nodes_list):

	end = 0
	for i in range(begin,len(nodes_list)): #node index
		node = nodes_list[i]
		if size == 0:break
		if node[node_process.node_info.word.value] is "\n":
			end = i
			size -= 1
	return end

def file_xml_format(nodes_list,out_fn):	
	
	
	out_fn_len = out_fn.find(".")
	last_index = 0
	i = 0
	while  i < len(nodes_list):

		
		new_out_fn = out_fn[0:out_fn_len] + "_" + str(i).zfill(2) + ".xml"
		
		print("make " + new_out_fn)
		xml.write_header(new_out_fn)
		xml.write_gatedocument_begin(new_out_fn)
		xml.write_gatedocument_feature(new_out_fn,os.path.abspath(sys.argv[1]))		

		file_line = find_line_node_index(last_index,10000,nodes_list)
		xml.write_textwithnodes(new_out_fn,nodes_list,last_index,file_line)
		xml.write_annotation_set(new_out_fn,nodes_list,last_index,file_line)

		xml.write_gatedocument_end(new_out_fn)
		last_index = file_line + 1
		if file_line == len(nodes_list)-1:
			break
		i += 1
	

def read_fixed_format_txt(fn):

	wor=[] #word
	pos=[] #part of speech 
	lia=[] #liaision

	with open(fn, mode='r', encoding='UTF-8') as file:

		for line in file:		
			line = line.strip()
			line = line.split(" ")
			for token in line:
				token = token.split("|")
				wor.append(token[0])
				pos.append(token[1])
				lia.append(token[2])
			wor.append("\n")
			pos.append("NL")
			lia.append("N")

	return wor,pos,lia

def read_french_dict(fn):
	
	french_dict = {}
	syllables = 0
	with open(fn, mode='r', encoding='UTF-8') as file:	

		for line in file:
			if line[0] is "#":continue		
			line = line.strip()
			line = line.split(",")
			syllables = 0
			for i in range(len(line[-1])):
				if line[-1][i] is "0" :#or  line[-1][i] is "0"
					syllables += 1
			if not line[0] in french_dict:
				french_dict[line[0]] = str(syllables)
			elif french_dict[line[0]] != str(syllables):
				french_dict[line[0]] += ","+ str(syllables)
			

	return french_dict
if __name__ == "__main__":
	
	print("load txt")
	lang_word,lang_pos,lang_liaision = read_fixed_format_txt(sys.argv[1])
	print("load dictonary")
	french_dict = read_french_dict(sys.argv[3])
	print("set nodes")
	nodes_list = node_process.set_nodes(lang_word,lang_pos,lang_liaision)
	print("set syllables")
	node_process.set_word_syllable(nodes_list,french_dict)
	print("set four rule")
	node_process.check_four_rule(nodes_list)
	print("save to xml")
	file_xml_format(nodes_list,sys.argv[2])