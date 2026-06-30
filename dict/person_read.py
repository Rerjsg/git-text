import math
from collections import Counter
from collections import defaultdict

with open("The Great Gatsby.txt", "r", encoding="utf-8")as f:
    text = f.read()

word = list(text)

words = [text[i:i+2] for i in range(len(text)-1)]

wordss = [text[i:i+3] for i in range(len(text)-2)]

# print(words)


word_count = Counter(words)
char_count = Counter(text)

# print(times(wordss))

left_neighbors = defaultdict(list)
right_neighbors = defaultdict(list)

for i in range(len(text) - 1):
    word = text[i:i+2]
    if i > 0:
        left_neighbors[word].append(text[i-1])
    if i+2 < len(text):
        right_neighbors[word].append(text[i+2])


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


def entropy(chars):
    if not chars:
        return 0

    count = Counter(chars)
    total = len(chars)

    h = 0

    for c in count.values():
        p = c/total
        h -= p*math.log2(p)
    return h


def high_probability(pro: dict[str, float], pmi_threshold, entropy_threshold) -> dict[str, float]:
    high_words = {}

    for word, p_xy in pro.items():
        x = word[0]
        y = word[1]
        p_x = char_pro[x]
        p_y = char_pro[y]
        pmi = math.log2(p_xy/(p_x*p_y))

        left = entropy(left_neighbors[word])
        right = entropy(right_neighbors[word])

        if (
            pmi >= pmi_threshold
            and left >= entropy_threshold
            and right >= entropy_threshold
        ):
            high_words[word] = pmi

    return high_words


pmi_threshold = 3
entropy_threshold = 1

high_words = high_probability(pro, pmi_threshold, entropy_threshold)

# result = sorted(high_words.items(), key=lambda x: x[1], reverse=True)
# print(result[50:100])


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
