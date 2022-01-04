import app.outputer as outputer
import music.constants as constants

from midiutil.MidiFile import MIDIFile

class MidiOutputer(outputer.Outputer) :
	commandArguments = {
		'arguments' : [
			{
				'name' : '--file',
				'type' : str,
				'required' : True,
				'help' : 'The file name to save to.'
			}
		]
	}

	@classmethod
	def getName(cls) :
		return 'midi'

	def __init__(self) :
		super().__init__()

	def doOutput(self, convertedResult) :
		trackCount = 1
		noteGroupList = convertedResult.getNoteGroupList()
		for noteGroup in noteGroupList :
			trackCount = max(trackCount, len(noteGroup.getNoteList()))

		ticksPerQuarternote = 960
		midiFile = MIDIFile(trackCount, ticks_per_quarternote = ticksPerQuarternote, eventtime_is_ticks = True)

		time = 0
		for track in range(trackCount) :
			midiFile.addTrackName(track, time, "Track%d" % (track))
			midiFile.addTempo(track, time, 120)

		channel = 0

		time = 0
		for noteGroup in noteGroupList :
			maxDuration = 0
			noteList = noteGroup.getNoteList()
			for track in range(len(noteList)) :
				note = noteList[track]
				pitch = note.getSemitones()
				duration = int((note.getDuration() * ticksPerQuarternote) // constants.duration4th)
				volume = int((note.getVolume() * 127) // constants.fullVolume)
				midiFile.addNote(track, channel, pitch, time, duration, volume)
				maxDuration = max(maxDuration, duration)
				#print(track, note.getSpnName(), duration)
			time += maxDuration

		with open("output.mid", 'wb') as outf:
			midiFile.writeFile(outf)

