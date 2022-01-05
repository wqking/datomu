import app.action as action
import app.convertedresult as convertedresult
import common.util as util

class Converter(action.Action) :
	@classmethod
	def doSetupArgumentParser(cls, parser) :
		parser.add_argument(
			'--text',
			type = str,
			help = ''
		)
		parser.add_argument(
			'--text-file',
			type = str,
			help = ''
		)
		parser.add_argument(
			'--note-count',
			type = int,
			help = ''
		)

	def __init__(self) :
		super().__init__()
		self._text = None
		self._noteCount = 0

	def parsedArguments(self, argumentMap) :
		self.doParsedArguments(argumentMap)
		text = util.getDictValue(argumentMap, 'text')
		if text is not None :
			self._text = text
		textFile = util.getDictValue(argumentMap, 'text_file')
		if textFile is not None :
			self._text = util.readTextFile(textFile)
		if self._text is None :
			raise Exception("Either --text or --text-file should be specified.")
		noteCount = util.getDictValue(argumentMap, 'note_count')
		if noteCount is not None :
			self._noteCount = noteCount

	def convert(self) :
		result = convertedresult.ConvertedResult()
		self.doConvert(result)
		return result

	def getText(self) :
		return self._text

	def getNoteCount(self) :
		return self._noteCount

	def doConvert(self) :
		raise NotImplementedError

