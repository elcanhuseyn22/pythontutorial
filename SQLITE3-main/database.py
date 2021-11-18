import sqlite3

con=sqlite3.connect("lib.db") #CONNECT WITH TABLE.

cursor=con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS book (name TEXT,author TEXT,publisher TEXT,page_number INT)")
    con.commit()

def add_data1():
    cursor.execute("INSERT INTO book VALUES('American Marxism','Mark R. Levin','Threshold Editions',320)")
    con.commit()
#-------------------------------------
def add_data2(name,author,publisher,page_number):
    cursor.execute("INSERT INTO book VALUES(?,?,?,?)",(name,author,publisher,page_number))
    con.commit()

"""name=input("Enter book name: ")
author=input("Enter Aunthor: ")
publisher=input("Enter Publisher: ")
page_number=int(input("Enter Page Number: "))

add_data2(name,author,publisher,page_number)"""
#-------------------------------------
def get_data1():
    cursor.execute("SELECT * FROM book")
    lst=cursor.fetchall()

    for i in lst:
        name=i[0]
        author=i[1]
        publisher=i[2]
        page_number=i[3]
        print("Name: {}\nAuthor: {}\nPublisher: {},\nPage Number: {}".format(name,author,publisher,page_number))
        print("****************")
    
#-------------------------------------

def get_data2():
    cursor.execute("SELECT name,author from book")
    lst=cursor.fetchall()
    for i in lst:
        name=i[0]
        author=i[1]
        print("Name: {}\nAuthor: {}".format(name,author))
        print("*************")

#-------------------------------------

def get_data3(publisher):
    cursor.execute("SELECT * FROM book WHERE publisher=?",(publisher,))  #publisher,
    lst=cursor.fetchall()
    for i in lst:
        name=i[0]
        author=i[1]
        publisher=i[2]
        page_number=i[3]
        print("Name: {}\nAuthor: {}\nPublisher: {},\nPage Number: {}".format(name,author,publisher,page_number))
        print("****************")

#get_data3("Hardcover")

#-------------------------------------

def update_data(old_pulisher,new_publisher):
    
    cursor.execute("UPDATE book SET publisher=? WHERE publisher=?",(new_publisher,old_pulisher))
    con.commit()

#update_data("Hardcover","East West")
    
#-------------------------------------

def delete_data(author):
    cursor.execute("DELETE FROM book WHERE author=?",(author,))

#delete_data("Taylor Jenkins Reid")

#-------------------------------------

con.close() # Bağlantıyı koparıyoruz.
