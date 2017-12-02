with open("2_day.txt") as f:
    raw = f.read()
    raw = raw.splitlines()

    text = []
    for i in raw:
        b = []
        a = i.split('\t')
        for c in a:
            b.append(int(c))
        text.append(b)

    def div(a):
        for i in a:
            for c in [x for x in a if x != i]:
                if i % c == 0:
                    return i / c
    tot = 0
    for i in text:
        tot += div(i)

    print(tot)
