# This is Email Slicer Code Generator.
print("Welcome to Email Slicer Generator")
print("Please Enter Your Email Address Below")
# Here the user will be prompted to enter their email address.
user_input = input("\tEmail Address: ")
# Here is the email address slicing logic comes in if statement.
if "@" in user_input:
    print("Your Have Valid Email  address")
    b = (user_input.index("@"))
    b = int(b)
    c = user_input[0:b]
    d = user_input[b+1:]
    print("This is Email Username: ", c)
    print("This is Email Domain: ", d)
else:
    print("Invalid Email Address")