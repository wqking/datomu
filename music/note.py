import music.constants as constants
import common.util as util

import re

class Note :
	def __init__(self) :
		self._reset()
		self._isRest = False
		self._duration = constants.duration4th
		self._volume = constants.fullVolume

	def _reset(self) :
		self._degree = 0
		self._octave = 0
		self._accidental = constants.AccidentalType.none

	def isRest(self) :
		return self._isRest

	def getDuration(self) :
		return self._duration

	def setDuration(self, duration) :
		self._duration = duration

	def getVolume(self) :
		return self._volume

	def setVolume(self, volume) :
		volume = int(volume)
		assert(volume >= 0 and volume <= constants.fullVolume)
		self._volume = volume

	def getDegree(self) :
		return self._degree

	def getOctave(self) :
		return self._octave

	def setOctave(self, octave) :
		self._octave = octave
		if self._octave < 0 :
			self._octave = 0

	def increaseOctave(self, delta = 1) :
		self.setOctave(self.getOctave() + delta)

	def getAccidental(self) :
		return self._accidental

	# C0 semitons is 0, C4 is 48
	def getSemitones(self) :
		semitones = constants.semitoneListInOneOctave[self._degree]
		semitones += constants.accidentalSemitoneList[int(self._accidental)]
		semitones += self._octave * constants.semitoneCountPerOctave
		return semitones

	def getName(self) :
		return constants.noteNameList[self._degree]

	# SPN -- Scientific pitch notation
	def getSpnName(self, includeOctave = True) :
		result = self.getName().upper()
		result += constants.accidentalSymbolList[int(self._accidental)]
		if includeOctave :
			result += str(self._octave)
		return result

	def clone(self) :
		other = Note()
		other._degree = self._degree
		other._octave = self._octave
		other._accidental = self._accidental
		other._duration = self._duration
		other._volume = self._volume
		return other

	def fromRest(self) :
		self._isRest = True
		return self

	def fromSemitones(self, semitones, accidentalType = constants.AccidentalType.sharp) :
		self._reset()
		octave, remainder = divmod(semitones, constants.semitoneCountPerOctave)
		self._octave = octave
		for i in range(0, len(constants.semitoneListInOneOctave)) :
			if remainder <= constants.semitoneListInOneOctave[i] :
				if remainder == constants.semitoneListInOneOctave[i] :
					self._degree = i
				else :
					if accidentalType == constants.AccidentalType.sharp :
						self._accidental = constants.AccidentalType.sharp
						self._degree = i - 1
					else :
						self._accidental = constants.AccidentalType.flat
						self._degree = i
				break
		return self

	def fromSpnNoteName(self, nameText) :
		if nameText == 'rest' :
			self._isRest = True
			return self
		return self._doFromSpnNoteName(nameText, self._doMatchNoteName(nameText))

	def fromText(self, text, accidentalType = constants.AccidentalType.sharp) :
		if text == 'rest' :
			self._isRest = True
			return self
		if re.match(r"^\d+$", text) is not None :
			return self.fromSemitones(int(text), accidentalType)
		match = self._doMatchNoteName(text)
		if match is not None :
			return self._doFromSpnNoteName(text, match)
		raise ValueError('Invalid note name: %s' % (text))

	def _doFromSpnNoteName(self, nameText, match) :
		self._reset()
		if match is None :
			raise ValueError('Invalid note name: %s' % (nameText))
		name = match.group(1).lower()
		octave = int(match.group(3))
		accidental = constants.AccidentalType.none
		accidentalText = match.group(2)
		if accidentalText is not None :
			accidentalText = accidentalText.lower()
			index = util.findItemInList(constants.accidentalSymbolList, accidentalText)
			if index >= 0 :
				accidental = constants.AccidentalType(index)
			elif accidentalText == '##' :
				accidental = constants.AccidentalType.doubleSharp
		self._degree = util.findItemInList(constants.noteNameList, name)
		self._octave = octave
		self._accidental = accidental
		return self

	def _doMatchNoteName(self, nameText) :
		return re.match(r'^([a-g])(=|#|x|##|b|bb)?([0-9])$', nameText, re.IGNORECASE)

