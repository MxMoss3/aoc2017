#this is also terrible, but it works
number = int(input("What number? "))

spiral = []
spiral.append([0, 0, 1])
spiral.append([1, 0, 1])

def findval(x,y):
    for i in spiral:
        if i[0] == x and i[1] == y:
            return i[2]
    return 0

def add_adj(x,y):
    tot = 0
    for i in range(3):
        for c in range(3):
            a = x+(i-1)
            b = y+(c-1)
            tot += findval(a,b)
    return tot

def spir():
    num = 0
    ring = 2
    x = 1
    y = 0
    while spiral[-1][2] <= number + 1:
        for i in range(ring*2 - 3):
            y += 1
            spiral.append([x,y,add_adj(x,y)])
        for i in range(ring*2 - 2):
            x -= 1
            spiral.append([x,y,add_adj(x,y)])
        for i in range(ring*2 - 2):
            y -= 1
            spiral.append([x,y,add_adj(x,y)])
        for i in range(ring*2 - 1):
            x += 1
            spiral.append([x,y,add_adj(x,y)])

        ring += 1
    for i in spiral:
        if i[2] > number:
            return i[2]
        else:
            None
print(spir())

