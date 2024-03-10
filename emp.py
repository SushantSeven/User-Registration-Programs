# method to check if the first name is valid
def is_valid_first_name(first_name):

    return 0 if first_name[0].isupper() and len(first_name)>=3 else 1 # return 0 if first name is valid else 1

# method to check if the last name is valid
def is_valid_last_name(first_name, last_name):
#    method to check first name is called
    return (is_valid_first_name(first_name), 0) if last_name[0].isupper() and len(last_name) >= 3 else (is_valid_first_name(first_name), 1)

# main function
def main():
    first_name = input("Enter your first name: ") # variable to store the first name
    last_name = input("Enter your last name: ") # variable to store the last name
    result = is_valid_last_name(first_name, last_name) # variable to hosd the value returned by the is_valid_firstname function
    if result == (0,0):
        print("valid first name and last name")
    elif result == (0,1):
        print("valid first name and invalid last name")
    elif result == (1,0):
        print("Invalid firstname and valid last name")
    elif result == (1,1):
        print("Invalid firstname and last name")


if __name__=="__main__":
    main()
    
    
    
