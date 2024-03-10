# method to check if the first name is valid
def is_valid_First_name(first_name):
    return 0 if first_name[0].isupper() and len(first_name)>=3 else 1 # returns 0 if first name is valid else 1

# main function
def main():
    result = is_valid_First_name(input("Enter your first name : ")) # variable to hold the value returned by the is_valid_firstname function
    print("It is a valid first name") if result == 0 else print("It is not a valid first name")


if __name__=="__main__":
    main()