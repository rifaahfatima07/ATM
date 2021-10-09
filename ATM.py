data = [['Tisha', 'abc123', 2000],
         ['Fizur', 'xyz456', 2300],
         ['Adeeba', 'rif245', 3000],
         ['Olivia', 'ish980', 5300]]


def CheckBalance():
    id = input('Plaese enter your id')
    for v in data:
        if v[1] == id:
            print('Your balance is'+str(v[2]))
            

def CashWidraw():
    car = input('Please enter your id!')
    van = int (input('Enter the amount you want to widraw'))
    for v in data:
        if v[1] == car:
            f = v[2]-van
            print('Your current balance is' +str(f))


def CashDeposit():
    bus = input('Please enter your ID!')
    truck = int (input('Enter the amount you want to deposit!'))
    for v in data:
        if v[1] == bus:
            g = v[2] + truck
            print('Your Current Amount is' + str(g))


#CheckBalance()
#CashWidraw()
CashDeposit()


