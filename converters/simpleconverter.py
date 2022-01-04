import app.converter as converter
import music.constants as constants
from music.note import Note
from music.notegroup import NoteGroup
import music.noteutil as noteutil

noteMap = {
	'0' : 'rest',
	'1' : 'c4',
	'2' : 'd4',
	'3' : 'e4',
	'4' : 'f4',
	'5' : 'g4',
	'6' : 'a4',
	'7' : 'b4',
	'8' : 'c5',
	'9' : 'd5',
}

XXXcMajorScale = [
	NoteGroup(noteutil.noteListFromSpnNoteNames('c4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('d4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('e4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('f4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('g4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('a4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('b4')),
]

XXXcMajorScale = [
	NoteGroup(noteutil.noteListFromSpnNoteNames('c4, e4, g4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('d4, f4, a4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('e4, g4, b4')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('f4, a4, c5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('g4, b4, d5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('a4, c5, e5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('b4, d5, f5')),
]

cMajorScale = [
	NoteGroup(noteutil.noteListFromSpnNoteNames('c4, e4, g4, b5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('d4, f4, a4, c5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('e4, g4, b4, d5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('f4, a4, c5, e5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('g4, b4, d5, f5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('a4, c5, e5, g5')),
	NoteGroup(noteutil.noteListFromSpnNoteNames('b4, d5, f5, a5')),
]

noteLetters = '123456789'

class SimpleConverter(converter.Converter) :
	@classmethod
	def getName(cls) :
		return 'simple'

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		text = self.getText()
		for char in text :
			index = noteLetters.find(char)
			if index >= 0 :
				octave, remainder = divmod(index, len(cMajorScale))
				noteGroup = cMajorScale[remainder].clone()
				noteGroup.increaseOctave(octave)
				noteGroup.setVolume(constants.fullVolume / 2)
				noteGroup.getNoteList()[-1].setVolume(constants.fullVolume)
				result.addNoteGroup(noteGroup)
