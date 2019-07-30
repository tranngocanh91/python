def chuoi(str):


    if len(str) >=2 and  len(str[:1])=="is":
        return str
    return "is" + str

print(chuoi("anhlaconga"))