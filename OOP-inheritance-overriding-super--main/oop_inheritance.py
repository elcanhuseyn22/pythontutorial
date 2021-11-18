class Employeer():

    def __init__(self,name,salary,department):
        print("Employeer self has been used...")
        self.name=name
        self.salary=salary
        self.department=department
#=============================================
    def show_info(self):
        print("Employeer's Data...")
        print("""
        Name: {}
        Salary: {}
        Department: {}
        """.format(self.name,self.salary,self.department))
# =========================================================
    def change_department(self,new_department):
        self.department=new_department


class Employer(Employeer): #inheritance

    def __init__(self,name,salary,department,c_): #overriding
        super().__init__(name, salary, department)  # super()
        print("EmployEr self has been used...")

        self.count=c_
    def show_info(self):  #overriding
        print("EmployEr's Data...")
        print("""
        Name: {}
        Salary: {}
        Department: {}
        Cout: {}
        """.format(self.name,self.salary,self.department,self.count))

    def extra(self,quantity):
        self.salary+=quantity


employer=Employer("Eljan",2000,"Human Resources",15)

employer.show_info()