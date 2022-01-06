# datomu -- convert Data To Music

datomu is a little tool to convert any boring data to enjoyable music. For example, we can convert the mathematics constant π (Pi, 3.14159265 ......) to music, each digit is a note or chord, or convert Percy Bysshe Shelley's poem to music, letter by letter.  
datomu doesn't handle any musicality, it only converts the data accurately. So any musicality, if any, is produced by the data, or to say, produced by the wonderful nature.

Currently datomu can generate MIDI file. For example, the tool can convert 3.14159265 to C Major scale "E4 C4 F4 G4 B5 D4 A4 G4" note sequence and store to MIDI file. 

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

**--data**  
**--data-file filename**
--data specifies the data on the command line, for example, --data 3.14159265  
--data-file loads the data from `filename`. Since most data is long, --data-file is more useful than --data.  
There are pre-defined data in the `data` folder. You can use any data.  

**--converter**  
Specify the converter. The default converter is 'digit'.  
Availabe converters:  
`digit`: convert digit 1~9 to the notes in the scale degrees. 0 doubles the duration of the previous note.  
`letter`: convert letter a~z to the notes in the scale degrees. space, dot, comma, and '!?;:' doubles the duration of the previous note.  
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
`jp-hira`: Japanese Hirajōshi Scale  

**--outputer**  
Specifies the outputer, how the converted notes are outputted. The default value is 'midi'.  
Currently there is only one outputer, 'midi'. It will write the notes to MIDI file.  

**--output-file**    
Specifies the MIDI file name to write to. The default value is 'output.mid'.   

**--instrument**  
Specifies the instrument used in the MIDI file. The default value is 1, which is Acoustic Grand Piano.  
The value is 1~128, see https://soundprogramming.net/file-formats/general-midi-instrument-list/ for details.

**--tempo**  
Specifies the tempo in BPM for quarter note. The default value is 120  

**--note-count**  
Specifies how many notes will be converted and generated. The default value is 0, that means no limits, all notes will be converted.

### Example commands

`python datomu.py --converter digit --scale jp-hira --outputer midi --data-file mydata.txt --output-file myoutput.mid --tempo 120 --instrument 41 --note-count 100`  

## Developer document

Currently there is no document for developer. You are welcome to read the source code and contribute your code, especially new converters and new outputers.  
Warning: the code style doesn't conform PEP8 or any Python style. If you want to contribute, please follow current code style.  

## Motivations

I (wqking) like programming, I like music, I like the beauty of nature. datomu puts all what I like together, nothing is more exciting.  