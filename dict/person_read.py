

with open("article.txt", "r", encoding="utf-8")as f:
    text = f.read()

word = list(text)

words = [text[i:i+2] for i in range(len(text)-1)]

wordss = [text[i:i+3] for i in range(len(text)-2)]

# print(words)


def times(words: list[str]) -> dict[str, int]:
    words_time = {}
    for w in words:
        if w in words_time:
            words_time[w] += 1
        else:
            words_time[w] = 1
    return words_time


# print(times(wordss))


def probability(word_count: dict[str, int]) -> dict[str, float]:
    total = len(words)
    pro = {}
    for k, v in word_count.items():
        pro[k] = v/total
    return pro


word_count = times(words)
pro = probability(word_count)
# print(pro)


def high_probability(pro: dict[str, float], threshold: float) -> dict[str, float]:
    high_words = {}

    for word, p in pro.items():
        if p >= threshold:
            high_words[word] = p

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
