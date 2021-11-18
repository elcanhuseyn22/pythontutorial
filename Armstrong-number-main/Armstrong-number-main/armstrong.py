number=input('Enter a number: ')
sum=0
for i in number:
    sum+=int(i)**len(number)
if sum==int(number):
    print("Amstrong number..")
else:
    print("Is NOT amstrong number")