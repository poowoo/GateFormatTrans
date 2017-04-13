# -*- coding: utf8 -*-
def write_header(fn):
	out = open(fn, mode='w', encoding='UTF-8')
	out.write("<?xml version='1.0' encoding='utf-8'?>")
	out.close()