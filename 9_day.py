with open("9_day.txt") as f:
    raw = list(f.read())
    raw.pop()

    #do ! first
    while "!" in raw:
        a = raw.index("!")
        raw.pop(a)
        raw.pop(a)

    #remove garbage
    while "<" in raw and ">" in raw:
        a = raw.index("<")
        b = raw.index(">")
        for i in range((b-a) + 1):
            raw.pop(a)

    raw = [x for x in raw if x != ',']
    
    def group(ind):
        a = len([x for x in raw[0:ind] if x == "{"])
        b = len([x for x in raw[0:ind] if x == "}"])
        return (a-b) + 1

    tot = 0
    for i,c in enumerate(raw):
        if c == "{":
            tot += group(i)

    print(tot)



    
