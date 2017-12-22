with open("16_day.txt") as f:
    inst = f.read().splitlines()[0].split(',')

    begin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    prog = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

    def spin(num):
        for i in range(int(num)):
            prog.insert(0, prog.pop())

    def swap(x,y):
        prog[int(x)], prog[int(y)] = prog[int(y)], prog[int(x)]

    def partner(x,y):
        a = prog.index(x)
        b = prog.index(y)
        prog[a], prog[b] = prog[b], prog[a]


    def dance():

        for i in inst:
            if i[0] == 's':
                spin(i[1:])
            elif i[0] == 'x':
                swap(i[1:].split('/')[0],i[1:].split('/')[1])
            elif i[0] == 'p':
                partner(i[1:].split('/')[0],i[1:].split('/')[1])
            
        new = []

        for i in prog:
            new.append(i)

        return new

    cycle = []
    count = 0
    complete = False
    while not complete:
        count += 1
        
        a = dance()
        cycle.append(a)

        if prog == begin:
            complete = True

    print(''.join(cycle[(1000000000 % count)-1]))


