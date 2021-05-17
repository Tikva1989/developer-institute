from menu_management_system import *


def load_manager(item, price):
    request = MenuItem.get_by_name(item)
    if request == []:
        item = MenuItem(item, price)
    else:
        item = MenuItem(item, request[0][2])
    return item

def show_user_menu():
    while True:
        menu= '''
        MENU
        (a) Add an item
        (u) Update an Item
        (d) Delete an item
        (v) View the menu
        (x) Exit'''
        print(menu)
        user_select = input("Choose an option  from menu..")
        if user_select in ('x', "X"):
            show_restaurant_menu()
            print("Have a nice day . Goodbye.\n\"")
            break
        if user_select in ('a', 'A'):
            add_item()
        elif user_select in ('d', 'D'):
            remove()
        elif user_select in ('v', 'V'):
            show_restaurant_menu()

def add_item():
    while True:
        input_item= input("Enter a item name:  ")
        if input_item == '':
            print("Empty isn't an option")
            continue
        if MenuItem.get_by_name(input_item) != []:
            print ("Item allready exists!")
            continue
        break
    while True:
        input_price = input("Enter item price:  ")
        try:
            p = int(input_price)
        except:
            continue
        if p < 0:
            continue
        break
    item = load_manager(input_item, p)
    item.save()

def remove():
    while True:
        input_item = ("Enter item to remove:   ")
        if input_item == "":
            print("Item is not exists")
            continue
        if MenuItem.get_by_name(input_item) == []:
                print("Item does not exists!")
                continue
        break
    item = load_manager(input_item, 0)
    item.delete()

def show_restaurant_menu():
    print("\nRestaurant Menu\n===============")
    for id, item, price in MenuItem.all():
          print(item, price)


 show_user_menu()


