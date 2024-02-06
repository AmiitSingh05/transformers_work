def find_word_indices(sentence, word):
    # Convert both the sentence and the word to lowercase for case-insensitive matching
    sentence = sentence.lower()
    word = word.lower()

    # Check if the word is present in the sentence
    if word in sentence:
        # Find the beginning index of the word
        start_index = sentence.find(word)

        # Calculate the end index of the word
        end_index = start_index + len(word) - 1

        return start_index, end_index
    else:
        # If the word is not found in the sentence, return a message indicating so
        return "Word not found in the sentence"


# Example usage:
sentence = "This is a sample sentence to demonstrate the program."
word_to_find = "sample"

result = find_word_indices(sentence, word_to_find)

if isinstance(result, tuple):
    start_index, end_index = result
    print(f"The word '{word_to_find}' starts at index {start_index} and ends at index {end_index}.")
else:
    print(result)
