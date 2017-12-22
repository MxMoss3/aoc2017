inp = 355
pos = 0
buf = [0]

for i in range(50000000):
    if i % 1000000 == 0:
        print(i)
    pos = (pos + inp) % (i + 1)
    if pos == 0:
        buf.insert(pos + 1, i + 1)
    pos += 1

print(buf[1])
