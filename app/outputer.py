import app.action as action

class Outputer(action.Action) :
	def __init__(self) :
		super().__init__()

	def setupArgumentParser(self, parser) :
		self.doSetupArgumentParser(parser)

	def doSetupArgumentParser(self, parser) :
		pass

	def output(self, convertedResult) :
		self.doOutput(convertedResult)

	def doOutput(self, convertedResult) :
		raise NotImplementedError

