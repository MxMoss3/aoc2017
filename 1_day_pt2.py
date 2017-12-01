with open("1_day.txt") as f:
    text = list(f.read())
    text.pop()

    tot = 0
    for i in range(len(text)):
        cycle = int(len(text) / 2)
        if i + cycle >= len(text):
            cycle = (i + cycle) - len(text)
            if text[i] == text[cycle]:
                tot += int(text[i])
        else:
            if text[i] == text[i+cycle]:
                tot += int(text[i])
            else:
                None
    print(tot)

