import converters.letterconverter as letterconverter
import music.constants as constants

def test_digitConverter() :
	converter = letterconverter.LetterConverter()
	converter._data = 'Abc.De, fGHZ'
	converter._scaleName = 'cmaj'
	noteGroupList = converter.convert().getNoteGroupList()
	assert len(noteGroupList) == 9
	for noteGroup in noteGroupList :
		assert len(noteGroup.getNoteList()) == 1
	assert noteGroupList[0].getNoteList()[0].getSpnName() == 'C4'
	assert noteGroupList[0].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[1].getNoteList()[0].getSpnName() == 'D4'
	assert noteGroupList[1].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[2].getNoteList()[0].getSpnName() == 'E4'
	assert noteGroupList[2].getNoteList()[0].getDuration() == constants.duration2nd
	assert noteGroupList[3].getNoteList()[0].getSpnName() == 'F4'
	assert noteGroupList[3].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[4].getNoteList()[0].getSpnName() == 'G4'
	assert noteGroupList[4].getNoteList()[0].getDuration() == constants.durationWhole
	assert noteGroupList[5].getNoteList()[0].getSpnName() == 'A4'
	assert noteGroupList[5].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[6].getNoteList()[0].getSpnName() == 'B4'
	assert noteGroupList[6].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[7].getNoteList()[0].getSpnName() == 'C5'
	assert noteGroupList[7].getNoteList()[0].getDuration() == constants.duration4th
	assert noteGroupList[8].getNoteList()[0].getSpnName() == 'G7'
	assert noteGroupList[8].getNoteList()[0].getDuration() == constants.duration4th
