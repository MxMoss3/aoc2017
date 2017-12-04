with open("4_day.txt") as f:
    raw = f.read()

    text = []
    for i in raw.splitlines():
        text.append(i.split(" "))

    def valid(a):
        for i in a:
            if i in a[0:a.index(i)] or i in a[a.index(i)+1:]:
                return False
        return True
    
    tot = 0
    for i in text:
        if valid(i):
            tot += 1

    print(tot)


