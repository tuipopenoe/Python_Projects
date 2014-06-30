# Tui Popenoe
# Create 2d lists

def twoD(x, y):
    a = []
    for i in xrange(x):
        a.append([])
        for j in xrange(3):
            a[i].append(i+j)

    return a