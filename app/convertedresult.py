class ConvertedResult :
	def __init__(self) :
		self._noteGroupList = []

	def getNoteGroupList(self) :
		return self._noteGroupList

	def addNoteGroup(self, noteGroup) :
		self._noteGroupList.append(noteGroup)
