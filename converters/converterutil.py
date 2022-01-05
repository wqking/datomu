import music.scales as scales
import music.constants as constants
from music.note import Note
from music.notegroup import NoteGroup
import common.util as util

def findLetterIndex(char, letterList) :
	if callable(letterList) :
		return letterList(char)
	return letterList.find(char)

def convertSingleLettersToScale(result, text, scale, config) :
	scale = scales.scalesToNoteGroupList(scale)
	noteLetters = config['noteLetters']
	durationExtendLetters = util.getDictValue(config, 'durationExtendLetters', '')
	restLetters = util.getDictValue(config, 'restLetters', '')
	noteCount = util.getDictValue(config, 'noteCount', 0)
	octaveChange = util.getDictValue(config, 'octaveChange', 0)
	for char in text :
		index = findLetterIndex(char, noteLetters)
		if index >= 0 :
			octave, remainder = divmod(index, len(scale))
			noteGroup = scale[remainder].clone()
			noteGroup.increaseOctave(octave)
			noteGroup.setVolume(constants.fullVolume / 2)
			noteGroup.getNoteList()[-1].setVolume(constants.fullVolume)
			if octaveChange != 0 :
				noteGroup.increaseOctave(octaveChange)
			result.addNoteGroup(noteGroup)
		elif findLetterIndex(char, durationExtendLetters) >= 0 :
			noteGroupList = result.getNoteGroupList()
			if len(noteGroupList) > 0 :
				noteList = noteGroupList[-1].getNoteList()
				for note in noteList :
					duration = note.getDuration()
					duration *= 2
					if duration <= constants.durationWhole :
						note.setDuration(duration)
		elif findLetterIndex(char, restLetters) >= 0 :
			noteGroup = NoteGroup([ Note().fromRest() ])
			result.addNoteGroup(noteGroup)
		if noteCount > 0 and len(result.getNoteGroupList()) >= noteCount :
			break
