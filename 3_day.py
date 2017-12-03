number = int(input("What number: "))

#construct spiral
spiral = []
spiral.append([1])

ring_lev = 1
num = 2
while num <= number:
    ring = []
    while len(ring) < ring_lev * 8:
        ring.append(num)
        num += 1
    ring_lev += 1
    spiral.append(ring)

def Manhat_Dis(a):
    for i in a:
        if number in i:
            x = a.index(i)
            y = i.index(number)+1

            return x + abs((x) - ((y) % (x*2))) 

print(Manhat_Dis(spiral))
