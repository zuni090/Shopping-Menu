import os.path

class Costumer:  # this class contains all the informations about the costomer of shop#
    cos_name = " "
    cos_cell = " "
    amount_paid = 0
    amount_get_back = 0

    def __init__(self):
        pass

    def get_user_details(self):
        print("GETTING COSTUMER'S DETAILS\n")
        self.cos_name = str(input("Enter your Name : "))
        self.cos_cell = str(input("Enter Your cell # : "))

    def print_cos(self):
        print("NAME YOUR NAME : " + str(self.cos_name))
        print("CELL # : " + str(self.cos_cell))
        

    def paying(self):
        self.amount_paid = int(input("Enter amount costumer Paid : $"))

    def returnned(self):
        print("Amount returned : $" +str(self.amount_get_back))


class User:  # this class contains all the informations about the shop admin#
    id_name = "admin"
    id_pass = "12345"

    item_names = ["Corn", "Apple", "Cookies", "Maggie", "Milk", "Candies", "Cream", "Snacks", "Drinks", "Mangoes"]
    item_price = [20, 15, 30, 50, 100, 40, 90, 45, 80, 25]
    total_item = 10

    def display_available_items(self):
        print("ITEM NAME\t\t\tPrice($)")
        print("==================================")
        for i in range(len(self.item_names)):
            print(str(self.item_names[i]) + "\t\t\t\t" + str(self.item_price[i]) + "$")

    def get_user_detail(self):
        print("\nAdmin Login details ...\n===================\n")
        self.id_name = str(input("Enter ID-Name : "))
        self.id_pass = str(input("Enter Password : "))
        while (True):
            if self.id_name == "admin" and self.id_pass == "12345":
                #  self.crud()
                return True
                break

            else:
                print("Wrong ID or Password\nTry Again")
                self.get_user_detail()

    def add_item_to_shop(self):
        name = str(input("Enter Name of item you want to add : "))
        price = int(input("Enter the price of that item $:"))
        self.item_names.append(name)
        self.item_price.append(price)
        self.total_item += 1
        print("Item added successfully..!")

    def remove_from_shop(self):
        name = str(input("Enter name of item you want to remove : "))
        for i in range(len(self.item_names) - 1):
            if self.item_names[i] == name:
                del (self.item_names[i])
                self.total_item -= 1
                print("Item removed successfully")

    def admin_choice(self):
        print("\t\t\tADMIN PORTAL\n\t\t\t============\n")
        print("\t[1]. Display all items\n\t[2].Add more\n\t[3].Remove Item\n\t[4].Back-->")
        choice = int(input("SELECT WHAT YOU WANT TO DO ? "))
        if choice == 1:
            self.display_available_items()
            y = str(input("press Y or y to continue ..."))
            if y == "Y" or "y":
                self.admin_choice()

        elif choice == 2:
            self.add_item_to_shop()
            y = str(input("press Y or y to continue ..."))
            if y == "Y" or "y":
                self.admin_choice()

        elif choice == 3:
            self.remove_from_shop()
            y = str(input("press Y or y to continue ..."))
            if y == "Y" or "y":
                self.admin_choice()

    def admin_side(self):
        x = False
        x = self.get_user_detail()
        if x == True:
            self.admin_choice()


