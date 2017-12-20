a = 699
b = 124
a_factor = 16807
b_factor = 48271
div = 2147483647

a_val = []
while len(a_val) < 5000000:
    a = (a*a_factor) % div
    if a % 4 == 0:
        a_val.append(a)
        
b_val = []
while len(b_val) < 5000000:
    b = (b*b_factor) % div
    if b % 8 == 0:
        b_val.append(b)


tot = 0
for i,c in enumerate(a_val):
    if i % 100000 == 0:
        print(i)

    bin_a = bin(c)[2:]
    bin_b = bin(b_val[i])[2:]

    if bin_a[-16:] == bin_b[-16:]:
        tot += 1

print(tot)
