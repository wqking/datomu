import app.converter as converter
import converters.converterutil as converterutil

class DigitConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return 'digit'

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self.getData(),
			scale = self.getScale(),
			config = {
				'noteLetters' : '123456789',
				'durationExtendLetters' : '0',
				'noteCount' : self.getNoteCount(),
				'octaveChange' : self.getOctaveChange(),
			}
		)
