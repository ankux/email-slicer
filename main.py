# This is Email Slicer Code Generator.
print("Welcome to Email Slicer! 😀")
print("Please Enter Your Email Address Below")

# Here the user will be prompted to enter their email address.
user_input = input("\tEmail Address: ").strip()

# Here is the email address slicing logic comes in if statement.
if "@" in user_input:
    print("✅ You have an valid Email address")
    b = (user_input.index("@"))
    x = int(b)
    user_name = user_input[0:x]
    domain_name = user_input[x+1:]
    print("\tUsername: ", user_name)
    print("\tDomain name: ", domain_name)

else:
    print("❌ Invalid Email Address")