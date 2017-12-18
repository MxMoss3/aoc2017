#Be Warned, this solution is very slow
with open("13_day.txt") as f:
    raw = f.read().splitlines()
    #raw = "0: 3\n1: 2\n4: 4\n6: 4".splitlines()

    layers = []
    for i in raw:
        layers.append([int(x) for x in i.split(':')])

    for i in range(layers[-1][0]):
        if layers[i][0] != i:
            layers.insert(i, [i])

    def try_pass(delay):

        caught = 0 

        for i in range(layers[-1][0] + 1):
            try:
                scanner = (i + delay) % (layers[i][1]*2 - 2)
                if scanner == 0:
                    caught += 1
            except IndexError:
                None
        
        if caught == 0:
            return True
        else:
            return False

    delay = 0

    while not try_pass(delay):
        delay += 1

    print(delay)

