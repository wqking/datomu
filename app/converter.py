import app.action as action
import app.convertedresult as convertedresult
import common.util as util

class Converter(action.Action) :
	@classmethod
	def doSetupArgumentParser(cls, parser) :
		parser.add_argument(
			'--data',
			type = str,
			help = ''
		)
		parser.add_argument(
			'--data-file',
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
		self._data = None
		self._noteCount = 0

	def parsedArguments(self, argumentMap) :
		self.doParsedArguments(argumentMap)
		data = util.getDictValue(argumentMap, 'data')
		if data is not None :
			self._data = data
		dataFile = util.getDictValue(argumentMap, 'data_file')
		if dataFile is not None :
			self._data = util.readTextFile(dataFile)
		if self._data is None :
			raise Exception("Either --data or --data-file should be specified.")
		noteCount = util.getDictValue(argumentMap, 'note_count')
		if noteCount is not None :
			self._noteCount = noteCount

	def convert(self) :
		result = convertedresult.ConvertedResult()
		self.doConvert(result)
		return result

	def getData(self) :
		return self._data

	def getNoteCount(self) :
		return self._noteCount

	def doConvert(self) :
		raise NotImplementedError

