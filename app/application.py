import app.converter as converter
import app.outputer as outputer

import sys
import os
import importlib
import inspect
import argparse

def importModules(path) :
	moduleList = []
	fileList = os.listdir(path)
	for file in fileList :
		fullFileName = path + os.sep + file
		if os.path.isfile(fullFileName) and file.endswith('.py') :
			packageName = fullFileName
			packageName = packageName[0 : -3]
			packageName = packageName.replace('\\', '.')
			packageName = packageName.replace('/', '.')
			module = importlib.import_module(packageName)
			moduleList.append(module)
	return moduleList

class Application :
	def __init__(self) :
		self._converterMap = {}
		self._outputerMap = {}
		self._converterName = 'simple'
		self._outputerName = 'midi'

	def run(self) :
		self._loadModules()
		runIt = self._parseCommandLine(sys.argv[1:])
		converter = self._converterMap[self._converterName]()
		outputer = self._outputerMap[self._outputerName]()
		text = '3.14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 '
		#text = '3.14159 26535 '
		convertedResult = converter.convert(text)
		outputer.output(convertedResult)

	def _loadModules(self) :
		self._converterMap = self._loadModuleMap('converters', converter.Converter)
		self._outputerMap = self._loadModuleMap('outputers', outputer.Outputer)

	def _loadModuleMap(self, path, baseClass) :
		moduleMap = {}
		moduleList = importModules(path)
		for module in moduleList :
			for _, obj in inspect.getmembers(module, inspect.isclass) :
				if issubclass(obj, baseClass) :
					moduleMap[obj.getName()] = obj
					break
		return moduleMap

	def _parseCommandLine(self, commandLineArguments) :
		parser = argparse.ArgumentParser(add_help = False)
		parser.add_argument('--help', action = 'store_true')
		parser.add_argument('-h', action = 'store_true', dest = 'help')
