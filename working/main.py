import pyrebase



firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

username = str(input("Enter the username\n"))
password = str(input("Enter your password\n"))

if len(password)<6:
    print("Password should be more than 6 letters\n")
    exit()

#user = auth.create_user_with_email_and_password(username,password)
user = auth.sign_in_with_email_and_password(username,password)
#auth.send_email_verification(user['idToken'])
info = auth.get_account_info(user['idToken'])
check = info['users'][0].get('emailVerified')
if check ==  False:
    print("You are a valid user, need a email verification")
else:
    print("Welcome, you are verified, good to go")
