from data import emojies

def emojify(text):
	for ename in emojies:
		text = ' '.join([w.replace(ename, emojies[ename]) for w in text.split(" ")])
		text = str(text)

	return text
