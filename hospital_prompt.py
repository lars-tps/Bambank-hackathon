import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


def name_prompt():
    name = input("Please enter hospital name\n> ").lower()
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

    string = ''
    for slot in timeslots:
        string += f"{','.join(slot)};"

    return string


def numberofvaccine_prompt():
    amount = input("Please enter the number of available vaccine\n> ")
    return amount


def coordinates_prompt():
    coordinates = input("Please enter coordinates of this vaccination location")
    return coordinates


def form_tool():
    print("Welcome to the vaccination station details form\nThis script allows user to input details of a vaccination station and stores them in a csv file\n")
    row = [name_prompt(), timeslots_prompt(), numberofvaccine_prompt(), coordinates_prompt()]
    print("Form submitted! Thanks for using this tool")
    return row


# CSV Thing
def importToCSV():
    form = form_tool()
    file = open("hospital_data.csv", "a")
    for i in range(len(form)):
        file.writelines(str(form[i])+";")

    file.close()


importToCSV()
