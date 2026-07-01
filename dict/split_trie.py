import json
import math
from collections import Counter
from collections import defaultdict

with open("The Great Gatsby.txt", "r", encoding="utf-8")as f:
    text = f.read()

MAX_LEN = 4
all_words = []

for n in range(1, MAX_LEN + 1):
    for i in range(len(text) - n + 1):
        all_words.append(text[i:i+n])

word_count = Counter(all_words)
char_count = Counter(text)

left_neighbors = defaultdict(list)
right_neighbors = defaultdict(list)

for n in range(2, MAX_LEN + 1):

    for i in range(len(text) - n + 1):

        word = text[i:i+n]

        if i > 0:
            left_neighbors[word].append(text[i-1])

        if i + n < len(text):
            right_neighbors[word].append(text[i+n])


def probability(word_count: dict[str, int]) -> dict[str, float]:
    total = sum(word_count.values())
    return {k: v / total for k, v in word_count.items()}


pro = probability(word_count)

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


def calc_pmi(word, pro):

    p_word = pro[word]

    best = float("inf")

    for i in range(1, len(word)):

        left = word[:i]
        right = word[i:]

        if left not in pro or right not in pro:
            continue

        value = math.log2(
            p_word /
            (pro[left] * pro[right])
        )

        best = min(best, value)

    if best == float("inf"):
        return None

    return best


def high_probability(pro, pmi_threshold, entropy_threshold):

    stop_char = {
        "的", "地", "得",
        "了", "着", "过",
        "和", "与", "及",
        "把", "被"
    }

    for word in word_count:

        if len(word) == 2:
            if word[0] in stop_char or word[-1] in stop_char:
                continue
    high_words = {}

    for word in word_count:

        pmi = calc_pmi(word, pro)

        if pmi is None:
            continue

        left = entropy(left_neighbors[word])
        right = entropy(right_neighbors[word])

        if (
            pmi >= pmi_threshold
            and left >= entropy_threshold
            and right >= entropy_threshold
        ):
            high_words[word] = pmi

    return high_words


# print("出现次数:", word_count["说"])
# print("左:", left_neighbors["说"][:10])
# print("右:", right_neighbors["说"][:10])

# print("概率:", pro.get("说"))
# print("概率:", pro.get("忙忙"))
# print("概率:", pro.get("匆匆忙忙"))
# print("PMI:", calc_pmi("匆匆忙忙", pro))

# print("左熵:", entropy(left_neighbors["匆匆忙忙"]))
# print("右熵:", entropy(right_neighbors["匆匆忙忙"]))

pmi_threshold = 3
entropy_threshold = 0.8

high_words = high_probability(pro, pmi_threshold, entropy_threshold)

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

    while i < len(text) and i - start < 4:
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


# print(find_words(text))

with open("dictionary.json", "w", encoding="utf-8") as f:
    json.dump(high_words, f, ensure_ascii=False, indent=4)

# print("地" in high_words)
# print(high_words.get("匆匆忙忙"))
# print("地说" in high_words)
# print(word_count["地说"])


def score(word):
    if word not in pro:
        return 0

    pmi = calc_pmi(word, pro)
    if pmi is None:
        pmi = 0

    return pmi * len(word)


def segment(text):

    n = len(text)
    dp = [float("-inf")] * (n + 1)
    path = [None] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):

        for j in range(0, i):

            word = text[j:i]

            s = score(word)

            if dp[j] + s > dp[i]:
                dp[i] = dp[j] + s
                path[i] = j

    result = []
    i = n

    while i > 0 and path[i] is not None:
        j = path[i]
        result.append(text[j:i])
        i = j

    return result[::-1]


print(segment("研究生命起源"))
print(segment("昨天留下来的脚印已经被雪覆盖"))
