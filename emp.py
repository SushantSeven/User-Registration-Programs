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

# main function
def main():
    while True: # loop until you enter a valid email
        email = input("Enter your email address: ")
        if is_valid_email(email) is True:
            print("Valid email address entered:", email)
            break
        else:
            print("Invalid email address. Please try again.")


if __name__ == "__main__":
    main()
