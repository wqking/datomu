import sys
sys.path.insert(0,'..')
sys.path.insert(0,'.')

import converters.digitconverter as digitconverter
import converters.letterconverter as letterconverter
import converters.unicodeconverter as unicodeconverter
import converters.scales as scales
import common.util as util

import os
import glob
import argparse

def getOptionValue(options, key, default) :
	if key not in options :
		return default
	if options[key] is None :
		return default
	return options[key]

class Application :
	def __init__(self) :
		self._dataPath = './'
		self._outputPath = './'
		self._tempo = None
		self._instrument = None
		self._noteCount = None

	def run(self) :
		self._parseCommandLine(sys.argv[1:])
		dataFileList = self._loadDataFiles()
		for dataFile in dataFileList :
			self._convertDataFile(dataFile)

	def _parseCommandLine(self, commandLineArguments) :
		parser = argparse.ArgumentParser(add_help = False)
		parser.add_argument(
			'--data-path',
			type = str,
			help = ''
		)
		parser.add_argument(
			'--output-path',
			type = str,
			help = ''
		)
		parser.add_argument(
			'--note-count',
			type = int,
			help = ''
		)
		parser.add_argument(
			'--instrument',
			type = int,
			help = ''
		)
		parser.add_argument(
			'--tempo',
			type = int,
			help = ''
		)
		options = parser.parse_args(commandLineArguments)
		options = vars(options)
		self._dataPath = getOptionValue(options, 'data_path', self._dataPath)
		self._outputPath = getOptionValue(options, 'output_path', self._outputPath)
		self._tempo = getOptionValue(options, 'tempo', self._tempo)
		self._instrument = getOptionValue(options, 'instrument', self._instrument)
		self._noteCount = getOptionValue(options, 'note_count', self._noteCount)

	def _loadDataFiles(self) :
		files = glob.glob(os.path.join(self._dataPath, '*.txt'))
		return files

	def _convertDataFile(self, dataFile) :
		converter = self._detectDataFileConverter(dataFile)
		if converter is None :
			print("Can't detect converter for %s" % (dataFile))
			return
		scaleNameList = scales.scaleNameMap.keys()
		for scaleName in scaleNameList :
			self._convertDataFileWithConverter(dataFile, converter, scaleName)

	def _convertDataFileWithConverter(self, dataFile, converter, scaleName) :
		outputFileName = self._makeOutputFileName(dataFile, converter, scaleName)
		command = 'python datomu.py'
		command += ' --converter %s' % (converter)
		command += ' --scale %s' % (scaleName)
		command += ' --outputer midi'
		command += ' --data-file "%s"' % (os.path.abspath(dataFile))
		command += ' --output-file "%s"' % (outputFileName)
		octaveChange = 0
		if converter == letterconverter.LetterConverter.getNameList() or converter == unicodeconverter.UnicodeConverter.getNameList() :
			if len(scales.scaleNameMap[scaleName][0]) >= 3 :
				octaveChange = -1
		if octaveChange != 0 :
			command += ' --octave-change %s' % (str(octaveChange))
		if self._tempo is not None :
			command += ' --tempo %s' % (str(self._tempo))
		if self._instrument is not None :
			command += ' --instrument %s' % (str(self._instrument))
		if self._noteCount is not None :
			command += ' --note-count %s' % (str(self._noteCount))
		fullCommand = 'cd .. && %s' % (command)
		print(fullCommand)
		os.system(fullCommand)

	def _makeOutputFileName(self, dataFile, converter, scaleName) :
		fileName = os.path.basename(dataFile)
		fileName = util.replaceFileExtension(fileName, '')
		fileName += '-' + converter
		fileName += '-' + scaleName
		if self._tempo is not None :
			fileName += '-%sbpm' % (str(self._tempo))
		if self._instrument is not None :
			fileName += '-instrument%s' % (str(self._instrument))
		if self._noteCount is not None :
			fileName += '-%snotes' % (str(self._noteCount))
		fileName += '.mid'
		fileName = os.path.join(self._outputPath, fileName)
		return fileName

	def _detectDataFileConverter(self, dataFile) :
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
			return digitconverter.DigitConverter.getNameList()
		if letterCount >= digitCount and letterCount >= unicodeCount :
			return letterconverter.LetterConverter.getNameList()
		if unicodeCount >= digitCount and unicodeCount >= letterCount :
			return unicodeconverter.UnicodeConverter.getNameList()
		return None


Application().run()
