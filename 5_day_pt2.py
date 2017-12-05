with open("5_day.txt") as f:
    instruct = [int(x) for x in f.read().splitlines()]
    #instruct = [0,3,0,1,-3]
    
    step = 0
    pos = 0

    cont = True
    while cont:
        try:
            a = instruct[pos]
            if a >= 3:
                instruct[pos] -= 1
            else:
                instruct[pos] += 1
            pos = pos + a
            step += 1

            
        except IndexError:
            print(step)
            cont = False
