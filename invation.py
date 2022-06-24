import random

def dict_out(friends_dict):
    for key,value in friends_dict.items():
        print(f'{key} - {value}')

def create_list_of_friends(number_of_friend):
    friends_list = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friend):
        friends_list.append(input())
    return friends_list

def def_new_value(bill, number_of_friend):
    return round(bill/number_of_friend, 2)

def dict_update(friends_dict, new_value):
    for key in friends_dict:
        friends_dict[key] = new_value

def def_lucky_man(friends_list, number_of_friend):
    lucky_man = friends_list[random.randint(0, number_of_friend - 1)]
    print(f'{lucky_man} is the lucky one!')
    return lucky_man

def main():
    number_of_friend = int(input("Enter the number of friends joining (including you):\n"))

    if number_of_friend > 1:
        friends_list = create_list_of_friends(number_of_friend)
        friends_dict = dict.fromkeys(friends_list, 0)
        bill = int(input("Enter the total bill value: "))
        if bill <= 0:
            return print("Too few bill")

        new_value = def_new_value(bill, number_of_friend)
        dict_update(friends_dict, new_value)

        if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == "Yes":
            lucky_man = def_lucky_man(friends_list, number_of_friend)
            new_value = def_new_value(bill, number_of_friend - 1)
            dict_update(friends_dict, new_value)
            friends_dict[lucky_man] = 0
        else:
            print("No one is going to be lucky")
        dict_out(friends_dict)
    else:
        print("No one is joining for the party")

if __name__ == "__main__":
    main()