with open("7_day.txt") as f:
    raw = f.read().splitlines()

    text = []
    for i in raw:
        text.append(i.split(" "))

    for i in text:
        for c in i:
            i[i.index(c)] = c.strip("(),")

    bot = text[0][0]
    
    incr = 0
    while True:
        if incr < len(text):
            if len(text[incr]) > 2:
                if bot in text[incr][3:]:
                    bot = text[incr][0]
                    incr = 0
                else:
                    incr += 1
            else:
                incr += 1
        else:
            break


    def tree(a):
        t = []

        for i in text:
            if i[0] == a:
                t.append(i[0])
                t.append(i[1])

                if len(i) > 3:
                    for c in i[3:]:
                        t.append(tree(c))

        return t
    
    def weight(a):
        if len(a) > 2:
            w = int(a[1])
            for i in a[2:]:
                w += weight(i)
            return w
        else:
            return int(a[1])
    
    def balanced(a):
        if len(a) > 2:
            weights = []
            for i in a[2:]:
                weights.append(weight(i)) 

            equal = True
            for i in weights:
                if weights[0] == i:
                    None
                else:
                    odd = i
                    equal = False
            
            if equal:
                return True
            else:
                return False 
            
        else:
            return True
            


    def find_unbal(a, reg):
        children = []
        w = []

        for i in a[2:]:
            children.append(i)
            
        for i in children:
            w.append(weight(i))
            if balanced(i):
                None
            else:
                return find_unbal(i, 0)

        
        for i in children:
            if w.count(weight(i)) == 1:
                odd = i
            else:
                reg = i

                
        return weight(reg) - (weight(odd) - int(odd[1]))

                
    print(find_unbal(tree(bot), 0))
