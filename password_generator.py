'''
Requirements:

variable length at least 8 characters
at least one number 
at least one special character 
at least one uppercase letter 
at least one lowercase letter 

user input where the password goes (sql lite)
retrieve password from user input of service

process: 
(DONE) ask the user what they are trying to do

if generating password 
    then ask what the password is used for 
    generate the password using the requirments 
    add the entry into the sql lite(sanatize input)

if user wants to retrieve password
    user enters service 
    error handling if user spells service wrong or if entry doesnt exsist
    if correct show user the password 

'''
import random
import string
GET_OPTIONS = ["g","get"]
CREATE_OPTIONS = ["c","create"]
SESSION_OPTIONS = GET_OPTIONS + CREATE_OPTIONS
DEFAULT_PASSWORD_SIZE = 8
MAX_PASSWORD_SIZE = 20
REQUIREMENTS = {
    0: ["!","@","#","$","%","^","&","*","(",")","~"],
    1: list(string.ascii_uppercase),
    2: list(range(0,10)),
    3: list(string.ascii_lowercase)
}


def print_intro():
    print("Welcome to the Password Vault")
    
def complete_password(password):
    for i in range(0,len(password)):
        if not password[i]:
            random_char = random.randint(0,25)
            password[i] = REQUIREMENTS[3][random_char]            
    return password 
            

def generate_password():
    service = input("What kind of service is this passowrd for?").lower()
    password_length = random.randint(DEFAULT_PASSWORD_SIZE, MAX_PASSWORD_SIZE)
    output = [None] * password_length
       
    for i in range(0,3):
        random_index = random.randint(0,password_length - 1)  
        while output[random_index]:
            random_index = random.randint(0,password_length - 1)
        
        random_requirement_index = random.randint(0,len(REQUIREMENTS[i]) - 1)
        output[random_index] = REQUIREMENTS[i][random_requirement_index]
    output = complete_password(output)
    return "".join(output)

def get_password():
    print("Getting Password")
    return 

def main():
    print_intro()
    type_of_session = input("What kind of session are you starting?").lower()
    if not type_of_session in SESSION_OPTIONS:
        print("Please run program again and select valid option")
        exit(1)
    if type_of_session in CREATE_OPTIONS:
        password = generate_password()
        print(password)
    elif type_of_session in GET_OPTIONS:
        get_password()
    














if __name__ == "__main__":
    main()
