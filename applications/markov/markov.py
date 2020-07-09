import random


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


cache = {}
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

# split "words" into a list

word_list = words.split()

# look at each word
# store the word as the key
# store the word + 1

for idx, word in enumerate(word_list):

    if idx < (len(word_list) - 1):
        if word in cache:
            cache[word].append(word_list[idx + 1])

        else:
            cache[word] = [word_list[idx + 1]]

    else:
        break


# iterate through and if this word is not in your hash table you add it
# then you look one forward and append the following word to a list


# if the word is in the cache
    # we need to insert the word + 1 at the head of the list


# TODO: construct 5 random sentences
# Your code here

start_stop_cache = {
    "start": [],
    "stop": []
}

keys = list(cache.keys())
punct = [".", "?", "!", "?\"", ".\"", "!\""]

for key in keys:

    first_char = key[0]
    first_two_char = key[:2]
    last_char = key[len(key) - 1]
    last_two_char = key[:-2]

    if first_char.isupper() or first_two_char == ("\"" + first_char.upper()):
        start_stop_cache["start"].append(key)
    if last_char in punct or last_two_char in punct:
        start_stop_cache["stop"].append(key)

random_start = random.choice(start_stop_cache["start"])
print(random_start, end=" ")

current_word = random_start

while current_word not in start_stop_cache["stop"]:

    new_word = random.choice(cache[current_word])

    if new_word in start_stop_cache["stop"]:
        print(new_word)
        break
    else:
        current_word = new_word
        print(new_word, end=" ")
