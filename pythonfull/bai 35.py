def tong2so(a,b):

    if a==b  or abs(a-b)==5 or  (a+b)==5 :
        return True
    else:
        return False

print(tong2so(6,10))