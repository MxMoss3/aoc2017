with open("9_day.txt") as f:
    raw = list(f.read())
    raw.pop()

    #do ! first
    while "!" in raw:
        a = raw.index("!")
        raw.pop(a)
        raw.pop(a)

    tot = 0
    #remove garbage
    while "<" in raw and ">" in raw:
        a = raw.index("<")
        b = raw.index(">")
        tot += ((b-a)-1)
        for i in range((b-a) + 1):
            raw.pop(a)

    print(tot)
