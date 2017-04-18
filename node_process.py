# -*- coding: utf8 -*-
from enum import Enum
class node_info(Enum):

	index = 0
	word = 1
	start = 2
	end = 3
	pos = 4
	liaison = 5
	syllable = 6
	cons = 7			#last alphabet is consonant
	cons_v = 8 			#consonant_value
	vowe = 9			#first alphabet is vowel
	vowe_v = 10			#vowel_value
	dash = 11			# word with dash
	special_begin = 12	#Begin in D' J' L' T'


def set_nodes(words,pos,liaison):

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

def set_word_syllable(nodes_list,french_dict):

	for node in nodes_list:
		if node[node_info.word.value] is "\n":continue
		if node[node_info.word.value][-1] is "." or node[node_info.word.value][-1] is ",":
			word = node[node_info.word.value][0:-1].lower()
		else:
			word = node[node_info.word.value].lower()
		if word in french_dict:
			node.append(french_dict[word])
		else:			
			node.append("Not_found_in_dict")

def check_four_rule(node_list):

	
	consonant = ["p","t","d","s","z","x","n","m","g"]
	vowel = ["A","a","À","à","Â","â","Æ","æ","E","e","É","é","È","è","Ê","ê","Ë","ë","H","h","I","i","Î","î","Ï","ï","O","o","Ô","ô","Œ","œ","U","u","Ù","ù","Û","û","Ü","ü","Y","y","Ÿ","ÿ"]
	spec_begin = ["d\'","j\'","l\'","t\'"]
	word_begin = ""

	for node in node_list:

		if node[node_info.word.value] is "\n":continue
		#check last consonant and first vowel
		if node[node_info.word.value][-1] in consonant:
			node.append("True") 
			node.append(node[node_info.word.value][-1])
		else:
			node.append("False") 
			node.append(" ")
		if node[node_info.word.value][0] in vowel:
			node.append("True") 
			node.append(node[node_info.word.value][0])
		else:
			node.append("False") 
			node.append(" ")
		
		#check word with dash
		if "-" in node[node_info.word.value]:
			node.append("True")
		else:
			node.append("False")
	
		#check D' J' L' T'
		if len(node[node_info.word.value]) > 1:
			word_begin = node[node_info.word.value][0:2].lower()
		else:
			word_begin = node[node_info.word.value][0].lower
		if word_begin in spec_begin:
			node.append("True")
		else:
			node.append("False")