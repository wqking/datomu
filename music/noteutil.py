from music.note import Note
import common.util as util

def noteListFromSpnNoteNames(nameList) :
	if util.isString(nameList) :
		nameList = util.splitByCommaOrSpace(nameList)
	noteList = []
	for name in nameList :
		noteList.append(Note().fromSpnNoteName(name))
	return noteList

def noteListToSpnNoteNames(noteList) :
	names = []
	for note in noteList :
		names.append(note.getSpnName())
	return names

