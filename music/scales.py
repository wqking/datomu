from music.notegroup import NoteGroup
import music.noteutil as noteutil
import common.util as util

cMajorScale = [
	'c4',
	'd4',
	'e4',
	'f4',
	'g4',
	'a4',
	'b4',
]

cMajorChord = [
	'c4, e4, g4',
	'd4, f4, a4',
	'e4, g4, b4',
	'f4, a4, c5',
	'g4, b4, d5',
	'a4, c5, e5',
	'b4, d5, f5',
]

cMajor7Chord = [
	'c3, e3, g3, b4',
	'd3, f3, a3, c4',
	'e3, g3, b3, d4',
	'f3, a3, c4, e4',
	'g3, b3, d4, f4',
	'a3, c4, e4, g4',
	'b3, d4, f4, a4',
]

def scalesToNoteGroupList(scaleList) :
	noteGroupList = []
	for scale in scaleList :
		noteGroup = scale
		if util.isString(noteGroup) :
			noteGroup = NoteGroup(noteutil.noteListFromSpnNoteNames(noteGroup))
		noteGroupList.append(noteGroup)
	return noteGroupList
