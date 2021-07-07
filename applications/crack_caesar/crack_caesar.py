# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open("ciphertext.txt", "r")
txt = f.read()

ordered_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

letter_frequencies = {}

for c in txt:
    if c.isalpha() and c != 'â':
        if c in letter_frequencies:
            letter_frequencies[c] += 1
        else:
            letter_frequencies[c] = 1

letter_frequencies = list(letter_frequencies.items())

letter_frequencies.sort(key=lambda t: t[1], reverse=True)

decoder = {}
for i in range(len(ordered_letters)):
    decoder[letter_frequencies[i][0]] = ordered_letters[i]

deciphered_txt = ""
for c in txt:
    if c.isalpha() and c != 'â':
        c = decoder[c]
        deciphered_txt += c
    else:
        deciphered_txt += c

print(deciphered_txt)

