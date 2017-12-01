with open("1_day.txt") as f:
    text = f.read()

    text = list(text) 
    text.pop()
    text.append(text[0])
    tot = 0
    good = []
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            good.append(text[i])
            tot += int(text[i])
        else:
            None
    print(tot)
