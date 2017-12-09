with open("8_day.txt") as f:
    raw = f.read().splitlines()

    text = []
    for i in raw:
        text.append(i.split(" "))

    regs = []
    for i in text:
        reg = []
        if [i[0], 0] not in regs:
            reg.append(i[0])
            reg.append(0)
            regs.append(reg)

    for i in text:
        if i[5] == '==':
            for c in regs:
                if i[4] in c and c[1] == int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])
        if i[5] == '>':
            for c in regs:
                if i[4] in c and c[1] > int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])
        if i[5] == '<':
            for c in regs:
                if i[4] in c and c[1] < int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])
        if i[5] == '>=':
            for c in regs:
                if i[4] in c and c[1] >= int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])
        if i[5] == '<=':
            for c in regs:
                if i[4] in c and c[1] <= int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])
        if i[5] == '!=':
            for c in regs:
                if i[4] in c and c[1] != int(i[6]):
                    for n in regs:
                        if n[0] == i[0]:
                            if i[1] == "inc":
                                n[1] += int(i[2])
                            else:
                                n[1] -= int(i[2])


    high = 0
    for i in regs:
       if int(i[1]) > high:
           high = int(i[1])

    print(high)
