
#takes in a list
def knot(inp):

    inp = [ord(x) for x in inp]
    inp = inp + [17, 31, 73, 47, 23]
    
    loop = [x for x in range(256)]
    pos = 0
    skip = 0


    def reverse(a,i):
        for c in range(i // 2):
            x = (a + c) % len(loop)
            y = ((a + (i-1)) - c) % len(loop)

            loop[x], loop[y] = loop[y], loop[x]

        return loop

    def xor(a):
        x = a[0]
        for c in range(len(a)-1):
            x = x ^ a[c+1]
        return x


    #step 1

    for num in range(64):
        for i in [int(x) for x in inp]:
            reverse(pos,i)
            pos = (pos + i + skip) % len(loop)
            skip += 1

    #step 2

    xored = []

    for i in range(16):
        xored.append(xor(loop[16*i:(16*i + 16)]))

    #step 3

    hexidec = []
    for i in xored:
        if len(hex(i)[2:]) == 2:
            hexidec.append(hex(i)[2:])
        else:
            hexidec.append('0' + hex(i)[2:])
    hexidec = list(''.join(hexidec))

    
    binary = []
    for i in list(''.join(hexidec)):
        binary.append(bin(int(str(i),16))[2:].zfill(4))

    return ''.join(binary)


string = 'ffayrhll'
grid = []
for i in range(128):
    inp = list(string + '-' + str(i))

    grid.append(list(knot(inp)))

def region(y,x):
    #print(y,x)
    grid[y][x] = 'X'
    #twentyxtwenty()
    #input()

    n = [x, y+1]
    e = [x+1, y]
    s = [x, y-1]
    w = [x-1, y]
    
    direct = [n,e,s,w]

    to_change = []

    for i in direct:
        try:
            if i[0] >= 0 and i[1] >= 0:
                if grid[i[1]][i[0]] == '1':
                    region(i[1], i[0])
        except IndexError:
            None
    
#debugging
def twentyxtwenty():
    for i in range(15):
        for c in range(15):
            print(grid[i][c], end=' ')
        print()
        
    

tot = 0
for i,c in enumerate(grid):
    for a,b in enumerate(c):
        if b == '1':
            tot += 1
            region(i,a)
        else:
            None

print(tot)



            



