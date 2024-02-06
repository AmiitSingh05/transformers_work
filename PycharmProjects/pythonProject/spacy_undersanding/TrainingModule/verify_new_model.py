"""
This module is to verify if the fine_tuned_model, trained_ner_model is trained
for new set of training data. finally able to recognized my name "Amit" - 'PERSON'
"""

import spacy

nlp = spacy.load("trained_ner_model2")
#nlp = spacy.load("en_core_web_sm")

new_text = "my Name is Amit, i am working with Unisys at California."
doc = nlp(new_text)
a =[(ent.text, ent.label_) for ent in nlp(new_text).ents]
print(" ner : ",a)