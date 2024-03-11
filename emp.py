import re
# method to check if the first name is valid
def is_valid_first_name(first_name):
     first_name_patttern = r'^[A-Z]{1}+[a-z]{2,}'
     return bool(re.match(first_name_patttern,first_name)) # returns true if the first name is valid else false

# method to check if the last name is valid
def is_valid_last_name(last_name):
      last_name_patttern = r'^[A-Z]{1}+[a-z]{2,}'
      return bool(re.match(last_name_patttern,last_name)) # returns true if the first name is valid else false

# method to check if the email is valid or not
def is_valid_email(email):
    pattern = r'^[\w.-]+@([\w-]+\.[\w.-]+)$' # creating pattern to check the email
    if re.match(pattern, email): # using regex.match 
        return True
    else:
        return False

# method to validate phone number
def is_valid_phone_no(phone_number):
    phone_pattern = r'^91\s{1}[0-9]{10}$' # creat a pattern to chcke a valid phone number
    return True if re.match(phone_pattern, phone_number) else False # return true if phone number is valid else False
    
# main function
def main():
    phone_number = input("\nEnter your phone number: ")
    print("\nIt is a valid phone number!") if is_valid_phone_no(phone_number) is True else print("\nIt is not a valid Phone nummber!")


if __name__ == "__main__":
    main()
