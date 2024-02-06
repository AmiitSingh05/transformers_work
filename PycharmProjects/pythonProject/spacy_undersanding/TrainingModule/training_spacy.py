import spacy
from spacy.training.example import Example
from sentence_generator import list_of_sentences
# train_data = [
#     ("My name is Amit.", {"entities": [(11, 16, "PERSON")]}),
# ("This is Amit.", {"entities": [(7, 12, "PERSON")]}),
# ("Hi I am Amit.", {"entities": [(12, 13, "PERSON")]}),
# ("I as Amit.", {"entities": [(5, 10, "PERSON")]}),
#     # Add more examples with your name
# ]
train_data = list_of_sentences
#print("list_of_sentences type :", type(list_of_sentences))
#print(" type ", type(train_data))
nlp = spacy.load("en_core_web_sm")
#print(nlp.pipe_names, type(nlp.pipe_names[5]))

# Create a blank NER model
ner = nlp.get_pipe("ner")

# Add a new label to the NER model
ner.add_label("PERSON")
# Update the NER model with the training data
#print(list_of_sentences)
# for text, annotations in train_data:
#     print(type(text), type(annotations))
# for text, annotations in list_of_sentences:
#     print(type(text), type(annotations))
# print(train_data)

for text, annotations in list_of_sentences:
    example = Example.from_dict(nlp.make_doc(text), annotations)
    ner.update([example], drop=0.5)

# Save the model after training
nlp.to_disk("trained_ner_model2")
