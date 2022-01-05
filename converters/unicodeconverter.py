import app.converter as converter
import music.scales as scales
import converters.converterutil as converterutil

import re

nameScaleMap = {
	'unicode-cmaj' : scales.cMajorScale,
	'unicode-cmaj-chord' : scales.cMajorChord,
	'unicode-cmaj7-chord' : scales.cMajor7Chord,
	'unicode-cmin' : scales.cMinorScale,
	'unicode-cmin-chord' : scales.cMinorChord,
	'unicode-cmin7-chord' : scales.cMinor7Chord,
}

class UnicodeConverter(converter.Converter) :
	@classmethod
	def getNameList(cls) :
		return nameScaleMap.keys()

	def __init__(self) :
		super().__init__()
		self._scale = None
		self._durationExtendLetters = ' ,.，。'
		self._ignoredLetters = '\r\n'

	def doConvert(self, result) :
		self._scale = scales.scalesToNoteGroupList(nameScaleMap[self.getName()])
		converterutil.convertSingleLettersToScale(
			result = result,
			text = self.getText(),
			scale = self._scale,
			config = {
				'noteLetters' : self._findCharIndex,
				'durationExtendLetters' : self._durationExtendLetters,
				'noteCount' : self.getNoteCount(),
				'octaveChange' : -1,
			}
		)

	def _findCharIndex(self, char) :
		if char in self._durationExtendLetters :
			return -1
		if char in self._ignoredLetters :
			return -1
		index = ord(char)
		noteGroupCount = len(self._scale)
		maxOctave = 4
		if index > maxOctave * noteGroupCount :
			index = maxOctave * noteGroupCount + index % noteGroupCount
		return index