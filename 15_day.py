a = 699
b = 124
a_factor = 16807
b_factor = 48271
div = 2147483647

tot = 0
for i in range(40000000):
    if i % 1000000 == 0:
        print(i)
    a = (a*a_factor) % div
    b = (b*b_factor) % div

    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]

    if bin_a[-16:] == bin_b[-16:]:
        tot += 1

print(tot)
