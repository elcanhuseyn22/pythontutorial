class car():
    def __init__(self,model="no info",color="no info",horse_power="no info",cylinder="no info"):
        print("Init function has been used...")

        self.model=model
        self.color=color
        self.horse_power=horse_power
        self.cylinder=cylinder


car1=car("BMW M5 F90","Black","600","V8")

car2=car("BMW M3 F80","Red","300","V6")

print(car1.color)