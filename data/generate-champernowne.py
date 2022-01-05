import codecs

digitCount = 1000
outputFileName = 'champernowne-%d.txt' % (digitCount)
text = ''
n = 1
while len(text) < digitCount :
	text += str(n)
	n += 1
text = text[0 :  digitCount]
with codecs.open(outputFileName, "w", "utf-8") as file :
	file.write(text)
