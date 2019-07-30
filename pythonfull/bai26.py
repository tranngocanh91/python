def thamso(items):
    for n in items:
        output = ""
        while ( n > 0):
            output+="$"
            n=n-1
        print(output)



thamso([2,5,7,9,3])