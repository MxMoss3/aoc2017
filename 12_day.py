with open("12_day.txt") as f:
    raw = f.read().splitlines()

    inst = []
    for i in raw:
        a = ''.join([x for x in i if x not in ['<','-','>',',']])
        a = a.split(' ')
        a.pop(1)
        inst.append(a)

    connect = []
    for i in inst[0]:
        connect.append(i)
    
    while True:
        length = len(connect)
        for i, pipe in enumerate(inst):
            for c in pipe:
                if c in connect:
                    for x in pipe:
                        if x not in connect:
                            connect.append(x)
                    del inst[i]
                    break
        if length == len(connect):
            break
        else:
            None


    print(len(connect))

