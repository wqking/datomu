import app.action as action
import app.convertedresult as convertedresult
import converters.scales as scales
import common.util as util

class Converter(action.Action) :
	@classmethod
	def doSetupArgumentParser(cls, parser) :
		parser.add_argument(
			'--data',
			type = str,
			help = "Specifies the data on the command line, for example, --data 3.14159265"
		)
		parser.add_argument(
			'--data-file',
			type = str,
			help = "Loads the data from the data file."
		)
		parser.add_argument(
			'--note-count',
			type = int,
			help = "Specifies how many notes will be converted and generated. The default value is 0, that means no limits, all notes will be converted."
		)
		parser.add_argument(
			'--scale',
			type = str,
			help = "Specify the scale used by the --converter. The default scale is 'cmaj'."
		)
		parser.add_argument(
			'--octave-change',
			type = int,
			help = "Change octave higher or lower. The value is an integer. Negative integer decreases the octave. Positive integer increases the octave. The default value is 0, which doesn't change the octave."
		)
		parser.add_argument(
			'--volume',
			type = int,
			help = "Specifies the volume in the output sound file. The default value is 80. The value is between 0 and 100. 100 is the highest volume, 0 is silent."
		)

	def __init__(self) :
		super().__init__()
		self._data = None
		self._noteCount = 0
		self._scaleName = "cmaj"
		self._octaveChange = 0
		self._volume = 80

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
		scaleName = util.getDictValue(argumentMap, 'scale')
		if scaleName is not None :
			self._scaleName = scaleName
		octaveChange = util.getDictValue(argumentMap, 'octave_change')
		if octaveChange is not None :
			self._octaveChange = octaveChange
		volume = util.getDictValue(argumentMap, 'volume')
		if volume is not None :
			self._volume = volume
			if self._volume < 0 or self._volume > 127 :
				raise Exception("--volume must be between [0, 127]")

	def convert(self) :
		result = convertedresult.ConvertedResult()
		self.doConvert(result)
		return result

	def getData(self) :
		return self._data

	def getNoteCount(self) :
		return self._noteCount

	def getScaleName(self) :
		return self._scaleName

	def getScale(self) :
		if self._scaleName not in scales.scaleNameMap :
			raise Exception("Unknown scale name %s" % (self._scaleName))
		return scales.scaleNameMap[self._scaleName]

	def getOctaveChange(self) :
		return self._octaveChange

	def getVolume(self) :
		return self._volume

	def doConvert(self) :
		raise NotImplementedError

