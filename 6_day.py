raw = "4    10  4   1   8   4   9   14  5   1   14  15  0   15  3   5"

text = [int(x) for x in raw.split(" ") if x != '']

loop = True
combos = []

while loop:

    high = max(text)
    ind = (text.index(high) + 1) % len(text)
    text[text.index(high)] = 0
    while high > 0:
        text[ind] += 1
        ind = (ind + 1) % len(text)
        high -= 1

    
    if text in combos:
        loop = False

    combos.append([x for x in text])
        

print(len(combos))

