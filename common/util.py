import os
import codecs
import time
import random
import re

def readTextFile(fileName) :
	with codecs.open(fileName, "r", "utf-8") as file :
		return file.read()

def replaceFileExtension(fileName, extension) :
	fileName, _ = os.path.splitext(fileName)
	return fileName + extension 

def getDictValue(dict, key, default = None) :
	if dict != None and key in dict :
		return dict[key]
	return default

def isString(s) :
	return isinstance(s, str)

def findItemInList(list, item) :
	if item in list :
		return list.index(item)
	return -1

def splitByCommaOrSpace(text) :
	return re.split(r'\s*,\s*|\s+', text)

