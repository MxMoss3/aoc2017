raw = "212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164"
inp = list(raw.split(','))

loop = [x for x in range(256)]
pos = 0
skip = 0

def reverse(a,i):
    for c in range(i // 2):
        x = (a + c) % len(loop)
        y = ((a + (i-1)) - c) % len(loop)

        loop[x], loop[y] = loop[y], loop[x]

    return loop

for i in [int(x) for x in inp]:
    reverse(pos,i)
    pos = (pos + i + skip) % len(loop)
    skip += 1


print(loop[0] * loop[1])

