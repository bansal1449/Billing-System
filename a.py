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

