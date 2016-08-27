def modify_list(l):
    i = l.__len__() - 1
    while i >= 0:
        if l[i] % 2 != 0:
            l.__delitem__(i)
            i -= 1
        else:
            l[i] //= 2
            i -= 1