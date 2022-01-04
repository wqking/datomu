import common.util as util

class Action :
	def __init__(self) :
		pass

	@classmethod
	def setupArgumentParser(cls, parser) :
		commandArguments = cls._tryGetCommandArguments()
		argumentList = util.getDictValue(commandArguments, 'arguments')
		if argumentList is None :
			return
		for argument in argumentList :
			parser.add_argument(
				argument['name'],
				type = argument['type'],
				help = argument['help'],
				required = util.getDictValue(argument, 'required')
			)

	@classmethod
	def _tryGetCommandArguments(cls) :
		if hasattr(cls, 'commandArguments') :
			return getattr(cls, 'commandArguments')
		raise NotImplementedError

