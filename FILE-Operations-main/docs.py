def bal_hesabla(setir):

    setir=setir[:-1]

    list=setir.split(",")

    ad=list[0]
    bal1=int(list[1])
    bal2=int(list[2])
    bal3=int(list[3])

    semestr_bali=bal1 * (3/10) + bal2 * (3/10) + bal3 * (4/10)

    if semestr_bali>=90:
        herf="AA"
    elif semestr_bali>=85:
        herf="BA"
    elif semestr_bali>=80:
        herf="BB"
    elif semestr_bali>=75:
        herf="CB"
    elif semestr_bali>=70:
        herf="CC"
    elif semestr_bali>=65:
        herf="DC"
    elif semestr_bali>=60:
        herf="DD"
    elif semestr_bali>=55:
        herf="FD"
    else:
        herf="FF"

    return ad+ "------------->"+ herf+"\n"



with open("file.txt","r",encoding="utf-8") as file:
    list=[]
    for i in file:

        list.append(bal_hesabla(i))

    with open("ballar.txt","w",encoding="utf-8") as ballar:

        for i in list:
            ballar.write(i)
