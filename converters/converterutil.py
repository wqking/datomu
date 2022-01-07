import music.constants as constants
from music.note import Note
from music.notegroup import NoteGroup
import music.noteutil as noteutil
import common.util as util

def findLetterIndex(char, letterList) :
	if callable(letterList) :
		return letterList(char)
	return letterList.find(char)

def scalesToNoteGroupList(scaleList) :
	noteGroupList = []
	for scale in scaleList :
		noteGroup = scale
		if util.isString(noteGroup) :
			noteGroup = NoteGroup(noteutil.noteListFromSpnNoteNames(noteGroup))
		noteGroupList.append(noteGroup)
	return noteGroupList

def convertSingleLettersToScale(result, text, scale, config) :
	scale = scalesToNoteGroupList(scale)
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
			noteGroup.setVolume(constants.fullVolume * 4 / 5)
			noteGroup.getNoteList()[-1].setVolume(constants.fullVolume)
			if octaveChange != 0 :
				noteGroup.increaseOctave(octaveChange)
			#print(noteGroup.getNoteList()[0].getSpnName(), noteGroup.getNoteList()[0].getSemitones())
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
