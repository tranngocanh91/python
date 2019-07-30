'''adawaiahwdiawhdwad'''

def translate(phrase):
    a=""
    for letter in phrase :
        if letter in "aieou":
            a=a + "g"
        else:
            a=a + letter
    return a
print(translate(input("enter a phrase  : ")))