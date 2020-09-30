import re

def word_count(s):
    delimeters = " ", "\n", "\t", "\r"
    regex_pattern = '|'.join(map(re.escape, delimeters))

    words = re.split(regex_pattern, s)
    count = {}
    for word in words:
        alpha_word = ''
        for c in word:
            if c not in '":;,.-+=/\\|[]{}()*^&':
                alpha_word += c
        if alpha_word == '':
            continue
        alpha_word = alpha_word.lower()
        if alpha_word in count:
            count[alpha_word] += 1
        else:
            count[alpha_word] = 1
    return count





if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))