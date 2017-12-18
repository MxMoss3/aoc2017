with open("13_day.txt") as f:
    raw = f.read().splitlines()

    layers = []
    for i in raw:
        layers.append([int(x) for x in i.split(':')])

    for i in range(layers[-1][0]):
        if layers[i][0] != i:
            layers.insert(i, [i])

    severity = 0 

    for i in range(layers[-1][0] + 1):
        try:
            scanner = i % (layers[i][1]*2 - 2)
            if scanner == 0:
                severity += layers[i][0] * layers[i][1]
        except IndexError:
            None

    print(severity)
        
    
        

