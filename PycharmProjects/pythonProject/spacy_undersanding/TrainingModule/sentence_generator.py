#from spacy_undersanding.TrainingModule.name_generator import (generate_random_word)
import ast
import json

from read_csv_to_list import get_name_list
from index_finder import find_word_indices

l1 = ["My", 'my', 'Her', 'her', 'His', 'his', 'Yours', 'yours',]
l2 = ['name', 'Name']
l3 = ["is", "are", "am", "was", "were",  "be" ]
#l4 = []
sentence_list = []
train_data = [("I am Amit.", {"entities": [(5, 10, "NEW_ENTITY")]})]

sentence = []




# for _ in range(50000):
#     l4.append(generate_random_word())
#     #print(generate_random_word())
#print(type(l4.append(get_name_list())))
l4 = get_name_list()
list_of_sentences = []
cnt = 0

def string_to_dict(input_string):
    items = input_string.split(',')
    my_dict = {}

    for item in items:
        key, value = item.split(':')
        my_dict[key] = value

    return my_dict



for one in l1:
    for two in l2:
        for three in l3:
            for four in l4:
                # ("My name is Amit.", {"entities": [(11, 16, "PERSON")]})
                a = '"'+one + " "+two+ " " + three + " "+ four + "." + '"'
                start_index, end_index = find_word_indices(a, four)
                dict_value = '{'+'"'+"entities"+'"'+ ': ' + '[' + '(' + str(start_index) + ', ' + str(end_index) + ', ' + '"' +'PERSON'+'"'+')'+']'+'}'
                #print(dict_value, type(ast.literal_eval(dict_value)))  #, string_to_dict(dict_value))
                #value = dict(dict_value)
                dict_value1 = ast.literal_eval(dict_value)
                #b = '(' + a + ',' + str(dict_value1) + ')'
                b = (a,dict_value1)
                cnt += 1
                #print(b)

                #print(find_word_indices(a, four))
                list_of_sentences.append(b)
print("Number of sentences generated : ",cnt)
# for text , annotations in list_of_sentences:
#     print(text, annotations)

