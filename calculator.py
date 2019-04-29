import math

def toplama(x,y):
    return x+y

def çıkarma (x,y):
    return x-y

def çarpma (x,y):
    return x*y

def bölme (x,y):
    return x/y

def faktöriyel(x) :
    answer = 1
    for i in range(1,x+1):
        answer*=i
    return answer
    #bunun yerine math.factorial(x) 'de diyebiliriz.

def üs_al(x,y):
    return x**y
    #bunun yerine math.pow(x,y) 'de diyebilirz.

def mod_al(x,y):
    return x%y

print("""         ==============CALCULATOR================
         || TOPLAMA : +                         || 
         || ÇIKARMA : -                         ||
         || BÖLME : /                           ||
         || ÇARPMA : *                          ||
         || KUVVET ALMA : q      ( BKZ:2q3 )    ||
         || FAKTÖRİYEL HESAPLAMA : !            ||
         || MODUNU AL : %                       ||
         ========================================
         (çıkış için işleme e yazınız !""")
işlemler = ["+","-","/","*","q","!","%"]

try:
    sayı1 = int(input("sayı :"))
except ValueError:
    print("Lütfen Sayı Giriniz")
    exit()

while True :

    while True:
        işaret = input("işlem :")
        if işaret in işlemler:
            break
        if işaret == "e":
            print("kapatılıyor..")
            exit()
        else:
            print("Geçerli bir işlem giriniz!!")

    if işaret == "+" :
        sayı2 = input("sayı:")
        sayı2 = int(sayı2)
        sayı1 = toplama(sayı1,sayı2)

    elif işaret == "-" :
        sayı2 = input("sayı:")
        sayı2 = int(sayı2)
        sayı1 = çıkarma(sayı1,sayı2)

    elif işaret == "*" :
        sayı2 = input("sayı:")
        sayı2 = int(sayı2)
        sayı1 = çarpma(sayı1,sayı2)

    elif işaret == "/" :
        sayı2 = input("sayı:")
        sayı2 = int(sayı2)
        sayı1 = bölme(sayı1,sayı2)

    elif işaret == "%" :
        sayı2 = input("sayı:")
        sayı2 = int(sayı2)
        sayı1 = mod_al(sayı1,sayı2)

    elif işaret == "!" :
        sayı1 = faktöriyel(sayı1)

    elif işaret == "q" :
        sayı2 = input("sayının kuvveti:")
        sayı2 = int(sayı2)
        sayı1 = üs_al(sayı1,sayı2)


    print(sayı1)





