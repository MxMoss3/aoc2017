with open("1_day.txt") as f:
    text = list(f.read())
    text.pop()

    text.append(text[0])
    tot = 0
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            tot += int(text[i])
        else:
            None
    print(tot)
