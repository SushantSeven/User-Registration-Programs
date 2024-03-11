import re
# method to check if the first name is valid
def is_valid_First_name(first_name):
    first_name_patttern = r'^[A-Z]{1}+[a-z]{3,}'
    return bool(re.match(first_name_patttern,first_name)) # returns true if the first name is valid else false

# main function
def main():
    result = is_valid_First_name(input("Enter your first name : ")) # variable to hold the value returned by the is_valid_firstname function
    print("It is a valid first name") if result is True else print("It is not a valid first name")


if __name__=="__main__":
    main()