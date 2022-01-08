import music.note as note
import music.noteutil as noteutil

cMajorScale = [
	'c4',
	'd4',
	'e4',
	'f4',
	'g4',
	'a4',
	'b4',
]

# https://www.piano-keyboard-guide.com/key-of-c.html
# C, Dm, Em, F, G, Am, Bdim
cMajorChord = [
	'c4, e4, g4',
	'd4, f4, a4',
	'e4, g4, b4',
	'f4, a4, c5',
	'g4, b4, d5',
	'a4, c5, e5',
	'b4, d5, f5',
]

# https://www.piano-keyboard-guide.com/key-of-c.html
# Cmaj7, Dm7, Em7, F7, G7, Am7, Bdim7
cMajor7Chord = [
	'c4, e4, g4, b4',
	'd4, f4, a4, c5',
	'e4, g4, b4, d5',
	'f4, a4, c5, e5',
	'g4, b4, d5, f5',
	'a4, c5, e5, g5',
	'b4, d5, f5, a5',
]

cMinorScale = [
	'c4',
	'd4',
	'eb4',
	'f4',
	'g4',
	'ab4',
	'bb4',
]

# http://www.piano-keyboard-guide.com/key-of-c-minor.html
# Cm, Ddim, Eb, Fm, Gm, Ab, Bb
cMinorChord = [
	'c4, eb4, g4',
	'd4, f4, ab4',
	'eb4, g4, bb4',
	'f4, ab4, c5',
	'g4, bb4, d5',
	'ab4, c5, eb5',
	'bb4, d5, f5',
]

# http://www.piano-keyboard-guide.com/key-of-c-minor.html
# Cm7, Ddim7, Eb7, Fm7, Gm7, Ab7, Bb7
cMinor7Chord = [
	'c4, eb4, g4, bb4',
	'd4, f4, ab4, c5',
	'eb4, g4, bb4, d5',
	'f4, ab4, c5, eb5',
	'g4, bb4, d5, f5',
	'ab4, c5, eb5, g5',
	'bb4, d5, f5, ab5',
]

# Chinese Pentatonic scale
pentatonic = [
	'c4',
	'd4',
	'e4',
	'g4',
	'a4',
]

# https://en.wikipedia.org/wiki/In_scale
# Japanese In Scale
japanIn = [
	'c4',
	'db4',
	'f4',
	'g4',
	'ab4',
]

scaleNameMap = {
	'cmaj' : cMajorScale,
	'cmaj-chord' : cMajorChord,
	'cmaj7-chord' : cMajor7Chord,
	'cmin' : cMinorScale,
	'cmin-chord' : cMinorChord,
	'cmin7-chord' : cMinor7Chord,

	'cn-penta' : pentatonic,

	'jp-in' : japanIn,
}

# for test
def verifyScales() :
	for scaleName in scaleNameMap :
		scaleList = scaleNameMap[scaleName]
		for scale in scaleList :
			noteList = noteutil.noteListFromSpnNoteNames(scale)
			for i in range(1, len(noteList)) :
				previousSemitones = noteList[i - 1].getSemitones()
				currentSemitones = noteList[i].getSemitones()
				if currentSemitones <= previousSemitones :
					raise Exception("verifyScales failed 1: %s %d" % (scaleName, i))
				if currentSemitones - previousSemitones >= 12 :
					raise Exception("verifyScales failed 2: %s %d" % (scaleName, i))

verifyScales()
