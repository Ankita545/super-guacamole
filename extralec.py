'''
car_timer(240) ➞ 4
# 240 minutes have passed since 00:00, the current time is 04:00
# Digits sum up is 0 + 4 + 0 + 0 = 4

car_timer(808) ➞ 14

car_timer(14) ➞ 5
'''
def cartimer(x):
    print("Given time in minutes: " + str(x))
    #int(y)=x/60
    y=int(x/60)
    z=x%60
    if y<10:
        #print("0"+str(y)+":"+ str(round(z,2)))
        print("0"+str(y)+":"+ '%.2f'%z)
    else:
        print(str(y)+":"+"{:.2f}".format(z)) 
cartimer(240)
#enumerate function
x=['ravi', 'ram', 'vishal', 78, 7.7]
y=enumerate(x,10)
print(type(y))

#tuple unpacking
'''
In a single statement, assigning values of tuple to variables
Assigning variables to tuple values
'''
#split function