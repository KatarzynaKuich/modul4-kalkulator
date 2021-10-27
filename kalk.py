import sys

#>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
#Podaj składnik 1. 2.3
#Podaj składnik 2. 5.4
#Dodaję 2.30 i 5.40
#Wynik to 7.70

def Dodawanie (a,b,*args):
    return a + b + sum(int(i) for i in args)
def Odejmowanie(a,b,*args):
    return a - b -sum(int(i) for i in args)
def Mnozenie(a,b,*args):
   return a*b* sum(int(i) for i in args)
def Dzielenie(a,b,*args):
   return a/b/sum(int(i) for i in args)


operacje ={
    1:Dodawanie,
    2:Odejmowanie,
    3:Mnozenie,
    4:Dzielenie
}

operacje_nazwy ={
    "1":"Dodawanie",
    "2":"Odejmowanie",
    "3":"Mnozenie",
    "4":"Dzielenie"
}


liczby={
    "a":"liczba a",
    "b":"liczba b"
}


print("\nPodaj działanie, posługując się odpowiednią liczbą:","\n",operacje_nazwy,"\n oraz minimum 2 liczby : (oddzielajac spacjami)")
# taking multiple inputs at a time separated by space

o,a,b,*args=[(x) for x in input().split()]

print("*args:",*args)

result =operacje[int(o)](float(a),float(b),*args)

print("Wykonane działanie to",operacje_nazwy[o],"liczb:",a,b,*args,"\nWynik:",result)


1

