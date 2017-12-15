with open("11_day.txt") as f:
    inst = ((f.read()).splitlines()[0]).split(",")

    coor = [0,0]
    
    for i in inst:
        if i == 'n':
            coor[1] += 1
        if i == 'ne':
            coor[0] += 1
            coor[1] += .5
        if i == 'se':
            coor[0] += 1
            coor[1] -= .5
        if i == 's':
            coor[1] -= 1
        if i == 'sw':
            coor[0] -= 1
            coor[1] -= .5
        if i == 'nw':
            coor[0] -= 1
            coor[1] += .5
    
    print(abs(coor[0]) + int(abs(coor[1]) - abs(coor[0])*.5))
