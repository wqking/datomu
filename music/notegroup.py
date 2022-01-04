class NoteGroup :
	def __init__(self, noteList) :
		self._noteList = noteList

	def clone(self) :
		other = NoteGroup([])
		for note in self._noteList :
			other._noteList.append(note.clone())
		return other

	def getNoteList(self) :
		return self._noteList

	def increaseOctave(self, delta) :
		for note in self._noteList :
			note.increaseOctave(delta)

	def setVolume(self, volume) :
		for note in self._noteList :
			note.setVolume(volume)

