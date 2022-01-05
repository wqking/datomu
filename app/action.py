import common.util as util

class Action :
	def __init__(self) :
		self._name = None

	@classmethod
	def getNameList(cls) :
		raise NotImplementedError

	@classmethod
	def setupArgumentParser(cls, parser) :
		cls.doSetupArgumentParser(parser)

		commandArguments = cls._tryGetCommandArguments()
		if commandArguments is None :
			return
		argumentList = util.getDictValue(commandArguments, 'arguments')
		if argumentList is None :
			return
		for argument in argumentList :
			parser.add_argument(
				argument['name'],
				type = argument['type'],
				help = argument['help'],
				default = util.getDictValue(argument, 'default')
			)

	@classmethod
	def doSetupArgumentParser(cls, parser) :
		pass

	@classmethod
	def _tryGetCommandArguments(cls) :
		if hasattr(cls, 'commandArguments') :
			return getattr(cls, 'commandArguments')
		return None

	def parsedArguments(self, argumentMap) :
		self.doParsedArguments(argumentMap)

	def doParsedArguments(self, argumentMap) :
		pass

	def getName(self) :
		return self._name

	def setName(self, name) :
		self._name = name