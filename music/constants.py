import enum

semitoneCountPerOctave = 12
degreeCountPerOctave = 7
semitoneListInOneOctave = [ 0, 2, 4, 5, 7, 9, 11 ]
noteNameList = [ 'c', 'd', 'e', 'f', 'g', 'a', 'b' ]

@enum.unique
class AccidentalType(enum.IntEnum) :
	natural = 0
	sharp = 1
	flat = 2
	doubleSharp = 3
	doubleFlat = 4
	none = 5

accidentalSymbolList = [ '=', '#', 'b', 'x', 'bb', '' ]
accidentalSemitoneList = [ 0, 1, -1, 2, -2, 0 ]

durationWhole = 1024
duration2nd = durationWhole / 2
duration4th = durationWhole / 4
duration8th = durationWhole / 8
duration16th = durationWhole / 16
duration32th = durationWhole / 32
duration64th = durationWhole / 64
duration128th = durationWhole / 128

fullVolume = 100
