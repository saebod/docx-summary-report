
import docx2txt

def Character_Count(filepath, stopword=None):
	text = docx2txt.process(filepath)
	if stopword is not None:
		text = text.split(stopword, 1)[0]
		number_of_characters = len(text)
	else:
		number_of_characters = len(text)
	return number_of_characters
