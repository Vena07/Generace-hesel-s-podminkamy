import random
povoleneZnaky = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "", "|", ";", ":", "'", ",", ".", "<", ">", "/", "?", "`", "~"]
zakazaneZnaky = []
velikost = 0


def GeneraceHesla(velikost):
    global i, heslo, znak
    
    heslo = []
    for i in range(velikost):
        znak = random.choice(povoleneZnaky)
        heslo.append(znak)
    heslo = "".join(heslo)
print("Generování hesel")
print("------------")



while True:
    print(" ")
    print(f"1) Zakázané znaky:{zakazaneZnaky} ")
    print("2) Povolit zakazany znak")
    print(f"3) Počet znaku: {velikost}")
    print("4) Generace hesla")
    vyber = int(input("Zvolte zadli chcete upravit z něketrých podmínek nebo chete generovat heslo: "))    
    
    if vyber == 1:
        print(" ")
        vybranyZnak = str(input("Napiště znak který chete zakázat: "))
        if vybranyZnak in povoleneZnaky:
            povoleneZnaky.remove(vybranyZnak)
            zakazaneZnaky.append(vybranyZnak)
        else:
            print(" ")
            print("Znak je but už zakazaný, nebo znak není v nabídce znaků.")
    
    elif vyber == 2:
        print(" ")
        vybranyZnak = str(input("Napiště znak který chete zakázat: "))
        if vybranyZnak in zakazaneZnaky:
            zakazaneZnaky.remove(vybranyZnak)
            povoleneZnaky.append(vybranyZnak)
        else:
            print(" ")
            print("Znak je but už zakazaný, nebo znak není v nabídce znaků.")    
    
    elif vyber == 3:
        print(" ")
        velikost = int(input("Zvolte velikost hesla: "))
            
    
    
    elif vyber==4:    
        print(" ")
        GeneraceHesla(velikost)
        print(f"Heslo : {heslo} ")
    else:
        print(" ")
        print("Vybrali jste špatnou možnost")
        
    
    
    