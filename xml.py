# -*- coding: utf8 -*-
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

def xml_write_textwithnodes(fn,words):

	node_index_l = []
	node_index = 0
	out = open(fn, mode='a', encoding='UTF-8')	
	out.write("<TextWithNodes>")
	for word in words:
		if word is '\n':
			out.write("&#xd;\n")
		else:			
			out.write("<Node id=\""+str(node_index)+"\"/>")
			node_index_l.append(node_index)
			node_index += len(word)
			out.write(word+"<Node id=\""+str(node_index)+"\"/> ")
			node_index_l.append(node_index)
			node_index += 1			
	out.write("</TextWithNodes>\n")
	out.close()
	return node_index_l

def xml_write_annotation_set(fn,word,pos,liasion,node_index_list):
	
	node_index = 0	
	anno_index = 0
	liasion_type =""
	liasion_boolean = ""
	next_line_count = 0
	out = open(fn, mode='a', encoding='UTF-8')
	out.write("<AnnotationSet>\n")
	#xml pos
	for p in pos:
		if p is not "NL":		
			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\""+p+"\" StartNode=\""+str(node_index_list[node_index])+"\" EndNode=\""+str(node_index_list[node_index+1])+"\">\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">part of speech</Name>\n")
			out.write("  <Value className=\"java.lang.String\">"+p+"</Value>\n")
			out.write("</Feature>\n")
			out.write("</Annotation>\n")
			node_index += 2
			anno_index += 1
	
	node_index = 0
	#xml liasion
	for l in liasion:
		if l is not "N":
			if l is "T":
				liasion_type = "Liasion_True"
				liasion_boolean = "true"
			else:
				liasion_type = "Liasion_False"
				liasion_boolean = "false"
			out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\""+liasion_type+"\" StartNode=\""+str(node_index_list[node_index])+"\" EndNode=\""+str(node_index_list[node_index+1])+"\">\n")
			out.write("<Feature>\n")
			out.write("  <Name className=\"java.lang.String\">liasion</Name>\n")
			out.write("  <Value className=\"java.lang.Boolean\">"+liasion_boolean+"</Value>\n")
			out.write("</Feature>\n")
			out.write("</Annotation>\n")
			node_index += 2
			anno_index += 1
	#xml special case

	for i in range(len(pos)):
		if pos[i] is not "NL":
			if pos[i] is "V" and pos[i+1] is "N" and liasion[i+1] is "T":
				out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\"V+N and liasion ture\" StartNode=\""+str(node_index_list[(i-next_line_count)*2])+"\" EndNode=\""+str(node_index_list[(i-next_line_count)*2+3])+"\">\n")			
				out.write("</Annotation>\n")						
			elif pos[i] is "V" and pos[i+1] is "N" and liasion[i+1] is "F":
				out.write("<Annotation Id=\""+str(anno_index)+"\" Type=\"V+N and liasion false\" StartNode=\""+str(node_index_list[(i-next_line_count)*2])+"\" EndNode=\""+str(node_index_list[(i-next_line_count)*2+3])+"\">\n")			
				out.write("</Annotation>\n")			
			anno_index += 1
		else:
			next_line_count += 1	
	out.write("</AnnotationSet>\n")
	out.close()