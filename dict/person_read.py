from collections import Counter

with open("article.txt", "r", encoding="utf-8")as f:
    text = f.read()

word = list(text)

words = [text[i:i+2] for i in range(len(text)-1)]

wordss = [text[i:i+3] for i in range(len(text)-2)]

# print(words)


word_count = Counter(words)
char_count = Counter(text)

# print(times(wordss))


def probability(word_count: dict[str, int]) -> dict[str, float]:
    total = len(words)
    pro = {}
    for k, v in word_count.items():
        pro[k] = v/total
    return pro


pro = probability(word_count)
# print(pro)
char_total = len(text)
char_pro = {}
for c, count in char_count.items():
    char_pro[c] = count / char_total


def high_probability(pro: dict[str, float], threshold: float) -> dict[str, float]:
    high_words = {}

    for word, p_xy in pro.items():
        x = word[0]
        y = word[1]
        p_x = char_pro[x]
        p_y = char_pro[y]
        if p_xy > p_x*p_y:
            high_words[word] = p_xy

    return high_words


threshold = 0.0019

high_words = high_probability(pro, threshold)

print(high_words)

trie = {}


def insert(trie: dict, word: str, probability: float) -> None:
    node = trie

    for w in word:
        if w not in node:
            node[w] = {}

        node = node[w]

    node["#"] = probability


for word, p in high_words.items():
    insert(trie, word, p)


def search(trie: dict, text: str, start: int) -> list:
    node = trie
    result = []
    i = start

    while i < len(text):
        w = text[i]

        if w not in node:
            break

        node = node[w]

        if "#" in node:
            word = text[start:i+1]
            result.append((word, node["#"]))

        i += 1

    return result


def find_words(text: str) -> list[str]:
    find = []
    unknow = ""
    i = 0

    while i < len(text):
        n = []

        for v, k in search(trie, text, i):

            n.append((k, v))

        if n:

            if unknow:
                find.append(unknow)
                unknow = ""

            best_word = max(n)[1]
            find.append(best_word)
            i += len(best_word)

        else:
            unknow += text[i]
            i += 1

    if unknow:
        find.append(unknow)

    return find


print(find_words(text))
