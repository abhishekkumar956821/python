#Pattern #3 - Printing Numbers Using Inverted Pyramids
#Pyramid

n = 7

m = 0

for k in range(n, 0, -1):

    m += 1

    for n in range(1, k + 1):

        print(m, end=' ')

    print('\r')


# output
# 1 1 1 1 1 1 1

# 2 2 2 2 2 2

# 3 3 3 3 3 

# 4 4 4 4 

# 5 5 5

# 6 6

# 7
