# Datomu -- convert Data To Music

Datomu is a little tool to convert any boring data to enjoyable music. For example, we can convert the mathematics constant π (Pi, 3.14159265 ......) to music, each digit is a note or chord, or convert Percy Bysshe Shelley's poem to music, letter by letter.  
Datomu doesn't handle any musicality, it only converts the data accurately. So any musicality, if any, is produced by the data, or to say, produced by the wonderful nature.

Currently Datomu can generate MIDI file. For example, the tool can convert 3.14159265 to C Major scale "E4 C4 F4 G4 B5 D4 A4 G4" note sequence and store to MIDI file. 

This tool is written in Python 3

## License

Apache License, Version 2.0  

If you use this tool to produce any great music, if you give credit to the tool author wqking (Wang Qi), you are appreciated.

## Dependencies

`pip install midiutil`

## User document

To use the tool, get the source from github https://github.com/wqking/datomu  
Install the dependencies in previous section.  
Then go to the source code folder in terminal (command line console). Then run command,  
`python datomu.py OPTIONS`  

### The options

**--help**  
Display help message.

**--data**  
**--data-file filename**
--data specifies the data on the command line, for example, --data 3.14159265  
--data-file loads the data from `filename`. Since most data is long, --data-file is more useful than --data.  
There are pre-defined data in the `data` folder. You can use any data.  

**--converter**  
Specify the converter. The default converter is 'digit'.  
Availabe converters:  
`digit`: convert digit 1-9 to the notes in the scale degrees. 0 doubles the duration of the previous note.  
`letter`: convert letter a-z to the notes in the scale degrees. space, dot, comma, and '!?;:' doubles the duration of the previous note.  
`unicode`: map the unicode values to the notes in the scale degrees. space, dot, comma, and '!?;:' doubles the duration of the previous note. It's useful for non-English and non-Latin languages.

**--scale**  
Specify the scale used by the --converter. The default scale is 'cmaj'.  
Available scales:  
`cmaj`: C Major scale. C, D, E, F, G, A, B.  
`cmaj-chord`: Chords in C Major. C, Dm, Em, F, G, Am, Bdim  
`cmaj7-chord`: Chords in C Major 7. Cmaj7, Dm7, Em7, F7, G7, Am7, Bdim7  
`cmin`: C Minor scale. C, D, Eb, F, G, Ab, Bb  
`cmin-chord`: Chords in C Minor. Cm, Ddim, Eb, Fm, Gm, Ab, Bb  
`cmin7-chord`: Chords in C Minor 7. Cm7, Ddim7, Eb7, Fm7, Gm7, Ab7, Bb7  
`cn-penta`: Chinese pentatonic scale   
`jp-in`: Japanese In Scale  

**--outputer**  
Specifies the outputer, how the converted notes are outputted. The default value is 'midi'.  
Currently there is only one outputer, 'midi'. It will write the notes to MIDI file.  

**--output-file**    
Specifies the MIDI file name to write to. The default value is 'output.mid'.   

**--instrument**  
Specifies the instrument used in the MIDI file. The default value is 1, which is Acoustic Grand Piano.  
The value is 1-128, see https://soundprogramming.net/file-formats/general-midi-instrument-list/ for details.

**--tempo**  
Specifies the tempo in BPM for quarter note. The default value is 120.  

**--volume**  
Specifies the volume in the output sound file. The default value is 80. The value is between 0 and 100. 100 is the highest volume, 0 is silent.  

**--note-count**  
Specifies how many notes will be converted and generated. The default value is 0, that means no limits, all notes will be converted.  

**--octave-change**  
Change octave higher or lower. The value is an integer. Negative integer decreases the octave. Positive integer increases the octave.  
The default value is 0, which doesn't change the octave.
For example, '--octave-change -2' will decrease 2 octaves on each notes.

**--octave-range**  
Used by 'unicode' converter. Specifies the range of the octaves to convert to. The default value is 3, that means, the converted note pitches are within 3 octaves.

### More explanation on coverter and scale

A 'scale' is a sequence of notes or chords. For example, 'cmaj' scales contains 7 notes, C4, D4, E4, F4, G4, A4, B4.  
A converter maps the data to scales.  
'digit' converter converts the digit 1-7 to C4-B4, 8 and 9 to C5 and D5. Each note has default duration of quarter note. The digit 0 doubles previous note's duration, the max duration is limited to whole note.  
'letter' converter converts the letters a-z. The first 7 letters a-g (case insensitive, A is same as a) are converted to C4-B4. The second 7 letters h-n are converted to one octave higher, C5-B5, the third 7 letters are converted to C6-B6, etc. The space and some symbols ' ,.!?;:' double previous note's duration.  
'unicode' converter converts each unicode value to a note, and limits the pitch to certain octaves.  
Note only current three converters (digit, letter, unicode) depends on the '--scale' option, it's possible to creat converters that don't need any scale.

The converters and scales are not limited to the ones in current code. It's very easy to add new converters and scales. When you add new stuff, I suggest you to use simplest algorithm as much as possible. Too much artificial algorithm or human intervention will distort the raw data. We want to listen the music from the raw data. Nature is the most beautiful.  

### Example commands

`python datomu.py --converter digit --scale cmaj-chord --outputer midi --data-file mydata.txt --output-file myoutput.mid --tempo 120 --instrument 41 --note-count 100`  

## Developer document

Currently there is no document for developer. You are welcome to read the source code and contribute your code, especially new converters and new outputers.  
Warning: the code style doesn't conform to PEP8 or any Python style, and the indent uses tabs, not spaces. If you want to contribute, please follow current code style.  

## Motivations

I (wqking) love programming, I love music, I love the beauty of nature. Datomu puts all my love together, nothing else is more exciting.  
