import app.converter as converter
import converters.converterutil as converterutil

import re

class LetterConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return 'letter'

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self._normalizeText(self.getData()),
			scale = self.getScale(),
			config = {
				'noteLetters' : 'abcdefghijklmnopqrstuvwxyz',
				'durationExtendLetters' : ' ,.!?;:',
				'noteCount' : self.getNoteCount(),
				'volume' : self.getVolume(),
				'octaveChange' : self.getOctaveChange(),
			}
		)

	def _normalizeText(self, text) :
		text = text.lower()
		text = re.sub(r'\s+', ' ', text)
		return text