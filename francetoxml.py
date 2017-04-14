# -*- coding: utf8 -*-
import sys
import os

from xml import xml_write_header
from xml import xml_write_gatedocument_begin
from xml import xml_write_gatedocument_end
from xml import xml_write_gatedocument_feature
from xml import xml_write_textwithnodes
from xml import xml_write_annotation_set

def file_xml_format(wor,pos,lia,out_fn):	
	#print annotation_set
	node_index_list = []

	xml_write_header(out_fn)
	xml_write_gatedocument_begin(out_fn)
	xml_write_gatedocument_feature(out_fn,os.path.abspath(sys.argv[1]))
	node_index_list = xml_write_textwithnodes(out_fn,wor)
	xml_write_annotation_set(out_fn,wor,pos,lia,node_index_list)
	xml_write_gatedocument_end(out_fn)
	#out.close()

def read_fixed_format_txt(fn):

	wor=[] #word
	pos=[]	#part of speech 
	lia=[] #liasion

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

if __name__ == "__main__":

	lang_word,lang_pos,lang_liasion = read_fixed_format_txt(sys.argv[1])
	file_xml_format(lang_word,lang_pos,lang_liasion,sys.argv[2])