""" Vending Machine,   Aviv Wachman"""


def round_only_up(floater, up_by):
    rounded_float = round(floater, up_by)
    if rounded_float < floater:
        return floater
    else:
        return rounded_float


def open_file(fname):
    input_lst = list()
    if len(fname) < 1:
        fname = 'input.txt'
    fh = open(fname)
    for line in fh:
        line = line.rstrip().split(" ")
        line_input = (line[0], line[1])
        input_lst.append(line_input)
    return input_lst


def init_machine():
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
    print("""         MENU\n        ~~~~~~""")
    for bev_num in bev_dict:
        beverage_name = bev_dict[bev_num]
        print(bev_num + ".   ", beverage_name, money_tuple[int(bev_num) - 1])
    print()


def choose(bev, bev_dict, money_tuple):
    print(f"You entered {bev}")
    if int(bev) not in range(1, 8):
        print("ERROR: no beverage with that number")
        return "NO"
    print(f"You chose {bev_dict[bev]}")
    nis_to_get = money_tuple[int(bev) - 1]
    print(f"Enter {nis_to_get} NIS -->", end='')
    return nis_to_get


def give_back(nis_entered, nis_to_get):
    print(f"You entered {nis_entered}")
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
    coins = (20, 10, 5, 2, 1, 0.5, 0.1)
    for coin in coins:
        if coin < excess:
            num_of_coins = int(excess / coin)
            print(num_of_coins, "coins of", coin, "NIS")
            excess = round_only_up(excess - num_of_coins * coin, 5)
    print("Thank you for using my beverage machine")


def main(bev_dict, entered_money):
    NIS_to_get = choose(bev_dict, BEV_DICT, MONEY_TUPLE)
    if isinstance(NIS_to_get, str):
        return
    EXCESS = give_back(entered_money, NIS_to_get)
    if isinstance(EXCESS, str):
        return
    elif EXCESS != 0:
        print_coins(EXCESS)


if __name__ == '__main__':
    BEV_DICT, MONEY_TUPLE = init_machine()
    print_menu(BEV_DICT, MONEY_TUPLE)
    INPUT_LST = open_file("")
    for i in INPUT_LST:
        main(i[0], i[1])
        print()


