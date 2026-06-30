import json
with open("dictionary.json", "r", encoding="utf-8") as f:
    words = json.load(f)

trie = {}


def insert(trie, word, weight):
    node = trie

    for w in word:
        if w not in node:
            node[w] = {}

        node = node[w]

    node["#"] = weight


def search(trie, text, start):
    node = trie
    result = []
    i = start

    while i < len(text) and i - start < 4:
        w = text[i]

        if w not in node:
            break

        node = node[w]

        if "#" in node:
            result.append((text[start:i+1], node["#"]))

        i += 1

    return result


def find_words(text):
    find = []
    unknow = ""
    i = 0

    while i < len(text):
        n = []

        for v, k in search(trie, text, i):
            # weight = k / (len(v) ** 0.5)
            weight = k
            n.append((weight, v))
            print(f"{v},{k},{weight}")

        if n:

            if unknow:
                find.append(unknow)
                unknow = ""

            best_word = max(n, key=lambda x: x[0])[1]
            find.append(best_word)
            i += len(best_word)

        else:
            unknow += text[i]
            i += 1

    if unknow:
        find.append(unknow)

    return find


for word, weight in words.items():
    insert(trie, word, weight)

print(search(trie, '匆匆忙忙', 0))

print(find_words("汽车路匆匆忙忙跟铁路会合"))
print("匆匆忙忙" in words)
print(words.get("匆匆忙忙"))
