item_list = ["Noodles", "Paratha", "Momos",
             "Burger"]  # ["Noodles","Paratha","Momos","Burger"]

price_list = [45, 40, 30, 56]
def menuAsDict():

    admin()
    global menu_As_Dict
    menu_As_Dict = dict(zip(item_list, price_list))


def finalMenu():

    global final_Menu
    final_Menu = dict(zip(item_list, price_list))
    print("\n\n")
    print("                       😋 MENU 😋\n")
    print("                 | Item      Price |")
    for i in range(len(item_list)):
        print("                  ", item_list[i], "  :  ", price_list[i])
    print("\n\n")


def customer():
    #   Menu display

    def menu():
        None

    menu()
    name = input("Customer Name : ")
    contact = int(input("Contact No. "))
    order_list = []
    number_of_items = []

    def menuPrint():
        # Customer information

        #  Data of  dictionary ziping of two list

        finalMenu()

        order = True

        for_exit = 0
        while order:
            a = input("Enter your item : ")
            a = a[0].upper() + a[1:].lower()
            if a != "E" and a != "M":
                order_list.append(a[0].upper() + a[1:].lower())
                b = int(input("Enter number of items : "))
                number_of_items.append(b)
            elif a == "E":
                order = False
                break
            elif a == "M":
                menu()
                menuPrint()
            else:
                print("\n                ❌ Invalid Input ❌\n ")
                menuPrint()

            if for_exit == 0:
                print("Enter E for no more order.")
                print("Enter M for menu.")
            for_exit += 1
       #************
def admin():
    print("""
                👍You can change or add items and price of your items.👍
    """)
    print("       \n    Enter Order for order. \n  ")

    while True:
        item_admin = input("Enter your item : ")
        item_admin = item_admin[0].upper() + item_admin[1:].lower()
        if item_admin == "Order":
            customer()
        elif item_admin == "E":
            quit()
        else:
            new_price = int(input("Price : "))
            item_list.append(item_admin)
            price_list.append(new_price)


admin_custome = input("""You are admin or customer : 
                1.admin
                2.customer    
        Enter here : """)

admin_custome_modified = admin_custome[0].upper() + admin_custome[1:].lower()
if admin_custome_modified == "Customer" or admin_custome_modified == "2":
    customer()
elif admin_custome_modified == "Admin" or admin_custome_modified == "1":

    for i in range(3):
        paasWord = input("Enter your Paasword : ")
        if paasWord == "chitkara@22":
            menuAsDict()
        else:
            print("\n                          ❌❌ Sorry ! Invalid paasword ❌❌\n ")
else:
    print("\n                                    ❌❌ Invalid input ❌❌\n ")
