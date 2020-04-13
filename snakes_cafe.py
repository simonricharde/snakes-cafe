from textwrap import dedent

welcome_message = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

order_message = """
***********************************
** What would you like to order? **
***********************************
"""

NA_message = """
***********************************
** This item does not exist. Please enter a valid item from the menu **
***********************************
"""

menu_list = {
    "Appetizers": {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0
    },
    "Entrees": {
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0
    },
    "Desserts": {
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0
    },
    "Drinks": {
        "Coffee": 0,
        "Tea": 0,
        "Soda": 0
    },
}


def print_menu():
    for menu in menu_list:
        print(dedent(f"""
        {menu}
        ****************
        """))
        for key, value in menu_list[menu].items():
            print(key)


def process_menu(menu_order):     
    flag = False
    for menu in menu_list:
        current_menu = menu_list[menu]
        menu_order = menu_order.title() 
        if menu_order in current_menu.keys():
            quantity = current_menu[menu_order]
            quantity += 1
            current_menu[menu_order] = quantity
            print(f"Item ordered {menu_order} with quantity {quantity}")
            flag = True
            return flag      

if __name__ == '__main__':
    print(welcome_message)
    print_menu()
    input_value = input(order_message)
    while input_value != "quit":
        flag = process_menu(input_value)
        if(flag):
            input_value = input(order_message)
        else:
            print(NA_message)
            input_value = input(order_message)

