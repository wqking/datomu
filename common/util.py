import os
import codecs
import time
import random
import re

def getDictValue(dict, key, default = None) :
	if dict != None and key in dict :
		return dict[key]
	return default

def trim(text) :
	if text is None :
		return text
	return text.strip()

def trimRight(text) :
	if text is None :
		return text
	return text.rstrip()

def isString(s) :
	return isinstance(s, str)

def findItemInList(list, item) :
	if item in list :
		return list.index(item)
	return -1

def splitByCommaOrSpace(text) :
	return re.split(r'\s*,\s*|\s+', text)

