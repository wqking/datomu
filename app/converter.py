import app.action as action
import app.convertedresult as convertedresult

class Converter(action.Action) :
	def __init__(self) :
		super().__init__()
		self._text = ''

	def convert(self, text) :
		self._text = text
		result = convertedresult.ConvertedResult()
		self.doConvert(result)
		return result

	def getText(self) :
		return self._text

	def doConvert(self) :
		raise NotImplementedError

