with open("7_day.txt") as f:
    raw = f.read().splitlines()

    text = []
    for i in raw:
        text.append(i.split(" "))

    for i in text:
        for c in i[3:-1]:
            i[i.index(c)] = c.strip('(),')
        None

    bot = text[0][0]
    
    incr = 0
    while True:
        if incr < len(text):
            if len(text[incr]) > 2:
                if bot in text[incr][3:]:
                    bot = text[incr][0]
                    incr = 0
                else:
                    incr += 1
            else:
                incr += 1
        else:
            break

print(bot)

