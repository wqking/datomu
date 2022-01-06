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
	'c3, e3, g3, b4',
	'd3, f3, a3, c4',
	'e3, g3, b3, d4',
	'f3, a3, c4, e4',
	'g3, b3, d4, f4',
	'a3, c4, e4, g4',
	'b3, d4, f4, a4',
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
	'c3, eb3, g3, bb4',
	'd3, f3, ab3, c4',
	'eb3, g3, bb3, d4',
	'f3, ab3, c4, eb4',
	'g3, bb3, d4, f4',
	'ab3, c4, eb4, g4',
	'bb3, d4, f4, ab4',
]

# Chinese Pentatonic scale
pentatonic = [
	'c4',
	'd4',
	'e4',
	'g4',
	'a4',
]

# https://www.musicnotes.com/now/omg/japanese-scales-in-music-theory/
# Japanese Hirajōshi Scale
japanHira = [
	'c4',
	'd4',
	'eb4',
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

	'jp-hira' : japanHira,
}

