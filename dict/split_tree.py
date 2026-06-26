words = {
    "中国": 100,
    "中": 10,
    "科学": 90,
    "科学院": 80,
    "学院": 60,
    "计算": 70,
    "技术": 70,
    "研究": 60,
    "研究所": 90,
    "人工": 40,
    "人工智能": 100,
    "智能": 50,
    "实验": 40,
    "实验室": 90,
    "发布": 70,
    "大规模": 80,
    "规模": 30,
    "语言": 60,
    "语言模型": 100,
    "模型": 50,
    "研究报告": 95,
    "报告": 60
}

trie = {}


def insert(trie, word, weight):
    node = trie

    for w in word:
        if w not in node:
            node[w] = {}

        node = node[w]

    node["#"] = weight


for word, weight in words.items():
    insert(trie, word, weight)


def search(trie, text, start):
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


def find_words(text):
    find = []
    unknow = ""
    i = 0

    while i < len(text):
        n = []

        for v, k in search(trie, text, i):
            weight = k + len(v) * 20
            n.append((weight, v))

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


print(find_words("hhh中国科学院hhhaaa报告kkk人工智能"))
print(search(trie, "hhh中国科学院hhhaaa报告kkk人工智能", 3))
print(trie)
