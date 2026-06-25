words = ["s", "g"]


def words_find(text):
    find = []
    unknow = ''
    i = 0
    while i < len(text):
        found = False
        for w in words:
            if text[i:].startwith(w):
                if unknow:
                    find.append(unknow)
                    unknow = ''

                find.append(w)
                i += len(w)
                found = True
                break
        if not found:
            unknow += text[i]
            i += 1
    if unknow:
        find.append(unknow)

    return find


print(words_find())
