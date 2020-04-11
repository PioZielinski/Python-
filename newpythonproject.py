#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#_author__ = "piotr"
#__date__ = "$2020-04-03 15:53:49$"
#
#if __name__ == "__main__":
#    print "Hello Word"
zadanie 1
--------------------------------------
for user in range (0,3):
    name = raw_input("jak massz na imie")
print("Czesc",name)
    
zadanie 2
--------------------------------------
counter = 0
while counter !=3:
    name = raw_input(str(counter)+"Jak masz na imie:   ")
    print("czesc",name)
counter +=1


zadanie 3
--------------------------------------
a=5
a= int(raw_input("wpisz liczbe wieksza od 4   "))
while (a>4):
   
    print("liczba wieksza od cztery to",a)
    print("podana liczba a nie jest wieksza od 4")
    break
      
zadanie 4
---------------------------------------


book = 59
while book > 30:
  print("Czekam na przecene")
  book = book * 0.8
  print("Przecena 20%, aktualna cena: ", round(book, 2), "zl")
  print("— — — — — — — — — — — — — — — — — —")
  print("\nIdę do księgarni!") 

zadanie 5
------------------------------------------------

num = 10
while num <20:
    num +=1
    if num ==15:
        continue
    print("aktualny numer to ",num)
print("jestem poza petla")    

zadanie 6
--------------------------------------------------------

import random

b = random.randint(0,4)

while True:
a = int(raw_input("podaj liczbe od 1-2      "))    
    if a==b:
        print("podales prawidlowa liczbe")
    else:
        print("pomyliles sie")


zadanie 7
------------------------------------------------------

   
a=1
b=2

podanaliczba=int(input('podaj liczbe'))-1  
d=podanaliczba+1
print(d)

for c in range(0,podanaliczba):
     a=a*b
     b=b+1
     while b==d:
        print('silnia liczby',d,'to',a*b)
        break

zadanie 8
-------------------------------------------------------------------

for r in range(0,2):
        print(r)
        
        z = str(raw_input("Zgadnij co to za slowo ?    :"+ zagadka))
        while True:
                if z==r:
                    print("brawo Ty - odgadles haslo")
                    break
                else:
                    print("sprobuj jeszcze raz")
                    break
                    
zadanie 9
--------------------------------------------------------------------------
import random
lista = ["szklanka", "wafle", "serek", "woda", "zegarek", "zeszyt", "tabletki", "myszka", "olowke", "talerz"]

losujemy dowolna liczba (random.randrange) z przedzialu od 0 do ilosci wyrazow (len(lista))
liczba = random.randrange(len(lista))


los = lista[liczba]


los = list(los)


print("Uloz z podanych liter slowo: ", zagadka)
slowo = str(raw_input("Podaj odpowiedz: "))
while slowo not in lista:
    print("Zla odpowiedz!")
    print("Uloz z podanych liter slowo: ", zagadka)
    slowo = str(raw_input("Sprobuj jeszcze raz: "))
    if slowo == "q" or "Q":
        print("Zakonczyles petle.")
    else:
        print("Zgadles, odpowiedz to: ", slowo)

zolwie = str(raw_input("czy lubie zolwie: odpowiedz TAK lub NIE      :"))
p1 = "TAK"

if zolwie==p1 :
        print("poprawna odpowiedz")
else:
        print("nie poprawna odpowwiedz")

urodziny = str(raw_input("za ile dni mam urodziny    :" ))  
p2=6
if urodziny==6:
             print("poprawna odpowiedz")
else:
                print("Próbuj dalej ")
mettalica = str(raw_input("Czy sluchalem w mlodosci mettaliki??  odpowiedz TAK lub NIE      :"))
p3= "TAK"            
if mettalica ==p3:
                    print("dobrze")
else:
                    print("za malo mnie  znasz :)")
zielony = str(raw_input("MOj ulubiony kolor zaczyna sie na litere ?"))
p4 = "z"

if zielony ==p4:
                            print("dobrze")
else:
                            print("zle")

        
zadanie 10
--------------------------------------------------------------------------------


#op = "t"
#while op == "t":
#    a, b, c = str(raw_input("Podaj trzy liczby oddzielone spacjami: ")).split(" ")
#
#    print("Wprowadzono liczby:", a, b, c)
#    print("\nNajmniejsza:")
#
#    if a < b:
#        if a < c:
#            najmniejsza = a
#        else:
#            najmniejsza = c
#    elif b < c:
#        najmniejsza = b
#    else:
#        najmniejsza = c
#
#    print(najmniejsza)
#
#    op = str(raw_input("Jeszcze raz (t/n)? "))
#
#print("Koniec.")

#
#def pogoda():
#    print("fsds")
#    print("fsdf")
#    
#pogoda()  
#
#def przedstawsie(imie,wiek):  
#    print("mam na imie" + imie)
#    print("mam" +wiek)
#    
#przedstawsie("   piotr  "," 33 lata")
#przedstawsie("  rysiu ", " 22 lata  ")

#def dziennik(klasa,**kwargs):
#    print('klasa' + klasa)
#    for nazwisko in kwargs.keys():
#      print(nazwisko)
#    print(kwargs.get('Kowalski'))  
#        
#dziennik('3c',kowalski='1',nowak='2')        

#def dodawanie(pierwsza,druga):
#     return(pierwsza+druga)
#
#pierwsza_suma=dodawanie(2,2)
#druga_suma=dodawanie(1,1)
#print(dodawanie(2,2)+dodawanie(1,1))
#
#def odejmowanie(a,b):
#    print(a-b)
#
#roznica = odejmowanie(3,2)
#print(roznica)