class Shop(Costumer,User):  # this class contains the actual data and informations about shop#
    itemQuantity = 0
    itemPrice = 0
    itemName = " "
    num = 0
    total = 0
    items = []
    Qty = []
    tot = []
    price = []
    amount_rec = 0
    amount_returned = 0

    # composition of classes
    # --------------------#
    admin = User()
    costumer = Costumer()

    # --------------------#

    def __init__(self):
        pass

    def intro(self): 
        print(
            "\n\t\tWELCOME TO OUR SHOP \U0001F600 \n\t\t\n\t\t  HUNGER SOLUTION \U0001F637 \n\t\t---------------------\n\t\t ..we serve you..! \U0001F917 \n\t\t----------------------\n\nAddress : xyz road , Block abc , Khi\nContact # : +9232-shop(2122)\n\n")

    def interface(self):  # this is the method in which the program has two interface one is admin and the other is costumer#
        self.intro()
        abc = int(input("SELECT YOU SIDE :\n================\n\n[1]. ADMIN\n[2]. COSTUMER\n[3]. EXIT\nType here ... "))
        if abc == 1:
            self.admin.admin_side()
            y = str(input("Press Y to continue .."))
            if y == "Y" or "y":
                self.interface()
        elif abc == 2:
            self.costumer_side()
            y = str(input("Press Y to continue .."))
            if y == "Y" or "y":
                self.interface()
        elif abc == 3:
            print("EXITING PROGRAM>> THANK YOU ...!")
            for i in range(9):
                print("\U0001F917 ", end=' ')
            exit(1)

    def costumer_side(self):
        self.costumer.get_user_details()
        self.costumer_choice()

    def billing_process(self):
        self.paying()
        self.receiving_amount()
        self.returning_amount()
        self.returning_amount()

    def print_bill(self):
        print("WELCOME TO OUR SHOPPING MART\n============================\n")
        print("Costumer Name : " + str(self.cos_name))
        print("Costumer cell : " + str(self.cos_cell))
        print("\n\t\tTOTAL BILL\n\t\t==========\n")
        print("Item Name\t\tQuanitity\tPrice($)_each")
        print("=====================================\n")
        for i in range(self.num):
            print(str(self.items[i]) + "\t\t\t   " + str(self.Qty[i]) + "\t\t    " + "$" + str(self.price[i]))

        for i in range(len(self.tot)):
            self.total += self.tot[i]
        print("GST IS OF 5%\n")
        print("Amount due : $" + str(self.total))
        self.receiving_amount()
        print("Costumer Paid : $" + str(self.amount_rec))
        if self.amount_rec < self.total:
            print("Please give $" + str((self.total - self.amount_rec)) + " amount more ...")
            self.paying()
        else:
            print("Amount returned : $", abs(self.amount_rec - self.total - self.total * 0.05))
            print("===========================================")
            print("TOTAL Amount after GST of 5% : " + str(self.total + (self.total * 0.05)) + "\n   THANK YOU!\n   HAVE A NICE DAY!!.")

    def receiving_amount(self):
        self.paying()
        self.amount_rec = self.amount_paid

    def returning_amount(self):
        self.amount_returned = self.total - self.amount_rec - self.total * 0.05
        self.amount_get_back = self.amount_returned

    def add_item(self):
        self.items.append(self.itemName)
        self.price.append(self.itemPrice)
        self.Qty.append(self.itemQuantity)
        self.tot.append(self.itemPrice * self.itemQuantity)

    def selection(self):
        print("\nSHOWING COSTUMER PRICE OF ITEMS\n\n")
        self.admin.display_available_items()
        for i in range(self.num):
            print("\nITEM NUMBER " + str(i + 1) + " : ")
            self.itemName = input("Enter Item name : ")
            self.itemPrice = int(input("Enter item price : $"))
            if self.itemName in self.admin.item_names:
                self.itemQuantity = int(input("Enter item quantity : "))
                self.add_item()

            else:
                print("ITEM NOT AVAILABLE!")

    def number(self):
        print("Item Numbers:")
        self.num = int(input("Enter no of item you want:"))

    def display(self):
        for i in range(len(self.items)):
            if i < self.num:
                print("ITEM # " + str(i + 1) + " : ")
                print("NAME : " + self.items[i])
                print("QUANTITY : " + str(self.Qty[i]))

    def remove_item(self):
        dumy = str(input("Enter Name of item you want to remove from list : "))
        for i in range(len(self.items) - 1):
            if str(self.items[i]) == str(dumy):
                del (self.items[i])
                del (self.Qty[i])
                print("Item removed successfully!")
                self.num -= 1

    def costumer_choice(self):
        print("\n\nWELCOME TO OUR SHOPPING CART \n============================\n")
        print(
            "[1]. Purchase Available Products \n[2]. Remove Item from list \n[3]. Display list Items \n[4]. Print Bill\n[5]. EXIT\n\n")
        value = int(input("SELECT WHAT YOU WANT TO DO ?"))
        if value == 1:
            self.number()
            self.selection()
            y = str(input("Press Y to continue .."))
            if y == "Y" or "y":
                self.costumer_choice()

        elif value == 2:
            if self.num == 0:
                print("Can't delete data because list is empty")
                self.costumer_choice()
            else:
                self.remove_item()
                y = str(input("Press Y to continue .."))
                if y == "Y" or "y":
                    self.costumer_choice()

        elif value == 3:
            self.display_available_items()
            y = str(input("Press Y to continue .."))
            if y == "Y" or "y":
                self.costumer_choice()

        elif value == 4:
            self.print_bill()
            y = str(input("Press Y to continue .."))
            if y == "Y" or "y":
                self.costumer_choice()


class UserLogin:
    createLogin = ""
    createPassw = ""
    login = ""
    passw = ""

    def displayMenu(self):
        if not os.path.exists("UserInfo.txt"):
            createFile = open("UserInfo.txt","w+")
        status = input("Do You Have A Account? yes/no? ")
        if status == "yes":
            self.oldUser()
        elif status == "no":
            self.newUser()

    def newUser(self):
        f=open("UserInfo.txt","a+")
        read = open("UserInfo.txt","r")
        createLogin = str (input("Create login name: "))
        UserData = read.read() 
        if createLogin in UserData:
            print ("Login name already exist!")
        else:
            createPassw = input("Create password: ")
            f.write(createLogin)
            f.write(createPassw)
            print("User created!")
            

        f.close()
    def oldUser(self):
        login = input("Enter login name: ")
        passw = str(input("Enter Your Password: "))
        read = open("UserInfo.txt","r")
        f=open("UserInfo.txt","a+")
        UserData = read.read() 
        if login and str(passw) in UserData :
            print ("Login successful!")
        else:
            print ("User doesn't exist or wrong password")
        f.close()


mainCls = UserLogin()
mainCls.displayMenu()
obj = Shop()
obj.interface()


