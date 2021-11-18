try:
    a=int(input("a: "))
    b=int(input("b: "))
    c=int(a/b)
    print(c)
except (ValueError,ZeroDivisionError):
    print("Error!")
finally:
    print("test") #mutleq isleyir

#-------------------rise--------------

def ters_cevir(a):
    if type!=str:
        raise ValueError("Please enter string...")
    else:

        return (a[::1])

try:
    print(ters_cevir(12))
except ValueError:
    print("Error")