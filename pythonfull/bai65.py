s=int(input("nhap giay = "))
day=s//86400
a=s%86400
gio=a//3600
b=a%3600
phut=b//60
giay=b%60

print("ngay {} gio {} phut {} giay {}" .format("day","gio","phut","giay"))
