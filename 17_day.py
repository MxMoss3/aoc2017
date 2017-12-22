inp = 355
pos = 0
buf = [0]

for i in range(2017):
    pos = (pos + inp) % len(buf)
    buf.insert(pos + 1, i + 1)
    pos += 1

print(buf[buf.index(2017)], buf[buf.index(2017)+1])
