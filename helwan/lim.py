from operator import *
global flag


def tansiq(rel,arr1,arr2):
    global flag
    tot = len(arr1) + len(arr2)
    z = tot * rel/ 100
    z=int(z)
    arr1 = sorted(arr1, key=itemgetter('Degree'), reverse=True)
    arr2 = sorted(arr2, key=itemgetter('Degree'))
    if z <= len(arr1):
        flag = 0
        return arr1[z-1]
    else:
        x = z - len(arr1)
        flag = 1
        return arr2[x]
