number_of_friend = int(input("Enter the number of friends joining (including you):\n"))
if number_of_friend <= 0:
    print("No one is joining for the party")
else:
    friends_list = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friend):
        friends_list.append(input())
    friends_dict = dict.fromkeys(friends_list, 0)
    print(friends_dict)

    bill = int(input("Enter the total bill value: "))
    new_value = round(bill/number_of_friend, 2)
    for key in friends_dict:
        friends_dict[key] = new_value
    print(friends_dict)