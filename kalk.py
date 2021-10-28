import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

#>> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
#Podaj składnik 1. 2.3
#Podaj składnik 2. 5.4
#Dodaję 2.30 i 5.40
#Wynik to 7.70

def isnumeric(x):
    # zwraca True jesli jest numeric
    return all(i in "0123456789.+-" for i in x) and any(i in "0123456789" for i in x)

def Dodawanie (a,b,*args):
    return a + b + sum(float(i) for i in args)
def Odejmowanie(a,b,*args):
    return a - b -sum(float(i) for i in args)
def Mnozenie(a,b,*args):
   return a*b* sum(float(i) for i in args)
def Dzielenie(a,b,*args):
       #dzielenie przez 0 niedozwolone wyjdz
        try:
         return a/b/sum(int(i) for i in args)
        except ZeroDivisionError as err:
         print('Dzielenie przez 0 niedozwolone:', err)
         exit(1)
  
 
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



print("\nPodaj działanie, posługując się odpowiednią liczbą:","\n",operacje_nazwy,"\n oraz minimum 2 liczby : (oddzielajac spacjami)")
#sprawdz czy sa przynajmniej 3 liczby jak nie ma to wyjdz
count=0
tekst = input().split()
for x in tekst:
    if isnumeric(x):
        count=count+1
        

if count <3 :
   print("za malo podales wartosci liczbowych")
   exit(1)
else:
    # taking multiple inputs at a time separated by space
    o,a,b,*args=[x for x in tekst if isnumeric(x)]
    #sprawdz czy 1 argument jest liczba calkowita z listy 1 do 4
    if not int(o) in [1,2,3,4]:
        print("Nie wybrales działania z zakresu 1 -4")
        exit(1)

logging.debug("operacje")

result =float(operacje[int(o)](float(a),float(b),*args))

print("Wykonane działanie to",operacje_nazwy[o],"liczb:",a,b,*args,"\nWynik:",result)
