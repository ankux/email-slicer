# This is Email Slicer Code Generator.
print("Welcome to Email Slicer Generator")
print("Please Enter Your Email Address Below")

# Here the user will be prompted to enter their email address.
user_input = input("\tEmail Address: ")

# Here is the email address slicing logic comes in if statement.
if "@" in user_input:
    print("Your Have Valid Email  address")
    b = (user_input.index("@"))
    x = int(b)
    user_name = user_input[0:x]
    domain_name = user_input[x+1:]
    print("This is Email Username: ", user_name)
    print("This is Email Domain: ", domain_name)

else:
    print("Invalid Email Address")