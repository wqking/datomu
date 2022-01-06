import app.converter as converter
import converters.converterutil as converterutil

class UnicodeConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return 'unicode'

	def __init__(self) :
		super().__init__()
		self._scale = None
		self._durationExtendLetters = ' ,.!?;:'
		self._ignoredLetters = '\r\n'

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
				'octaveChange' : -1,
			}
		)

	def _findCharIndex(self, char) :
		if char in self._durationExtendLetters :
			return -1
		if char in self._ignoredLetters :
			return -1
		index = ord(char)
		noteGroupCount = len(self._scale)
		maxOctave = 3
		index = index % (maxOctave * noteGroupCount)
		return index