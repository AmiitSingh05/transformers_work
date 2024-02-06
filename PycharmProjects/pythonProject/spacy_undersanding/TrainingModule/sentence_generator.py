import ast
from read_csv_to_list import get_name_list
from index_finder import find_word_indices

l1 = ["My", 'my', 'Her', 'her', 'His', 'his', 'Yours', 'yours',]
l2 = ['name', 'Name']
l3 = ["is", "are", "am", "was", "were",  "be" ]
sentence_list = []
sentence = []
l4 = get_name_list()
list_of_sentences = []
cnt = 0


def string_to_dict(input_string):
    """
    This function convert str object to dictionary
    :param input_string: string object
    :return: dict object
    """
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
                a = '"'+one + " "+two+ " " + three + " "+ four + "." + '"'
                start_index, end_index = find_word_indices(a, four)
                dict_value = '{'+'"'+"entities"+'"'+ ': ' + '[' + '(' + str(start_index) + ', ' + str(end_index) + ', ' + '"' +'PERSON'+'"'+')'+']'+'}'
                dict_value1 = ast.literal_eval(dict_value)
                b = (a,dict_value1)
                cnt += 1
                list_of_sentences.append(b)
print("Info: Number of sentences generated : ",cnt)

