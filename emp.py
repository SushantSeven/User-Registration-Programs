import re
# method to check if the first name is valid
def is_valid_first_name(first_name):
     first_name_patttern = r'^[A-Z][a-zA-Z]{2,}$'
     return bool(re.match(first_name_patttern,first_name)) # returns true if the first name is valid else false

# method to check if the last name is valid
def is_valid_last_name(last_name):
      last_name_patttern = r'^[A-Z][a-zA-Z]{2,}$'
      return bool(re.match(last_name_patttern,last_name)) # returns true if the first name is valid else false

# method to check if the email is valid or not
def is_valid_email(email):
    pattern = r'^[\w+.-]+@([\w-]+\.[\w-]{2,}+)$' # creating pattern to check the email
    double_dot = r'\.\.'
    if re.match(pattern, email) and len(re.findall(double_dot, email))==0: # using regex.match 
        return True
    else:
        return False

# method to validate phone number
def is_valid_phone_no(phone_number):
    phone_pattern = r'^91\s{1}[7,6,8,9]{1}[0-9]{9}$' # creat a pattern to chcke a valid phone number
    return True if re.match(phone_pattern, phone_number) else False # return true if phone number is valid else False

# method to validate password
def validate_password(password):
    password_pattern = r'.{8,}' # pattern to check minimum 8 characters and atleast one numeric charachter
    uppercase_pattern = r'[A-Z]' # patern to check if it has an upper case
    numeric_pattern = r'\d' # pattern to check if it has a number
    special_char_pattern = r'[!@#$%^&*]' # pattern to check if it has exactly one special character
    if (re.match(password_pattern, password) and re.search(uppercase_pattern, password) and re.search(numeric_pattern, password) and len(re.findall(special_char_pattern, password)) == 1):
        return True
    else:
        return False

# main function
def main():
    password = input("Enter your password: ")
    print("It is a valid password!!") if validate_password(password) else print("Invalid password!!")


if __name__ == "__main__":
    main()
