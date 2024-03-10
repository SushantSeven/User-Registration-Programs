import re
# method to check if the first name is valid
def is_valid_first_name(first_name):

    return 0 if first_name[0].isupper() and len(first_name)>=3 else 1

# method to check if the last name is valid
def is_valid_last_name(first_name, last_name):
#    method to check first name is called 
    return (is_valid_first_name(first_name), 0) if last_name[0].isupper() and len(last_name) >= 3 else (is_valid_first_name(first_name), 1)

# method to check if the email is valid or not
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+\.+[a-zA-Z]+@[bi]+\.co(?:\.[a-zA-Z]{2})?$' # creating pattern to check the email
    if re.match(pattern, email): # using regex.match 
        return True
    else:
        return False

# main function
def main():
    while True: # loop until you enter a valid email
        email = input("Enter your email address: ")
        if is_valid_email(email):
            print("Valid email address entered:", email)
            break
        else:
            print("Invalid email address. Please try again.")


if __name__ == "__main__":
    main()
