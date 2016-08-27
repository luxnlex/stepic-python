def f(x):
    if (x<=-2):
        n = 1-(x+2)**2
    elif (x>2):
        n = 1+(x-2)**2
    else:
        n = -1 * (x/2)
    return n