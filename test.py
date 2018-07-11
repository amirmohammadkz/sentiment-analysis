import spacy
nlp = spacy.load('en')
doc = nlp(u'This is not a sentence and im not amir mohammad.')
print([(i.text,i.tag_) for i in doc])