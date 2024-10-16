class BankAccount:
    
    def __init__(self):
        self.__balance = 0
        
    def deposite(self,amount):
        self.__balance = amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Apka balance nakafi hai!")
            
    def getter(self):
        print("Your balance is: ", self.__balance)
    
A1 = BankAccount()
# A1.deposite(300)
# A1.withdraw(200)
A1.getter()


A2 = BankAccount()
# A2.deposite(2000)
# A2.withdraw(200)
#A2.getter()

A3 = BankAccount()
# A3.deposite(230)
# A3.withdraw(20)
# #A3.getter()

list = [A1,A2,A3]
print('length before: ', len(list))
# list.append(A4= BankAccount()) # append takes no keyword arguments
print('length after ', len(list)) 

# i = 1
# for ls in list:
#     ls.deposite(float(input(f"deposite amount for user_{i}: ")))
#     ls.withdraw(float(input(f"withdraw amount for user_{i}: ")))
#     print(ls.getter())
#     i = i+1

#print(list)
# def main():
    
#     query = int(input("Enter 1 for deposite 2 for withdrawal 3 for status: "))
    
    
#     if query == 1:
#         amount = float(input("Please enter the amount: "))
#         A1.deposite(amount)
#         print(A1.getter())
#     elif query == 2:
#         amount = float(input("Please enter the amount: "))
#         A1.withdraw(amount)
#         print(A1.getter())
#     elif query == 3:
#         A1.getter()


#main()
# bool = True
# while bool == True:
#     main()
#     q = int(input("press 0 to end program: "))
#     if q == 0:
#         bool = False
#     else:
#         bool = True
    
    
    