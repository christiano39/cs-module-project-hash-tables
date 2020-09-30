# Your code here
def histogram(filename):
    f = open(filename, 'r')
    txt = f.read()
    words = txt.split(" ")

    word_count = {}
    for word in words:
        new_word = ""
        for c in word:
            if c.isalpha():
                new_word += c.lower()
        if new_word in word_count:
            word_count[new_word] += 1
        elif len(new_word) > 0:
            word_count[new_word] = 1

    word_count = list(word_count.items())
    word_count.sort(key=lambda t: t[1], reverse=True)

    print("Word Count\n")

    for tup in word_count:
        spaces = " " * (20 - len(tup[0]))
        hashes = "#" * tup[1]
        print(tup[0] + spaces + hashes)

histogram('robin.txt')