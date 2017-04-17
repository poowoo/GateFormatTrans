# -*- coding: utf8 -*-
from enum import Enum
class node_info(Enum):
	index = 0
	word = 1
	start = 2
	end = 3
	pos = 4
	liaison = 5

def xml_write_header(fn):

	out = open(fn, mode='w', encoding='UTF-8')
	out.write("<?xml version='1.0' encoding='utf-8'?>\n")
	out.close()

def xml_write_gatedocument_begin(fn):

	out = open(fn, mode='a', encoding='UTF-8')	
	out.write("<GateDocument version=\"3\">\n")
	out.close()

def xml_write_gatedocument_end(fn):

	out = open(fn, mode='a', encoding='UTF-8')
	out.write("</GateDocument>\n")
	out.close()

def xml_write_gatedocument_feature(fn,abspath):

	out = open(fn, mode='a', encoding='UTF-8')
	out.write("<GateDocumentFeatures>\n")
	out.write("<Feature>\n")
	out.write("  <Name className=\"java.lang.String\">gate.SourceURL</Name>\n")
	out.write("  <Value className=\"java.lang.String\">"+abspath+"</Value>\n")
	out.write("</Feature>\n")
	out.write("<Feature>\n")
	out.write("  <Name className=\"java.lang.String\">MatchesAnnots</Name>\n")
	out.write("  <Value className=\"gate.corpora.ObjectWrapper\"><![CDATA[<?xml version='1.1'?><gate.corpora.ObjectWrapper><value class=\"map\"><entry><null/><list><list><int>1657</int><int>1659</int><int>1663</int><int>1664</int></list></list></entry></value></gate.corpora.ObjectWrapper>]]></Value>\n")
	out.write("</Feature>\n")
	out.write("<Feature>\n")
	out.write("  <Name className=\"java.lang.String\">MimeType</Name>\n")
	out.write("  <Value className=\"java.lang.String\">text/plain</Value>\n")
	out.write("</Feature>\n")
	out.write("</GateDocumentFeatures>\n")
	out.close()

def xml_write_textwithnodes(fn,nodes_list):
	
	out = open(fn, mode='a', encoding='UTF-8')	
	out.write("<TextWithNodes>")
	for node in nodes_list:
		if node[node_info.word.value] is "\n":
			out.write("&#xd;\n")
		else:			
			out.write("<Node id=\""+str(node[node_info.start.value])+"\"/>"+node[node_info.word.value]+"<Node id=\""+str(node[node_info.end.value])+"\"/> ")
	out.write("</TextWithNodes>\n")
	out.close()	

def xml_write_annotation_set(fn,nodes_list):
		
	anno_index = 0
	liaison_type =""		
	out = open(fn, mode='a', encoding='UTF-8')
	out.write("<AnnotationSet>\n")
	#xml word
	for node in nodes_list:
		if node[node_info.word.value] is not "\n":		
			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\"word\" StartNode=\""+str(node[node_info.start.value])+"\" EndNode=\""+str(node[node_info.end.value])+"\">\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">string</Name>\n")
			out.write("  <Value className=\"java.lang.String\">"+node[node_info.word.value]+"</Value>\n")
			out.write("</Feature>\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">part of speech</Name>\n")
			out.write("  <Value className=\"java.lang.String\">"+node[node_info.pos.value]+"</Value>\n")
			out.write("</Feature>\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">liaison</Name>\n")
			out.write("  <Value className=\"java.lang.Boolean\">"+node[node_info.liaison.value]+"</Value>\n")
			out.write("</Feature>\n")
			out.write("</Annotation>\n")			
			anno_index += 1
	#xml pos
	for node in nodes_list:
		if node[node_info.word.value] is not "\n":		
			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\""+node[node_info.pos.value]+"\" StartNode=\""+str(node[node_info.start.value])+"\" EndNode=\""+str(node[node_info.end.value])+"\">\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">part of speech</Name>\n")
			out.write("  <Value className=\"java.lang.String\">"+node[node_info.pos.value]+"</Value>\n")
			out.write("</Feature>\n")
			out.write("</Annotation>\n")			
			anno_index += 1
	
	#xml liaison
	for node in nodes_list:
		if node[node_info.word.value] is not "\n":
			if node[node_info.liaison.value] is "True":
				liaison_type = "liaison_True"				
			else:
				liaison_type = "liaison_False"				
			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\""+liaison_type+"\" StartNode=\""+str(node[node_info.start.value])+"\" EndNode=\""+str(node[node_info.end.value])+"\">\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">liaison</Name>\n")
			out.write("  <Value className=\"java.lang.Boolean\">"+node[node_info.liaison.value]+"</Value>\n")
			out.write("</Feature>\n")
			out.write("</Annotation>\n")			
			anno_index += 1
	#xml special case

	#for i in range(len(pos)):
	#	if pos[i] is not "NL":
	#		if pos[i] is "V" and pos[i+1] is "N" and liaison[i+1] is "T":
	#			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\"V+N and liaison ture\" StartNode=\""+str(node_index_list[(i-next_line_count)*2])+"\" EndNode=\""+str(node_index_list[(i-next_line_count)*2+3])+"\">\n")			
	#			out.write("</Annotation>\n")						
	#		elif pos[i] is "V" and pos[i+1] is "N" and liaison[i+1] is "F":
	#			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\"V+N and liaison false\" StartNode=\""+str(node_index_list[(i-next_line_count)*2])+"\" EndNode=\""+str(node_index_list[(i-next_line_count)*2+3])+"\">\n")			
	#			out.write("</Annotation>\n")			
	#		anno_index += 1
	#	else:
	#		next_line_count += 1	
	out.write("</AnnotationSet>\n")
	out.close()

def xml_set_nodes(words,pos,liaison):

	nodes_list = []
	#node = [] # node index, word, start_index , end_index , pos , liaison 
	node_index = 0
	for i in range(len(words)):
		node = []
		if words[i] is not "\n" and pos[i] is not "NL" and liaison[i] is not "N":			
			node.append(i)
			node.append(words[i])
			node.append(node_index)
			node_index += len(words[i])
			node.append(node_index)
			node_index += 1
			node.append(pos[i])
			if liaison[i] is "T":
				node.append("True")
			else:
				node.append("False")
		else:
			node.append(i)
			node.append("\n")
		nodes_list.append(node)
	return nodes_list
