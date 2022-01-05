import app.outputer as outputer
import music.constants as constants
import common.util as util

from midiutil.MidiFile import MIDIFile

class MidiOutputer(outputer.Outputer) :
	commandArguments = {
		'arguments' : [
			{
				'name' : '--file',
				'type' : str,
				'help' : 'The file name to save to.'
			},

			# https://soundprogramming.net/file-formats/general-midi-instrument-list/
			{
				'name' : '--instrument',
				'type' : int,
				'help' : 'The instrument number of 1 to 128. '
			},
		]
	}

	@classmethod
	def getNameList(cls) :
		return 'midi'

	def __init__(self) :
		super().__init__()
		self._file = 'output.mid'
		self._instrument = 1

	def doParsedArguments(self, argumentMap) :
		file = util.getDictValue(argumentMap, 'file')
		if file is not None :
			self._file = file 
		instrument = util.getDictValue(argumentMap, 'instrument')
		if instrument is not None :
			self._instrument = instrument 
		if self._instrument < 1 or self._instrument > 128 :
			raise Exception('Instrument must be between 1 and 128')

	def doOutput(self, convertedResult) :
		trackCount = 1
		noteGroupList = convertedResult.getNoteGroupList()
		for noteGroup in noteGroupList :
			trackCount = max(trackCount, len(noteGroup.getNoteList()))

		ticksPerQuarternote = 960
		midiFile = MIDIFile(trackCount, ticks_per_quarternote = ticksPerQuarternote, eventtime_is_ticks = True)

		channel = 0

		time = 0
		for track in range(trackCount) :
			midiFile.addTrackName(track, time, "Track%d" % (track))
			midiFile.addTempo(track, time, self.getTempo())
			midiFile.addProgramChange(track, channel, time, self._instrument - 1)

		time = 0
		for noteGroup in noteGroupList :
			maxDuration = 0
			noteList = noteGroup.getNoteList()
			for track in range(len(noteList)) :
				note = noteList[track]
				pitch = note.getSemitones()
				duration = int((note.getDuration() * ticksPerQuarternote) // constants.duration4th)
				volume = int((note.getVolume() * 127) // constants.fullVolume)
				if note.isRest() :
					volume = 0
				midiFile.addNote(track, channel, pitch, time, duration, volume)
				maxDuration = max(maxDuration, duration)
				#print(track, note.getSpnName(), duration)
			time += maxDuration

		with open(self._file, 'wb') as outf:
			midiFile.writeFile(outf)

