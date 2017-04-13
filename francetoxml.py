# -*- coding: utf8 -*-
import sys
import os
#from xml

def file_xml_format(wor,pos,lia,out_fn):


	out = open(out_fn, mode='w', encoding='UTF-8')
	#print gate_documentfeature
	#print text
	#print annotation_set
	out.write("<?xml version='1.0' encoding='utf-8'?>")
	out.write("<GateDocument version=\"3\">")
	out.write("<GateDocumentFeatures>")
	out.write("<Feature>")
  	out.write("  <Name className=\"java.lang.String\">gate.SourceURL</Name>")
  	out.write("  <Value className=\"java.lang.String\">file:/C:/Users/david_hung/Desktop/en-corpus.txt</Value>")
	out.write("</Feature>")
	out.write("<Feature>")
	out.write("  <Name className=\"java.lang.String\">MatchesAnnots</Name>")
	out.write("  <Value className=\"gate.corpora.ObjectWrapper\"><![CDATA[<?xml version='1.1'?><gate.corpora.ObjectWrapper><value class=\"map\"><entry><null/><list><list><int>1657</int><int>1659</int><int>1663</int><int>1664</int></list></list></entry></value></gate.corpora.ObjectWrapper>]]></Value>")
	out.write("</Feature>")
	out.write("<Feature>")
	out.write("  <Name className=\"java.lang.String\">MimeType</Name>")
	out.write("  <Value className=\"java.lang.String\">text/plain</Value>")
	out.write("</Feature>")
	out.write("<Feature>")
	out.write("  <Name className=\"java.lang.String\">docNewLineType</Name>")
	out.write("  <Value className=\"java.lang.String\">CRLF</Value>")
	out.write("</Feature>")
	out.write("</GateDocumentFeatures>")

	out.close()
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