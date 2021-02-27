import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

def start_menu():
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

    return timeslots

# CSV Thing
def importToCSV():
    timeslots = timeslots_prompt()
    file = open("timeslots.csv", "a")
    for i in range(len(timeslots)):
        for j in range(len(timeslots[i])):
            file.writelines(timeslots[i][j]+";")
        file.write("\n")

    file.close()

def clearCSV():
    file = open("timeslots.csv", "w")
    file.write("")
    file.close()

# End of CSV Thing

    


def numberofvaccine_prompt():
    amount = input("Please enter the number of available vaccine\n> ")
    return amount


def coordinates_prompt():
    coordinates = input("Please enter coordinates of this vaccination location")
    return coordinates

def prompt_loop():
    print("Welcome to the vaccination station details form\nThis script allows user to input details of a vaccination station\n")
