# -------- bank ------------
class Bank :
    def __init__(self, name):
        self.name = name
        self.balance = 9000000
        self.given_loan = 0
        self.users = []
        self.admins = []
        self.bankrupt = False
        self.loan_feature = True
 
    def add_user(self, user):
        user.account_no = len(self.users) + 100 
        self.users.append(user)

    def login_user(self, name, passward):
        for i in self.users :
            if(i.name == name and i.passward == passward):
                return i 

    def add_admin(self, admin):
        self.admins.append(admin)

    def login_admin(self, name, passward):
        for i in self.admins :
            if(i.name == name and i.get_passward == passward):
                return i 
            

# ---------- user ------------- 

from datetime import datetime

class User :
    def __init__(self, name, email, address, account_type, passward, bank):
        self.account_no = None
        self.name = name 
        self.email = email
        self.address = address
        self.account_type = account_type
        self.passward = passward
        self.bank = bank
        self.balance = 0
        self.loan = 0
        self.taken_loan = 0
        self.transaction_history = []

    def diposit(self, amount): # provide a bank object
        self.balance += amount
        # add the amount to the bank's balance 
        self.bank.balance += amount

        self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Diposit . Amount : {amount} . Balance : {self.balance} .")

    def withdraw(self, amount): # provide a bank object
        if(amount > self.balance):
            print("Withdrawal amount exceeded")
        elif(self.bank.bankrupt):
            print("The bank is bankrupt")
        else :
            self.balance -= amount
            self.bank.balance -= amount

            
            print(f"Congrats !!! Your Withdraw of {amount} Taka is Successfull .")
            
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Withdraw . Amount : {amount} . Balance : {self.balance} .")
    
    def check_balance(self):
        print(f"Your Available Balance is = {self.balance}\n")
    
    def check_transaction_history(self):
        for i in self.transaction_history :
            print(i)
        print("")
    
    def take_loan(self, amount):
        if(self.taken_loan >= 2):
            print("Sorry!! Your loan taking limit is exited .")
        elif self.bank.loan_feature != True :
            print("Sorry !! The Loan Feature of the bank is off now .")
        elif self.bank.bankrupt == True :
            print("The bank is bankrupt")
        else :
            self.balance += amount
            self.bank.balance -= amount
            self.bank.given_loan += amount
            self.taken_loan += 1
            
            
            print(f"Congrats !!! You have successfully taken a loan of {amount} Taka .")
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Loan Taken . Amount : {amount} . Balance : {self.balance} .")

    def transfer(self, account_no, amount):
        if(self.balance < amount):
            print("Sorry !! Insuficient Balance ")
            return
        
        ac = None
        for i in self.bank.users :
            if(i.account_no == account_no):
                ac = i
                break
        
        if ac == None :
            print("Account does not exist")
        else :
            self.balance -= amount
            ac.balance += amount

            
            print(f"Congrats !!! You have successfully transfered {amount} Taka .")
            
            self.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Transfered to {ac.name} . Amount : {amount} . Balance : {self.balance} .")

            ac.transaction_history.append(f"Transaction Time : {datetime.now()} . Transaction Type : Recived money from {self.name} . Amount : {amount} . Balance : {self.balance} .")


# ---------- Admin -------------- 
class Admin:
    def __init__(self, name, passward, assigned_bank):
        self.name = name 
        self.__passward = passward
        self.bank = assigned_bank

    @property
    def get_passward(self):
        return self.__passward
    
    def delete_user(self, account_no):
        ac = None
        for i in self.bank.users :
            if i.account_no == account_no :
                ac = i
                break 
        
        if ac == None :
            print("Invalid account no .")
        else :
            self.bank.users.remove(i)

    def see_all_users(self):
        for i in self.bank.users :
            print(f"Name : {i.name} . Account No : {i.account_no} . Email : {i.email} . Address : {i.address} . Account type : {i.account_type} .")
        print()
    
    def check_balance(self):
        print(f"The total Available balance of {self.bank.name} is {self.bank.balance}")

    def check_loan(self):
        print(f"The total given loan of the Bank {self.bank.name} is {self.bank.given_loan}")
    
    def loan_feature_on(self):
        self.bank.loan_feature = True
    
    def loan_feature_off(self):
        self.bank.loan_feature = False

    def make_bankrupt(self):
        self.bank.bankrupt = True



