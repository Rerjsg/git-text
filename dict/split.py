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
    "报告": 60,
}


def find_words(text):
    find = []
    unknow = ''
    i = 0

    while i < len(text):
        n = []

        for v, k in words.items():
            if text[i:].startswith(v):
                weight = k + len(v)*20
                n.append((weight, v))

        if len(n) > 0:
            if unknow:
                find.append(unknow)
                unknow = ''

            best_word = max(n)[1]
            find.append(best_word)
            i += len(best_word)

        else:
            unknow += text[i]
            i += 1

    if unknow:
        find.append(unknow)

    return find


print(find_words('hhh中国科学院hhh'))
