import random
import time

class Controller():

    def __init__(self,tv_status="OFF",tv_sound=0,channle_list=["CNN"],channel="CNN"):
        self.tv_status=tv_status
        self.tv_sound=tv_sound
        self.channel_list=channle_list
        self.channel=channel

    def power_on(self):

        if self.tv_status=="ON":
            print("TV already ON...")
        else:
            print("TV Turns ON")
            self.tv_status="ON"

    def power_off(self):

        if self.tv_status=="OFF":
            print("TV already OFF...")
        else:
            print("TV Turns OFF")
            self.tv_status="OFF"
    def sound_settings(self):

        while True:
            answer=input("Turn down the volume '<'\nTurn up the volume '>'\nExit 'q': ")
            if answer=="<":
                if self.tv_sound !=0:
                    self.tv_sound -=1
                    print("Sound: ",self.tv_sound)
            elif answer==">":
                if self.tv_sound !=32:
                    self.tv_sound+=1
                    print("Sound: ",self.tv_sound)
            else:
                print("Sound updated...:",self.tv_sound)
                break

    def add_channel(self,channel_name):

        print("Channel adding...")
        time.sleep(1)

        self.channel_list.append(channel_name)

        print("Channel added success...")

    def random_channel(self):
        random_=random.randint(0,len(self.channel_list)-1)

        self.channel=self.channel_list[random_]

        print("Current channel: ",self.channel)

    #============================ special functions ============================

    def __len__(self):

        return len(self.channel_list)

    def __str__(self):
        #self,tv_status="OFF",tv_sound=0,channle_list=["CNN"],channel="CNN"

        return "TV Status: {}\nTV Sound: {}\nCurrent Channel:{}\nChannel List: {}\n".format(self.tv_status,self.tv_sound,self.channel,self.channel_list)


controller=Controller()

print("""
TV App

1. TV ON

2. TV OFF

3. SOUND SETTINGS

4. ADD CHANNEL

5. CHANNEL NUMBER

6. RANDOM CHANNEL CHANGE

7. TV INFORMATION

FOR EXIT ENTER 'q'
""")

while True:
    process=input("Enter process: ")

    if process=="q":

        print("Porcess ending...")
        break

    elif process=="1":

        controller.power_on()
    elif process=="2":

        controller.power_off()
    elif process=="3":
        controller.sound_settings()

    elif process=="4":

        channel_names=input("Enter Channel names',': ")

        channel_list=channel_names.split(",")

        for adding in channel_list:
            controller.add_channel(adding)
    elif process=="5":
        print("Channels: ",len(controller))

    elif process=="6":
        controller.random_channel()
    elif process=="7":
        print(controller)

    else:
        print("Incorrect process")


#======================================