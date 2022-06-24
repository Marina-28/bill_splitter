import random

number_of_friend = int(input("Enter the number of friends joining (including you):\n"))
if number_of_friend <= 0:
    print("No one is joining for the party")
else:
    friends_list = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friend):
        friends_list.append(input())
    friends_dict = dict.fromkeys(friends_list, 0)
    # print(friends_dict)

    bill = int(input("Enter the total bill value: "))
    new_value = round(bill/number_of_friend, 2)
    for key in friends_dict:
        friends_dict[key] = new_value
    # print(friends_dict)

    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == "Yes":
        lucky_man = friends_list[random.randint(0, number_of_friend - 1)]
        print(f'{lucky_man} is the lucky one!')
        new_value = round(bill/(number_of_friend - 1), 2)
        for key in friends_dict:
            if key == lucky_man:
                continue
            friends_dict[key] = new_value
        friends_dict[lucky_man] = 0
    else:
        print("No one is going to be lucky")
    for key in friends_dict:
        print(f'{key} - {friends_dict[key]}')
