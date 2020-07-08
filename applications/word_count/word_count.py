cache = {}


def word_count(s):
    table = str.maketrans('', '', '":;,.-+=/\|[]{()}*^&')
    s = s.translate(table).lower()

    sentence = s.split()

    for word in sentence:
        if word not in cache:
            cache[word] = 1
        elif word in cache:
            cache[word] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
