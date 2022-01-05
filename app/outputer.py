import app.action as action
import common.util as util

class Outputer(action.Action) :
	@classmethod
	def doSetupArgumentParser(cls, parser) :
		parser.add_argument(
			'--tempo',
			type = int,
			help = ''
		)

	def __init__(self) :
		super().__init__()
		self._tempo = 120

	def getTempo(self) :
		return self._tempo

	def parsedArguments(self, argumentMap) :
		self.doParsedArguments(argumentMap)
		tempo = util.getDictValue(argumentMap, 'tempo')
		if tempo is not None :
			self._tempo = int(tempo)
		if self._tempo <= 0 :
			raise Exception('Tempo must be greater than 0')
		if self._tempo >= 1000 :
			raise Exception('Tempo must be less than 1000')

	def output(self, convertedResult) :
		self.doOutput(convertedResult)

	def doOutput(self, convertedResult) :
		raise NotImplementedError

