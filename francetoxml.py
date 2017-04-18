# -*- coding: utf8 -*-
import sys
import os
import xml
import node_process

def file_xml_format(nodes_list,out_fn):	
	
	xml.write_header(out_fn)
	xml.write_gatedocument_begin(out_fn)
	xml.write_gatedocument_feature(out_fn,os.path.abspath(sys.argv[1]))		
	xml.write_textwithnodes(out_fn,nodes_list)
	xml.write_annotation_set(out_fn,nodes_list)
	xml.write_gatedocument_end(out_fn)	

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
	
	lang_word,lang_pos,lang_liaision = read_fixed_format_txt(sys.argv[1])
	french_dict = read_french_dict(sys.argv[3])

	nodes_list = node_process.set_nodes(lang_word,lang_pos,lang_liaision)
	node_process.set_word_syllable(nodes_list,french_dict)
	node_process.check_four_rule(nodes_list)

	file_xml_format(nodes_list,sys.argv[2])