#imie = 'alaa'
#nazwisko= "kowalski 'nowak'"
#adres = '''kwiatowa 28c/1
            
#print(nazwisko)
#print("male liter".upper())
#print(nazwisko.isupper())
#
#for char in 'alaa':
#    print(char)
#    
#print(imie[0])
#print(imie[0:3])
#print(imie.index("a"))
#print("ala" not in "ala ma kota")
#
#print("ok".join([ " ala ", " ma " , " kota " ]))
#print("ma nazwisko ".join(["piotr ","zielinski"]))
#print("ala,ma,kota,i,psa").split("!")
#print(imie.startswith("Ba"))
#
#imiona = ["kasia","bartek","andrzej",1,2,3,45]
#print(imiona[0])
#print(imiona[6])
#print(imiona[0:4])
#print(imiona.index("kasia"))
#
#imiona.append("wojtek")
#imiona.insert(1,"grzegorz")
#print(len(imiona))
#
#print(imiona)
#del(imiona[0])
#print(imiona)
#
#pierwsz_lista = ["lampa","koc"]
#druga_lista=["auto","pociag"]
#print(pierwsz_lista+druga_lista)
#print(pierwsz_lista*3)

#nazwiska=["zielinski","adamiak","kurnicka"]
#posortowane= sorted(nazwiska,reverse=False)
#print(nazwiska)
#print(posortowane)

#JEZYKI_programowania=("js","php")
#print(JEZYKI_programowania[1])
#print(type(JEZYKI_programowania))

#pierwszy_zbior = str("warszawa","krakiw","lodz")
#drugi_zbior = str("poznan","warszawa")
#
#print(pierwszy_zbior)
#print(drugi_zbior)
#
#print(pierwszy_zbior | drugi_zbior)


#dziennik = {1:"kowalski",2:"nowak",3:"lewandowski",4:"kosinski"}
#print(dziennik)
#
#dziennik[5]="mucha"
#print(dziennik[5])
#
#for key in dziennik.keys():
#    print(key)
#    
#for value in dziennik.values():
#    print(value)
#    
#del dziennik[3]
#
#print("------------------------------")
#
#for key in dziennik.keys():
#    print(key)
#    
#print("-------------------------")
#
#for value in dziennik.values():
#    print(value)
#
#dziennik[2] ="nowy uczen"
#print("nowy uczen to " + dziennik[2])

#for x in range(0,5,1):
#    print(x)



#def funkcja(a,d,f):
#    a-=2
#    for a in range(a,d,f):
#        a+=f
#        print(a)
#        
#funkcja(6,12,2)        
    


#def maximum(x,y):
#    if x>y:
#        return x
#    else:
#        return y
#print maximum(646,4141461)



#for a in range(1,8,1):
#    if a==5:
#        print("Znalazlem 5!")
#    else:
#        print(a)

#a=[1,2,3]
#for x in (a):
#    for y in 'abc':
#         print(x,y)
      
#lista = ["AA","BBB","CCCC","DDDDD"]
#for a in lista:
#   print(a)
#else:
#   print("lista sie skonczyla")
    
#for z in range(1,21,1):
#    if z % 3==0:
#      print(z)
#    else:
#     print('')

#x=4
#while(x <9):
#    print(x)
#    x = x+1
#
#
#
#def ciag(x,y):
#    while(x <y):
#        print(x)
#        x = x+1
#
#ciag(1,15) 

#def gg(a,b):
#    while a<=b:
#        print(a)
#        a+=1
#    else:
#        ("start")
#gg(12,23)
#
#
#lista1 = ["KKKK", "GGGG", "HHHH"]
#lista2 = ["563-12", "363-AB"]
#
#for z in lista1:
#    for b in lista2:
#        print(z + " " + b)
#    print("---------")    

#a = (raw_input("Prosze o napisanie litery n lub c "))
#if a=="n" or a=="c":
#    print("Dziekuje")
#else:
#    print("wpisales niepoprawna litere")
    
#a = [17,21,18]
#b = "kolejna zmienna"
#d="AAA"
#
#for c in a:
#    print(c)
#    print(b)
#    print(d)

#a=[17,21,18]
#b=["Adrian","Paula"]
#
#for i in a:
#    print(i)
#    for j in b:
#        print(j)

#podsumowanie = 1
#for a in range(3):
#    print("wprowadz wartosc:")
#    b = raw_input()
#    b = int(b)
#    podsumowanie +=b
#print("suma wynikowto:" , podsumowanie)

#R = [["CA","NV","UT"],["NJ","NY","DE"]]
#for a in R:
#     for b in a:
#        print(b)

#suma_liczb = 0
#for a in range(5):
#        nowa_wartosc = int(raw_input("Wprowadz dowolna liczbę od 1 do 10:  "))
#        if nowa_wartosc == 5:
#            suma_liczb = suma_liczb +1
#        
#print("Uzytkownik wybral",suma_liczb,"razy liczbe 5.")
#
#lista = 0
#
#for a in range(0,4,1):
#    nowa_wartosc=int(raw_input("wprowadz liczbe od 1 do 10:  "))
#    if nowa_wartosc==4 and nowa_wartosc==3:
#        lista = lista +1
#print("uzytkownik wybral", lista)


for a in range(0,10,1):
    print(a*"*")
    



    






