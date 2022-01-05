import app.converter as converter
import music.constants as constants
from music.note import Note
from music.notegroup import NoteGroup
import music.noteutil as noteutil
import music.scales as scales

nameScaleMap = {
	'cmaj' : scales.cMajorScale,
	'cmaj-chord' : scales.cMajorChord,
	'cmaj7-chord' : scales.cMajor7Chord,
}

noteLetters = '123456789'

class SimpleConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return nameScaleMap.keys()

	def __init__(self) :
		super().__init__()

	def doConvert(self, result) :
		text = self.getText()
		scale = nameScaleMap[self.getName()]
		scale = scales.scalesToNoteGroupList(scale)
		noteCount = self.getNoteCount()
		for char in text :
			index = noteLetters.find(char)
			if index >= 0 :
				octave, remainder = divmod(index, len(scale))
				noteGroup = scale[remainder].clone()
				noteGroup.increaseOctave(octave)
				noteGroup.setVolume(constants.fullVolume / 2)
				noteGroup.getNoteList()[-1].setVolume(constants.fullVolume)
				result.addNoteGroup(noteGroup)
			elif char == '0' :
				noteGroupList = result.getNoteGroupList()
				if len(noteGroupList) > 0 :
					noteList = noteGroupList[-1].getNoteList()
					for note in noteList :
						duration = note.getDuration()
						duration *= 2
						if duration <= constants.durationWhole :
							note.setDuration(duration)
			if noteCount > 0 and len(result.getNoteGroupList()) >= noteCount :
				break