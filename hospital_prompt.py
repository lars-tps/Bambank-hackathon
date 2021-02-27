import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


def name_prompt():
    name = input("Please enter hospital name\n> ").lower()
    return name

def change_form(time_prompt):
    idx=time_prompt.find(":")
    if(idx!=-1):
        time_prompt=list(time_prompt)
        time_prompt[idx]='_'
        return "".join(time_prompt)
    else:
        return time_prompt
def timeslots_prompt():
    flag = True
    timeslots = []

    while flag:
        time_prompt1 = input("Please enter time when the vacination starts\nexample: 12:30\n (enter 'END' to finish)\n> ").lower()
        time_prompt2 =input("Please enter time when the vacination end\nexample: 15:30\n (enter 'END' to finish)\n> ").lower()
        time_prompt1=change_form(time_prompt1)
        time_prompt2=change_form(time_prompt2)
        if time_prompt1 and time_prompt2 != "end":
            second_prompt = input("Please enter capacity for this slot\nexample: 50\n> ")
            user_input = time_prompt1+'-'+time_prompt2+','+second_prompt
            timeslots.append(user_input)
        else:
            flag = False
        clear_screen()

    string = ''

    return timeslots


def numberofvaccine_prompt():
    amount = input("Please enter the number of available vaccine\n> ")
    return amount


def coordinates_prompt():
    coordinates = input("Please enter coordinates of this vaccination location\nexample: 1234567,123456789\n> ")
    return coordinates


def form_tool():
    print("Welcome to the vaccination station details form\nThis script allows user to input details of a vaccination station and stores them in a csv file\n")
    row = [name_prompt(), timeslots_prompt(), coordinates_prompt()]
    print("Form submitted! Thanks for using this tool")
    return row


# CSV Thing
def importToCSV():
    print("Enter 'OVERWRITE' to overwrite csv, enter anything to submit new row")
    add = input(">")
    if(add.lower() == "overwrite"):
        newCSV()
    else:
        form = form_tool()
        file = open("hospital_data.csv", "a")
        for i in form[1]:
            print(form[0],i,form[2])
            file.writelines(str(form[0]) +","+i+','+form[2]+"\n")
        #file.write("\n")

    file.close()

def clearCSV():
    file = open("hospital_data.csv","w")
    file.write("")
    file.close()

def newCSV():
    file = open("hospital_data.csv","w")
    file.writelines("Hospital, Timeslots & Number of Patient, Number of Vaccines, Coordinates \n")
    file.close()



importToCSV()
