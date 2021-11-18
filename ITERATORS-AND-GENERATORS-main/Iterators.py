class Pult():

    def __init__(self,list):
        self.list=list
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index<len(self.list):
            return self.list[self.index]
        else:
            self.index=-1
            raise StopIteration

pult=Pult(["atv","ans","lider","aztv","idman az"])


iterator=iter(pult)

"""for i in pult:
    print(i)"""

#----------------------------------------------------
def kvadrat():
    cavab = []

    for i in range(1, 6):
        cavab.append(i ** 2)
    return cavab


def kvadrat_():
    for i in range(1, 6):
        yield i ** 2  # generator


generator = kvadrat()

iterator = iter(generator)  # iterator

iterator2 = iter(generator)


# print(next(iterator2))

def vurma_cedveli():
    for i in range(1, 11):
        for j in range(1, 11):
            yield "{} x {} = {}".format(i, j, i * j)


"""for i in vurma_cedveli():
    print(i)"""


# --------------------------------------------------------------
# exercice iterabel class and fibonacci ceries

class Quvvet():

    def __init__(self, max=0):
        self.max = max
        self.quvvet = 0

    def __iter__(self):  # made this class an iterable class
        return self

    def __next__(self):
        if self.quvvet <= self.max:
            cavab = 3 ** self.quvvet

            self.quvvet += 1
            return cavab
        else:
            self.quvvet = 0
            raise StopIteration


quvvet = Quvvet(6)

iterator3 = iter(quvvet)

"""for i in iterator3:
    print(i)"""


# generator fibonacci

def fibonacci():
    a = 1
    b = 1
    yield a
    yield b

    while True:
        a, b = b, a + b

        yield b


"""for i in fibonacci():
    if i>=100000:
        break
    else:
        print(i)"""

# -------------------task-------------------

"""
Kareler isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. 
Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde 
 ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. 
StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""


class Kareler():

    def __init__(self, maksimum):
        self.maksimum = maksimum

        self.sayi = 1

    def __iter__(self):
        return self

    def __next__(self):

        if (self.sayi <= self.maksimum):

            sonuc = self.sayi ** 2
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration


kare = Kareler(5)

iterator4 = iter(kare)

"""for i in iterator4:
    print(i)
"""


# 1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.
def asal_mi(sayi):
    i = 2

    while i < sayi:
        if (sayi % i == 0):
            return False
        i += 1
    return True


def asal_generator():
    i = 2
    while True:
        if (asal_mi(i)):
            yield i
        i += 1


"""for sayi in asal_generator():
    if (sayi > 1000):
        break
    print(sayi)"""