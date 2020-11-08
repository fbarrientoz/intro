#imports
import os
from datetime import datetime, date
# global vars
clear = lambda:os.system('cls')
# functions
def print_menu():
    print('***************')
    print(" Welcome - PyCalc ")
    print('***************')
    print('[1] Add')
    print('[2] Substract')
    print('[3] Multipy')
    print('[4] Divide')
    print('[5] Calculate age')
    print('[x] Exit')
    print('-' * 20)

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    # HW: Phython clear console
    # HW2: Calcule the age... question to the user birthday and calculte
#instructions
opc = ''
while(opc != 'x'):
    cls()
    print_menu()
    opc = input("Please select an option: ")
    if(opc == '1' or opc =='2' or opc =='3' or opc =='4'):
        num1 = float(input("Plese provide Num1: "))
        num2 = float(input("Please provide Num2: "))
        if(opc == '4' and num2 ==0):
            while(num2 ==0):
                print("Error, zero division not alloewd")
                num2 = float(input("Please provide Num2: "))
    elif(opc =='5'):
       print("Your date of birth (dd mm yyyy): ")
       date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

    if(opc == '1'):
        print(num1 + num2)
        input("Press Enter to continue...")
    elif(opc == '2'):
        print(num1 - num2) 
        input("Press Enter to continue...")
    elif(opc == '3'):
        print(num1 * num2) 
        input("Press Enter to continue...")
    elif(opc == '4'):        
        print(num1 / num2)
        input("Press Enter to continue...")
    elif(opc == '5'):                
        age = calculate_age(date_of_birth)
        print(age)
        input("Press Enter to continue...")

    print("Good Bye")
    