# -------- replica system --------------

bd_bank = Bank("Bangladesh Bank")

hijbu = User("Hijbu","hijbu@gmail.com","abcd","current","123",bd_bank)
bd_bank.add_user(hijbu)
hijbu.diposit(1000)

jishan = User("Jishan","jishan@gmail.com","dfad","current","1234",bd_bank)
bd_bank.add_user(jishan)
jishan.diposit(5000)

ad = Admin("admin","123",bd_bank)
bd_bank.add_admin(ad)

while True:
    print()
    print("1. Create an User account")
    print("2. Log in as User")
    print("3. Create an Admin account")
    print("4. Log in as Admin")
    print("5. Exit\n")
    
    c0 = int(input("Enter Your choise : "))

    if c0 == 1 or c0 == 2 :
        usser = None 

        if(c0 == 1) :
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            account_type = input("Enter Your account type : ")
            passward = input("Enter Your Passward : ")

            usser = User(name,email,address,account_type, passward, bd_bank)
            bd_bank.add_user(usser)
            print(f"\nSuccessfully Created an User Account . The Account No is {usser.account_no}")

        else :
            name = input("Enter Your Name : ")
            passward = input("Enter Your Passward : ")
            usser = bd_bank.login_user(name, passward)

            if(usser == None) :
                print("Invalid Name or Passward .")
                continue
            print(f"\nWellcome AS User Name = {usser.name} and AC No = {usser.account_no} .")

        while True :
            print()
            print("1. Diposi Amount")
            print("2. Withdraw Amount")
            print("3. Check Available balance")
            print("4. Check transaction history")
            print("5. Take a loan from the Bank")
            print("6. Transfer amount to another user account")
            print("7. Exit\n")
            
            c1 = int(input("Enter Your choise : "))

            if c1 == 1 :
                amount = int(input("Enter Diposit Amount : "))
                usser.diposit(amount)
                print(f"Congrats !!! Your Diposit of {amount} Taka is Successfull .")
            elif c1 == 2 :
                amount = int(input("Enter Withdraw Amount : "))
                usser.withdraw(amount)
            elif c1 == 3 :
                usser.check_balance()
            elif c1 == 4 :
                usser.check_transaction_history()
            elif c1 == 5 :
                amount = int(input("Enter Loan Amount : "))
                usser.take_loan(amount)
            elif c1 == 6 :
                ac = int(input("Enter Reciver Account Number : "))
                amount = int(input("Enter Transfer Amount : "))
                usser.transfer(ac,amount)
            else:
                break
    elif c0 == 3 or c0 == 4 :
        name = input("Enter your Name : ")
        passward = input("Enter your Passward : ")
        addmin = None
        if c0 == 3 :
            addmin = Admin(name,passward,bd_bank)
            bd_bank.add_admin(addmin)
            print("\nSuccessfully Created an Admin Account .")
        else:
            addmin = bd_bank.login_admin(name, passward)

            if(addmin == None) :
                print("Invalid Name or Passward .")
                continue
            print(f"\nWellcome As Admin = {addmin.name}.")
        
        while True :
            print()
            print("1. Delete any user account ")
            print("2. See all user accounts list")
            print("3. Check the total available balance of the bank")
            print("4. Check the total loan amount of the bank")
            print("5. Turn On the loan feature")
            print("6. Turn Off the loan feature")
            print("7. Exit\n")

            c1 = int(input("Enter Your choise : "))

            if c1 == 1 :
                ac_no = int(input("Enter the Account no to Delete : "))
                ad.delete_user(ac_no)
                print(f"\nSuccessfully Deleted the Account no {ac_no}")
            elif c1 == 2 :
                ad.see_all_users()
            elif c1 == 3 :
                ad.check_balance()
            elif c1 == 4 :
                ad.check_loan()
            elif c1 == 5 :
                ad.loan_feature_on()
                print("\nSuccessfully Turned ON the loan Feature .")
            elif c1 == 6 :
                ad.loan_feature_off()
                print("\nSuccessfully Turned OFF the loan Feature .")
            else:
                break
    else :
        break
