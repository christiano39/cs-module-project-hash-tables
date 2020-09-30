import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words.replace('\n', '')
    words = words.split(" ")

# TODO: analyze which words can follow other words
# Your code here
following_words = {}

for i in range(len(words) - 1):
    if words[i] not in following_words:
        following_words[words[i]] = []
    following_words[words[i]].append(words[i + 1])
    # print(i, words[i])


# TODO: construct 5 random sentences
# Your code here
def construct_sentence():
    starting_word = random.choice([w for w in words if w.capitalize() == w])
    print(starting_word, end=" ")

    current_word = starting_word
    while current_word[-1] not in '.?!' and (len(current_word) < 2 or (current_word[-1] != "\"" and current_word[-2] not in '.?!')):
        current_word = random.choice(following_words[current_word])
        print(current_word, end=" ")

for i in range(5):
    print(f"#{i + 1}")
    construct_sentence()
    print('\n')
