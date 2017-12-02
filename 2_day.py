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
    
    def diff(a):
        return int(max(a)) - int(min(a)) 


    tot = 0
    for i in text:
        tot += diff(i)

    print(tot)
    
