import app.converter as converter
import app.outputer as outputer
import common.util as util

import sys
import os
import importlib
import inspect
import argparse
import traceback

def importModules(path) :
	moduleList = []
	fileList = os.listdir(path)
	for file in fileList :
		fullFileName = os.path.join(path, file)
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
		self._converterList = []
		self._outputerMap = {}
		self._outputerList = []
		self._converter = None
		self._outputer = None

	def run(self) :
		try :
			self._doRun()
		except Exception as e:
			print(str(e))
			traceback.print_exc()

	def _doRun(self) :
		self._loadModules()
		self._parseCommandLine(sys.argv[1:])
		convertedResult = self._converter.convert()
		self._outputer.output(convertedResult)

	def _loadModules(self) :
		self._converterMap, self._converterList = self._loadModuleMap('converters', converter.Converter)
		self._outputerMap, self._outputerList = self._loadModuleMap('outputers', outputer.Outputer)

	def _loadModuleMap(self, path, baseClass) :
		moduleMap = {}
		moduleList = []
		importedList = importModules(path)
		for module in importedList :
			for _, cls in inspect.getmembers(module, inspect.isclass) :
				if issubclass(cls, baseClass) :
					nameList = cls.getNameList()
					if util.isString(nameList) :
						nameList = [ nameList ]
					for name in nameList :
						moduleMap[name] = cls
					moduleList.append(cls)
		return moduleMap, moduleList

	def _parseCommandLine(self, commandLineArguments) :
		parser = argparse.ArgumentParser(add_help = False)
		parserWrapper = ArgParserWrapper(parser)
		parser.add_argument('--help', action = 'store_true')
		parser.add_argument('-h', action = 'store_true', dest = 'help')
		parserWrapper.add_argument('--converter', type = str, help = "Converter name", default = 'digit')
		parserWrapper.add_argument('--outputer', type = str, help = "Outputer name", default = 'midi')
		for convert in self._converterList :
			convert.setupArgumentParser(parserWrapper)
		for outputer in self._outputerList :
			outputer.setupArgumentParser(parserWrapper)
		options, _ = parser.parse_known_args(commandLineArguments)
		options = vars(options)
		#print(options)
		convertName = options['converter']
		if convertName not in self._converterMap :
			raise Exception('Unknown converter %s' % (convertName))
		self._converter = self._converterMap[convertName]()
		self._converter.setName(convertName)
		outputerName = options['outputer']
		if outputerName not in self._outputerMap :
			raise Exception('Unknown converter %s' % (outputerName))
		self._outputer = self._outputerMap[outputerName]()
		self._outputer.setName(outputerName)
		self._converter.parsedArguments(options)
		self._outputer.parsedArguments(options)

class ArgParserWrapper :
	def __init__(self, argParser) :
		self._argParser = argParser
		self._argumentMap = {}
	
	def add_argument(self, name, default = None, type = str, help = '', dest = None) :
		if name in self._argumentMap :
			return
		self._argumentMap[name] = True
		self._argParser.add_argument(
			name,
			default = default,
			type = type,
			help = help,
			dest = dest
		)
