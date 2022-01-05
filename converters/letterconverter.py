import app.converter as converter
import music.scales as scales
import converters.converterutil as converterutil

import re

nameScaleMap = {
	'letter-cmaj' : scales.cMajorScale,
	'letter-cmaj-chord' : scales.cMajorChord,
	'letter-cmaj7-chord' : scales.cMajor7Chord,
	'letter-cmin' : scales.cMinorScale,
	'letter-cmin-chord' : scales.cMinorChord,
	'letter-cmin7-chord' : scales.cMinor7Chord,
}

class LetterConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return nameScaleMap.keys()

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self.getText(),
			scale = nameScaleMap[self.getName()],
			config = {
				'noteLetters' : 'abcdefghijklmnopqrstuvwxyz',
				'durationExtendLetters' : ' .',
				'noteCount' : self.getNoteCount(),
				'octaveChange' : -1,
			}
		)

	def _normalizeText(self, text) :
		text = text.lower()
		text = re.sub(r'\s+', ' ', text)
		return text