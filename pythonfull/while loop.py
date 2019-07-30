secret_word = "anh321"
guess = " "
guess_zero = 0
guess_limit = 3
rangoai= False
while guess != secret_word and not(rangoai):
    if guess_zero<guess_limit :
        guess=input("nhap lai = ")
        guess_zero +=1
    else:
        rangoai = True
if rangoai :

    print(" ban da thua")
else :
    print("you win")