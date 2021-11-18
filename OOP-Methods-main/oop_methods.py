class Book():

    def __init__(self,name,author,nmb_of_pages,type):
        print("init function")
        self.name=name
        self.author=author
        self.number=nmb_of_pages #new
        self.type=type
    def __str__(self):
        return "Name: {}\nAothor: {}\nNumber of pages: {}\nType: {}".format(self.name,self.author,self.number,self.type)

    def __len__(self):
        return self.number

    def __del__(self):
        print("Book object has been deleted")


book=Book("Car","Eljan",333,"crminal") #__init__ method
del book
#print(book) #__str__ method