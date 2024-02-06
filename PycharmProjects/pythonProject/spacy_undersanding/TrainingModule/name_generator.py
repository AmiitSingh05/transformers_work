import random
import string

def generate_random_word():
    word_length = random.randint(3, 10)
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    random_word = ''.join(random.choice(letters) for _ in range(word_length))
    return random_word

# Generate and print 5 random words
for _ in range(5000):
    print(generate_random_word())
