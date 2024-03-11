import re
# method to check if the first name is valid
def is_valid_first_name(first_name):
        first_name_patttern = r'^[A-Z]{1}+[a-z]{2,}'
        return bool(re.match(first_name_patttern,first_name)) # returns true if the first name is valid else false


# method to check if the last name is valid
def is_valid_last_name(last_name):
     last_name_patttern = r'^[A-Z]{1}+[a-z]{2,}'
     return bool(re.match(last_name_patttern,last_name)) # returns true if the first name is valid else false

# main function
def main():
    last_name = input("Enter your last name: ") # variable to store the last name
    print("It is a valid last name! ")if is_valid_last_name(last_name) is True else print("It is not a valid last name!")
    

if __name__=="__main__":
    main()
    
    
    
