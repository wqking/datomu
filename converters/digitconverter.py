import app.converter as converter
import music.scales as scales
import converters.converterutil as converterutil

nameScaleMap = {
	'digit-cmaj' : scales.cMajorScale,
	'digit-cmaj-chord' : scales.cMajorChord,
	'digit-cmaj7-chord' : scales.cMajor7Chord,
	'digit-cmin' : scales.cMinorScale,
	'digit-cmin-chord' : scales.cMinorChord,
	'digit-cmin7-chord' : scales.cMinor7Chord,
}

class DigitConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return nameScaleMap.keys()

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self.getData(),
			scale = nameScaleMap[self.getName()],
			config = {
				'noteLetters' : '123456789',
				'durationExtendLetters' : '0',
				'noteCount' : self.getNoteCount(),
			}
		)
