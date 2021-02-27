import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def name_prompt():
    name = input("Please enter hospital name\n> ")
    return name


def timeslots_prompt():
    flag = True
    timeslots = []

    while flag:
        first_prompt = input("Please enter time slots\nexample: 12:30-15:30\n (enter 'END' to finish)\n> ").lower()
        if first_prompt != "end":
            second_prompt = input("Please enter capacity for this slot\nexample: 50\n> ")
            user_input = [first_prompt, second_prompt]
            timeslots.append(user_input)
        else:
            flag = False
        clear_screen()

    return timeslots

def numberofvaccine_prompt():
    amount = input("Please enter the number of available vaccine")
    return amount