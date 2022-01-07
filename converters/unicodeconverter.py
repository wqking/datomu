import app.converter as converter
import converters.converterutil as converterutil
import common.util as util

class UnicodeConverter(converter.Converter) :
	commandArguments = {
		'arguments' : [
			{
				'name' : '--octave-range',
				'type' : int,
				'help' : ''
			},
		]
	}

	@classmethod
	def getNameList(cls) :
		return 'unicode'

	def __init__(self) :
		super().__init__()
		self._scale = None
		self._durationExtendLetters = ' ,.!?;:'
		self._ignoredLetters = '\r\n'
		self._octaveRange = 3

	def doParsedArguments(self, argumentMap) :
		octaveRange = util.getDictValue(argumentMap, 'octave_range')
		if octaveRange is not None :
			self._octaveRange = octaveRange 
		if self._octaveRange < 1 :
			raise Exception('octave-range must be greater than 0')

	def doConvert(self, result) :
		self._scale = converterutil.scalesToNoteGroupList(self.getScale())
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self.getData(),
			scale = self._scale,
			config = {
				'noteLetters' : self._findCharIndex,
				'durationExtendLetters' : self._durationExtendLetters,
				'noteCount' : self.getNoteCount(),
				'octaveChange' : self.getOctaveChange(),
			}
		)

	def _findCharIndex(self, char) :
		if char in self._durationExtendLetters :
			return -1
		if char in self._ignoredLetters :
			return -1
		index = ord(char)
		noteGroupCount = len(self._scale)
		index = index % (self._octaveRange * noteGroupCount)
		return index