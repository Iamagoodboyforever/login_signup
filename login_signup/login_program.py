from login_functions import login, signup, forgot

choice = input("{1} Login "
               "\n{2} Signup "
               "\n{3} Forgot account"
               "\n").lower().strip()

if choice == '1' or choice == 'login':

    login()

elif choice == '2' or choice == 'signup':

    signup()

elif choice == '3':

    forgot()

else:
    print("Invalid.")
