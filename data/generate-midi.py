import sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')

import converters.digitconverter as digitconverter
import converters.letterconverter as letterconverter
import converters.unicodeconverter as unicodeconverter
import common.util as util

import os
import glob
import argparse

class Application :
	def __init__(self) :
		self._dataPath = './'
		self._outputPath = '/temp/test'
		self._tempo = None
		self._instrument = None

	def run(self) :
		self._parseCommandLine(sys.argv[1:])
		dataFileList = self._loadDataFiles()
		for dataFile in dataFileList :
			self._convertDataFile(dataFile)

	def _parseCommandLine(self, commandLineArguments) :
		parser = argparse.ArgumentParser(add_help = False)

	def _loadDataFiles(self) :
		files = glob.glob(os.path.join(self._dataPath, '*.txt'))
		return files

	def _convertDataFile(self, dataFile) :
		converterList = self._detectDataFileConverters(dataFile)
		if converterList is None :
			print("Can't detect converter for %s" % (dataFile))
			return
		for converter in converterList :
			self._convertDataFileWithConverter(dataFile, converter)

	def _convertDataFileWithConverter(self, dataFile, converter) :
		outputFileName = self._makeOutputFileName(dataFile, converter)
		command = 'python datomu.py'
		command += ' --converter %s' % (converter)
		command += ' --outputer midi'
		command += ' --data-file "%s"' % (os.path.abspath(dataFile))
		command += ' --output-file "%s"' % (outputFileName)
		fullCommand = 'cd .. && %s' % (command)
		print(fullCommand)
		os.system(fullCommand)

	def _makeOutputFileName(self, dataFile, converter) :
		fileName = os.path.basename(dataFile)
		fileName = util.replaceFileExtension(fileName, '')
		fileName += '-' + converter
		if self._tempo is not None :
			fileName += '-%sbpm' % (str(self._tempo))
		if self._instrument is not None :
			fileName += '-instrument%s' % (str(self._instrument))
		fileName += '.mid'
		fileName = os.path.join(self._outputPath, fileName)
		return fileName

	def _detectDataFileConverters(self, dataFile) :
		content = util.readTextFile(dataFile)
		digitCount = 0
		letterCount = 0
		unicodeCount = 0
		for char in content :
			if char.isdigit() :
				digitCount += 1
			elif char.lower() in 'abcdefghijklmnopqrstuvwxyz' :
				letterCount += 1
			elif ord(char) > 127 :
				unicodeCount += 1
		if digitCount >= letterCount and digitCount >= unicodeCount :
			return digitconverter.nameScaleMap.keys()
		if letterCount >= digitCount and letterCount >= unicodeCount :
			return letterconverter.nameScaleMap.keys()
		if unicodeCount >= digitCount and unicodeCount >= letterCount :
			return unicodeconverter.nameScaleMap.keys()
		return None


Application().run()
