def topla(a,b):
    return a+b
def vur(a,b):
    return a*b
def cix(a,b):
    return a-b
def bol(a,b):
    return a/b

def main_function(func1,func2,func3,func4,islem_adi):
    if islem_adi=="topla":
        print(func1(3,4))
    elif islem_adi=="vur":
        print(func2(3,4))
    elif islem_adi=="cix":
        print(func3(3,4))
    else:
        print(func4(3,4))
#main_function(topla,vur,cix,bol,"vur")


import time

def zaman(func):

    def wrapper(reqemler):
        baslama=time.time()

        cavab=func(reqemler)

        bitis=time.time()

        print(func.__name__ + " "+str(bitis-baslama)+" saniye cekdi.")

        return cavab
    return wrapper

@zaman
def kvadart(edeler):
    cavab=list()
    for i in edeler:
        cavab.append(i**2)

    return cavab
@zaman
def kub(edeler):
    cavab=list()
    for i in edeler:
        cavab.append(i**3)
    return cavab

#kvadart(range(100000))
#kub(range(100000))

#---------------------------------------------
def ekstra(funksiya):

    def wrapper(ededler):
        cutler_cemi=0
        cut_ededler=0
        tekler_cemi=0
        tek_ededler=0

        for reqem in ededler:

            if reqem%2==0:
                cutler_cemi+=reqem
                cut_ededler+=1
            else:
                tekler_cemi+=reqem
                tek_ededler+=1
        print("Teklerin ortalamasi: ",tekler_cemi/tek_ededler)
        print("Cutlerin ortalamasi: ",cutler_cemi/cut_ededler)

        funksiya(ededler)
    return wrapper

@ekstra
def ededi_orta(ededler):

    cem=0

    for reqem in ededler:
        cem+=reqem
    print("Ededi orta: ",cem/len(ededler))

#ededi_orta([1,2,3,4,5,12,23,4,22,65,73,78,98])

#=====================================================

#1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın.

def ekstra1(funksiya):

    def ekstra_ozelliy():
        print("Mukemmel sayilar")
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i +=1
            if (toplam == sayi):
                print(sayi)
        funksiya()
    return ekstra_ozelliy
@ekstra1
def sade_ededler():

    print("Sade ededler")
    for eded in range(2,1001):
        i=2
        say=0
        while i<eded:
            if eded%i==0:
                say+=1
            i+=1
        if say==0:
            print(eded)
sade_ededler()