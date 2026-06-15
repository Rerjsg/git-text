import re
result = {}
with open("D:\\data\\fruitmachine.blue_33_fruitmachine.2026-06-02.log", "r", encoding="utf-8") as f:

    for line in f:
        if not re.search(r'\buser_bet\b', line):
            continue

        uid = re.search(r'uid:([A-Za-z0-9]+)', line)
        if not uid:
            continue
        uid = uid.group(0)

        matches = re.findall(
            r'"tier_amount"\s*:\s*(\d+)\s*,\s*"times"\s*:\s*(\d+)', line)
        total = sum(int(a) * int(b) for a, b in matches)
        result[uid] = total+result.get(uid, 0)

        print(f'matches={matches}')

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

n = 0
for uid, total in sorted_result:
    if n < 10:
        print(uid, total)
        n += 1
    else:
        break
