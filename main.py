""" Vending Machine,   Aviv Wachman"""


def round_only_up(floater, up_by):
    """Gets a float to round, by how much to round and returns the rounded float only if it's it's smaller"""
    rounded_float = round(floater, up_by)
    if rounded_float < floater:
        return floater
    else:
        return rounded_float


def open_file(fname):
    """Gets a String of file location, opens it and return a list of tuples with the input"""
    input_lst = list()
    if len(fname) < 1:
        fname = '/Users/avivwach/Desktop/input.txt'
    fh = open(fname)
    for line in fh:
        line = line.rstrip().split(" ")
        line_input = (line[0], line[1])
        input_lst.append(line_input)
    return input_lst


def init_machine():
    """Creates a dict of the drinks, tuple of the prices and returns both"""
    bev_dict = {
        "1": "Ness Coffee",
        "2": "Coffee Black",
        "3": "Tea",
        "4": "Hot Chocolate",
        "5": "Soup",
        "6": "Coca-Cola",
        "7": "Orange Juice"
    }
    money_tuple = (2.4, 2.1, 1.6, 2.5, 3.1, 3.3, 3.2)
    return bev_dict, money_tuple


def print_menu(bev_dict, money_tuple):
    """Gets a dict and tuple- prints the menu: number and drink (form dict) , price (from tuple)"""
    print("""         MENU\n        ~~~~~~""")
    for bev_num in bev_dict:
        beverage_name = bev_dict[bev_num]
        print(bev_num + ".   ", beverage_name, money_tuple[int(bev_num) - 1])
    print()


def choose(bev, bev_dict, money_tuple):
    """ Get's the chosen beverage and the a dict and tuple with the prices and name of each drink.
    Returns NIS to pay (if a valid number was chosen) """
    print(f"You entered {bev}")
    if int(bev) not in range(1, 8):
        print("ERROR: no beverage with that number")
        return "NO"
    print(f"You chose {bev_dict[bev]}")
    nis_to_get = money_tuple[int(bev) - 1]
    print(f"Enter {nis_to_get} NIS -->", end='')
    return nis_to_get


def check_num(money):
    """Gets a float and checks how many after it goes.
     If goes more than once after the for, returns true. Else returns true."""
    money = str(money)
    money = money.split('.')
    if len(money) == 1:
        return True
    after_dot_len = len(money[1])
    if after_dot_len > 1:
        print("ERROR- entered coin not in use")
        return False
    return True


def give_back(nis_entered, nis_to_get):
    """Get's the paid amount and the payment required. Returns the excess or the amount needed to add or
     thanks you for using the vending machine"""
    print(f"You entered {nis_entered} NIS")
    if not check_num(nis_entered):
        print(f"You got back {nis_entered} NIS")
        return ""
    excess = round(float(nis_entered) - float(nis_to_get), 2)
    if excess == 0:
        print("Thank you for using my beverage machine")
        return 0
    if excess < 0:
        print("Not Enough Money")
        print("You are missing", abs(excess))
        return ""
    print("Your excess is:", excess)
    return excess


def print_coins(excess):
    """Gets the excess and prints the least amount of coins to return"""
    coins = (20, 10, 5, 2, 1, 0.5, 0.1)
    for coin in coins:
        if coin < excess:
            num_of_coins = int(excess / coin)
            print(num_of_coins, "coins of", coin, "NIS")
            excess = round_only_up(excess - num_of_coins * coin, 5)
    print("Thank you for using my beverage machine")


def main(chosen_bev, entered_money, bev_dict, money_tuple):
    """Gets the chosen bev index(int), money paid(float), dict of bevs and tuple of prices
     return excess or needed money to play or thanks you for using the vending machine"""
    nis_to_get = choose(chosen_bev, bev_dict, money_tuple)
    if isinstance(nis_to_get, str):
        return
    excess = give_back(entered_money, nis_to_get)
    if isinstance(excess, str):
        return
    elif excess != 0:
        print_coins(excess)


if __name__ == '__main__':
    """Prints the menu, goes through the list and runs 'main' """
    BEV_DICT, MONEY_TUPLE = init_machine()
    print_menu(BEV_DICT, MONEY_TUPLE)
    INPUT_LST = open_file("")
    for i in INPUT_LST:
        main(i[0], i[1], BEV_DICT, MONEY_TUPLE)
        print()
