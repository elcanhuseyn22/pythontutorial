def club(list):
    list=list[:-1]
    a=list.split(",")
    name=a[0]
    club=a[1]
    return [name,club]
with open("footballplayers.txt","r",encoding="utf-8") as file:
    list=[]
    for i in file:
        list.append(club(i))
    for i,j in list:
        if j=="Bayern":
            with open("bayern.txt","a",encoding="utf-8") as bayern:
                bayern.write(i+"\n")
        elif j=="Barcelona":
            with open("barcelona.txt","a",encoding="utf-8") as barcelona:
                barcelona.write(i+"\n")
        elif j=="PSG":
            with open("psg.txt","a",encoding="utf-8") as psg:
                psg.write(i+"\n")