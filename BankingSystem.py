def main_menu():
    while True:
        print("\n\t ------------------ Hello User, Welcome to our Banking Management System!!------------------")
        print("\n\t\t MAIN MENU")
        print("\n\t [1] Super User Login \n\t "
              "[2] Admin Login \n\t "
              "[3] Customer Login \n\t "
              "[4] New Customer Register \n\t "
              "[5] About Us \n\t "
              "[6] Exit ")
        option = input("\n\t Please Select Your Option:")
        print("--------------------------------------------------------------------------------")
        if option == '1':
            super_login()
            break
        elif option == '2':
            admin_login()
            break
        elif option == '3':
            customer_login()
            break
        elif option == '4':
            new_register()
            break
        elif option == '5':
            print("\n\n")
            with open('about_us.txt') as f:
                print(f.read())
        elif option == '6':
            exit()
            break
        else:
            print("Invalid User Option!")
        back = input("\nDo You Wish to Continue with Any Option? [Yes/No] \n>").lower()
        if back == "yes" or back == "y":
            return main_menu()
        else:
            exit()


def super_login():
    print("\n\t ------------------ SUPER USER LOGIN PAGE ------------------")
    print("\n")
    print("\t Welcome Super User, Please enter your details to login")
    print("\n")
    try:
        with open("superlogin.txt", "r") as f:
            print("Please use this ID and password:", f.read())
        print("\n")
        super_id = input("Enter Your Super User ID ---> \t "
                         "Super User ID:")
        password = input("Enter Your Password ---> \t "
                         "Password:")
        while True:
            with open("superlogin.txt") as confirm_login:
                for line in confirm_login.readlines():
                    if super_id in line and password in line:
                        print("\n")
                        super_user_menu()
                        break
                    elif super_id in line or password in line:
                        print("Incorrect Super User ID or Password! Please Try Again!")
                    else:
                        print("\t\t-----ERROR!----- \nInput User ID was not found!!")
                    back = input("\nWould you like to continue with this page?[Yes/No] \n>").lower()
                    if back == "yes" or back == "y":
                        super_login()
                        break
                    else:
                        exit()
                        break
    except FileNotFoundError:
        while True:
            print("Use this Super ID[SuperUser] and Password[super] to login Super User Account")
            super_id = input("\n\nEnter your Super User ID:")
            password = input("Enter your Password:")
            if super_id == "SuperUser" and password == "super":
                print("\n")
                super_user_menu()
            elif super_id != "SuperUser" or password != "super":
                print("\nIncorrect Super User ID or Password! Please Try Again")
                super_login()
            else:
                print("\t\t-----ERROR!----- \nInput Super User ID was not found!!")
            ans = input("\nWould you like to continue with this page?[Yes/No] \n>").lower()
            if ans == "yes" or ans == "y":
                super_login()
            else:
                exit()
                break


def super_user_menu():
    while True:
        print("\n\t ------------------ SUPER USER MENU ------------------")
        print("\nHello, Welcome to Super User Page")
        print("\n\t\t MENU")
        print("\n\t[1] Create A New Admin Staff Account \n\t"
              "[2] Manage Admin Account \n\t"
              "[3] Checking Feedback \n\t"
              "[4] Exit")
        choose = input("\nPlease choose an option to continue your next option:")
        print("----------------------------------------------------------------------------------------- \n")
        if choose == "1":
            new_admin_register()
            break
        elif choose == "2":
            print("\n")
            print("These are the admin staff's details that are in working. \n")
            with open("admin_details.txt", "r") as f:
                print(f.read())
            print("\nDear Super User, what is your next option?")
            option = input("\n[1] Modify Admin Staff's Details \n[2] Exit from this page \n>")
            if option == "1":
                change_admin_details()
                break
            elif option == "2":
                print("\nBack to previous page...")
                print("\n")
                super_user_menu()
                break
            else:
                print("Invalid User Input! Please Try Again")
        elif choose == "3":
            print("Loading...")
            print("\n")
            request = open("cus_feedback.txt", "r")
            request_count: int = 0
            for line in request:
                if line != "\n":
                    request_count += 1
            request.close()
            if request_count == 0:
                print("No customer feedback now!")
                print("\n")
                super_user_menu()
            else:
                print("\nHave some customer feedback.\n")
                f = open("cus_feedback.txt", "r")
                print(f.read())
                f.close()
        elif choose == "4":
            exit()
            break
        else:
            print("Invalid User Input!")
        back = input("Would you wish to continue with the Super User Menu page? [Yes/No]\n>").lower()
        if back == "yes" or back == "y":
            super_user_menu()
            break
        else:
            exit()
            break


def admin_login():
    print("\n\t ------------------ ADMIN LOGIN PAGE ------------------")
    print("\nHello, Welcome to Admin Login Page")
    print("\n")
    user_name = input("Enter Your Admin ID: ")
    user_password = input("Enter Your Password: ")
    while True:
        flag = True
        with open("admin_details.txt", "r") as admin_details:
            for line in admin_details:
                if user_name in line and user_password in line:
                    flag = False
                    break
            if flag == True:
                print("\nInput Admin ID and Password does not exist!")
            elif flag == False:
                print("\n")
                admin_menu(user_name)
            restart = input("Do you wish to continue? [Yes/No] \n>").lower()
            if restart == "yes" or restart == "y":
                admin_login()
                break
            else:
                exit()
                break


def admin_menu(user_name):
    while True:
        print("\n\t ------------------ ADMIN MENU PAGE ------------------")
        print("Welcome to Admin Menu Page!")
        print("\n\t\t MENU")
        print("\n\t[1] Giving Approval of Customer Apply Register New Account \n\t"
              "[2] Check Customer Details \n\t"
              "[3] Changed Customer Details \n\t"
              "[4] View All Transaction \n\t"
              "[5] Change My Personal Details \n\t"
              "[6] Exit")
        choose = input("\nPlease choose an option to continue your next option:")
        print("------------------------------------------------------------------")
        if choose == "1":
            new_request(user_name)
            break
        elif choose == "2":
            allCusDetails(user_name)
            break
        elif choose == "3":
            change_cus_details(user_name)
            break
        elif choose == "4":
            allCusTransaction(user_name)
            break
        elif choose == "5":
            admin_change_details_request(user_name)
            break
        elif choose == "6":
            exit()
            break
        else:
            print("Invalid User Input!")
        restart = input("\nDo you wish to continue with this page?[Yes/No] \n>").lower()
        if restart == "yes" or restart == "y":
            admin_menu(user_name)
            break
        else:
            exit()
        break


def customer_login():
    while True:
        print("\n\t ------------------ CUSTOMER LOGIN PAGE ------------------")
        print("\n Welcome to Customer Login Page!")
        print("\n[1] Already have an account \n[2] Haven't have an account "
              "\n[3] Leave this page, back to main menu")
        choose = input("\nEnter >")
        if choose == "1":
            user_name = input("\nEnter your User ID:")
            password = input("Enter your Password:")
            flag = True
            with open("all_customer_login_details.txt", "r") as user_details:
                for line in user_details:
                    if user_name in line and password in line:
                        flag = False
                        break
                if flag == True:
                    print("\nIncorrect Input User ID or Password!")
                elif flag == False:
                    print("\n", user_name, " Welcome!")
                    customer_menu(user_name)
        elif choose == "2":
            print("OK, Jump to new user register page...")
            print("\n")
            new_register()
            break
        elif choose == "3":
            print("OK, Back to main menu... ")
            print("\n")
            main_menu()
            break
        else:
            print("Invalid user input!")
        restart = input("\nWould you like to continue?\t [Yes/No] \n>").lower()
        if restart == "yes" or restart == "y":
            customer_login()
            break
        else:
            exit()
            break


def customer_menu(user_name):
    while True:
        print("\n\t ------------------ CUSTOMER MENU PAGE ------------------")
        print("\n Our Dearest Customer! Welcome!")
        print("\n\t\t MENU")
        print("\n\t[1] Savings \n\t"
              "[2] Withdrawal \n\t"
              "[3] Transferring \n\t"
              "[4] Check Account Balance \n\t"
              "[5] Change My Personal Details \n\t"
              "[6] Giving Feedback \n\t"
              "[7] Exit")
        print("\n Dear Customer, Please Choose Your Optional to Enjoy the Feature.")
        option = input("\n Your option:")
        if option == "1":
            cus_savings(user_name)
            break
        elif option == "2":
            cus_withdrawal(user_name)
            break
        elif option == "3":
            cus_transferring(user_name)
            break
        elif option == "4":
            check_balance(user_name)
            break
        elif option == "5":
            cus_change_details_request(user_name)
            break
        elif option == "6":
            cus_feedback(user_name)
            break
        elif option == "7":
            print("\nDear Customer, \n[1] Logout and Back to Main Menu"
                  "\t[2] Back to Previous Page \t[3] Exit from the Banking System ")
            leave = input("Enter your choose:")
            if leave == "1":
                print("\n")
                main_menu()
                break
            elif leave == "2":
                print("\n")
                customer_menu(user_name)
                break
            elif leave == "3":
                print("\n")
                exit()
                break
            else:
                print("Invalid User Input!")
        else:
            print("Invalid User Input!")
        restart = input("\nDo you wish to continue with this page?[Yes/No] \n>").lower()
        if restart == "yes" or restart == "y":
            customer_menu(user_name)
            break
        else:
            exit()
            break


def new_admin_register():
    import datetime
    while True:
        print("\n\t ------------------ NEW ADMIN REGISTER ------------------")
        print('\nHello, Welcome to New Admin Account Register Page')
        print("\n")
        print("Please input your details that you want to use for register\n")
        x = datetime.datetime.now()
        r = x.strftime("%d/%m/%Y")
        admin_name = input("Enter an Admin ID:")
        admin_password = input("Enter a Password:")
        contact_number = input("Enter a contact number: ")
        email = input("Enter an email address: ")
        content = "\n" + admin_name + "," + admin_password + "," + contact_number + "," + email + "," + r
        filename = "admin_details.txt"
        add_new_content(filename, content)
        print("\n ")
        print("Loading... ...")
        print("\n\nSucceed! New admin account register was done! \n")
        print("The Admin ID ", admin_name, " was saved and the New Account Register Date is", r)
        print("\n ---------- Thanks for register! ----------")
        restart = input("\n Would you like to continue next options? [Yes/No] \t"
                        "[No = Quit] \n> ").lower()
        if restart == "yes" or restart == "y":
            print("\n\t\t\t[1] Go to Admin Login Page \n\t\t\t"
                  "[2] Back to Super User Menu \n\t\t\t"
                  "[3] Quit")
            option = input("Please choose your next option:")
            if option == "1":
                admin_login()
                break
            elif option == "2":
                super_user_menu()
                break
            else:
                exit()
                break
        else:
            exit()
            break


def new_register():
    import datetime
    acc_number = []
    while True:
        print("\n\t\t ------------------ NEW CUSTOMER REGISTER PAGE ------------------")
        print("\n Welcome New User! Thanks for choosing our Banking System!")
        print("\n")
        print(
            "Dear customer, to create a new account, you must fill up your personal details and pay a RM200.00 as deposit and this RM200 will be saved in your current(pay & savings) account.")
        print(
            "Dear customer, you also need to pay a RM1.00 as handling fees for created account because we are not charge any tax.")
        print(
            "After fill up your personal details, our admin staff will give approval to set up your banking account in a moment.")
        print("\n ==================================================================================")
        print("Please fill up your personal details here for sign up a new account.")
        print("\n")
        name = input("Enter Your Name:")
        age = input("Enter Your Age:")
        gender = input("Enter Your Gender:")
        birth = input("Enter Your Date of Birth[DDMMYY]:")
        email = input("Enter Your Email Address:")
        ic = input("Enter Your NIC Number:")
        contact = input("Enter Your Contact Number:")
        country = input("Enter Your Country:")
        x = datetime.datetime.now()
        r = x.strftime("%d.%m.%Y")
        s = x.strftime("%H:%M:%S")
        t = x.strftime("%Y%m%d")
        with open("account_number.txt", "r") as allocate_acc_number:
            for line in allocate_acc_number:
                acc_number.append(line.strip().split(","))
        account_number = str(acc_number[0])
        allInfo = ("\n" + name + "," + age + "," + gender + "," + birth + "," + email + "," + ic + "," + contact + ","
                   + country + "," + r)
        userID = ic
        userPassword = name + birth
        with open("user_request.txt", "a+") as send_request:
            send_request.write(allInfo)
        print("\n Wait for a while, your personal details is uploading... ...")
        print("\n\t\t\t\tLoading... ... ")
        print("\n")
        print("Your personal details were successfully updated!")
        print("\n")
        print("For create a new balance, you need to pay RM200.00 as your savings deposit and RM1.00 as handling fees.")
        print("Total payment amount is RM201.00")
        print("Confirm payment... \n\n :[Yes]")
        print("\n")
        print("\n Payment Successful!")
        print("   Receipt   ")
        print("\n")
        print("       ---------------------------------------------------------------   ")
        print("       |                                                             |   ")
        print("       |      DEAR CUSTOMER                        ", r, "      |   ")
        print("       |                                             ", s, "      |   ")
        print("       |                                                             |   ")
        print("       |      DESC                                    AMOUNT         |   ")
        print("       |  ........................................................   |   ")
        print("       |      Savings Deposit                         RM 200.00      |   ")
        print("       |      Handling Fees                           RM   1.00      |   ")
        print("       |                                                             |   ")
        print("       |                                                             |   ")
        print("       |      TOTAL                                   RM 201.00      |   ")
        print("       |   _______________________________________________________   |   ")
        print("       |      CASH                                    RM 201.00      |   ")
        print("       |      CHANGE                                  RM   0.00      |   ")
        print("       ---------------------------------------------------------------   ")
        print("\n")
        print("Wait for a while...")
        print("\n")
        first_transaction_record = userID + "," + account_number + "," + "[Create Account Deposit]: My Current Account Balance " + "," + "+200.00" + "," + s + "," + r + "," + t + "\n"
        with open("all_customer_transaction.txt", "a+") as save_transaction_record:  # create a transaction record
            save_transaction_record.write(first_transaction_record)
        print("\nHere is your User ID, Password and Account Number. User ID:", userID, "Password:", userPassword,
              "Account Number:", account_number)
        login_info = "\n" + userID + "," + userPassword + "," + "0.00" + "," + "200.0" + "," + account_number  # a place that save all customer ID and password, can determine which customer when login
        with open("all_customer_login_details.txt", "a+") as save_login_info:
            save_login_info.write(login_info)
        need_remove_filename = "account_number.txt"
        remove_first_line(need_remove_filename)
        print("\nPlease wait for a while, our Admin Staff will give approval! \t Thanks for choosing us!!")
        restart = input("\n\t\t\t Press [1] for back to main menu, [2] for exit. \n>")
        if restart == "1":
            main_menu()
            break
        else:
            exit()
            break


def new_request(user_name):
    print("\t\tWelcome!", user_name)
    print("\n------------------------------------------------------------------")
    print("On the way counting how many new user register request... ...\n")
    request = open("user_request.txt", "r")
    request_count: int = 0
    for line in request:
        if line != "\n":
            request_count += 1
    request.close()
    if request_count == 0:
        print("No customer register request now! Enjoy your rest!")
        print("\n")
        admin_menu(user_name)
    else:
        print("Got", request_count, "request at the moment! Enjoy your work!\n")
        print("\n")
        print("Do you wish to continue solving the request? [Yes/No]"
              "\n[Yes] > I love work!"
              "\n[No] > Exit From This Page")
        restart = input("\nEnter your option:").lower()
        if restart == "yes" or restart == "y":
            print("\n......\n")
            handle_request(user_name)
        else:
            print("Press [1] Back to Main Menu\t[2] Back to Admin Menu")
            options = input("\nEnter your next option:")
            if options == "1":
                main_menu()
            elif options == "2":
                admin_menu(user_name)
            else:
                print("Invalid Input!\n")
                new_request(user_name)


def handle_request(user_name):
    import datetime
    user_info = []
    while True:
        print("\n\t ------------------ GIVING APPROVAL ------------------")
        print("\nWelcome!", user_name)
        print("Customer Details Loading...")
        print("\n")
        with open("user_request.txt", "r") as info:
            for line in info:
                user_info.append(list(line.strip("\n").split(",")))
        print(user_info[0])
        print("\nThis customer is the one of request you need to give approval in your work!\n "
              "After finish this approval you can select continue work or rest!\n"
              "Come on! Let's start!")
        print("\n")
        name = input("Customer Name:")
        age = input("Age:")
        gender = input("Gender:")
        birth = input("His/Her Date of Birth[DDMMYY]:")
        email = input("His/Her Email Address:")
        ic = input("His/Her NIC Number:")
        contact = input("His/Her Contact Number:")
        country = input("Country:")
        date = input("His/Her Register Date:")
        x = datetime.datetime.now()
        r = x.strftime("%d/%m/%Y")
        content = ("\n" + name + "," + age + "," + gender + "," + birth + "," + email + "," + ic + "," + contact + ","
                   + country + "," + "Register Date: " + date + "," + "Approve Date: " + r)
        filename = "done_user_details.txt"
        add_new_content(filename, content)
        print("\n Wait for a while, customer personal details is uploading... ...")
        print("\nLoading... ... ")
        print("\n")
        need_remove_filename = "user_request.txt"
        remove_first_line(need_remove_filename)
        print("\nCustomer personal details was successfully updated!")
        restart = input("\nDo you wish to continue giving approval?[Yes/No] \n>").lower()
        if restart == 'yes' or restart == 'y':
            new_request(user_name)
            break
        else:
            print("\n[1] Back to Admin Page \t[2] Back to Main Menu \t[3] Exit from Banking System ")
            choose = input("Enter your choose >")
            if choose == "1":
                admin_menu(user_name)
                break
            elif choose == "2":
                main_menu()
                break
            else:
                exit()
                break


def admin_change_details_request(user_name):
    while True:
        filename = "admin_changed_details_request.txt"
        print("\n ---------------- CHANGE MY PERSONAL DETAILS PAGE ---------------- ")
        print("Welcome!", user_name)
        print(user_name, ", what can I help you?")
        print("\n")
        choose = input("[1] Modify my personal details \t[2] No, exit from this page \n>")
        if choose == "1":
            send_changed(filename, user_name)
        elif choose == "2":
            print("Back to previous page...")
            print("\n")
            admin_menu(user_name)
        else:
            print(user_name, " Invalid Entry!")
        restart = input("\nDo you wish to continue with this page?[Yes/No] \n>").lower()
        if restart == "y" or restart == "yes":
            admin_change_details_request(user_name)
            break
        else:
            print("Back to previous page...")
            admin_menu(user_name)
            break


def change_admin_details():
    show_request = []
    print("\n\t ------------------ MODIFY ADMIN DETAILS ------------------")
    print("\n Super User, you would like to revise which admin staff's personal details?")
    print("-----------------------------------------------------------------------------------------")
    print("On the way counting how many admin changed details request... ...")
    print("\n")
    request = open("admin_changed_details_request.txt", "r")
    request_count: int = 0
    for line in request:
        if line != "\n":
            request_count += 1
    request.close()
    if request_count == 0:
        print("No admin changed details request now! Enjoy your rest!")
        print("\n")
        super_user_menu()
    else:
        print("Got ", request_count, " request at the moment! Enjoy your work!\n")
        print("The request below\n")
        with open("admin_changed_details_request.txt", "r") as read_info:
            for line in read_info:
                show_request.append(list(line.strip("\n").split(",")))
        print(show_request[0])
        print("\n-----------------------------------------------------------------------------------------")
        flag = True
        admin_name = input("\nEnter his/her Admin ID: ")
        old_content = input("His/Her old content: ")
        new_content = input("His/Her new content: ")
        revise_data = ""
        with open("admin_details.txt", "r") as f:
            for line in f:
                if admin_name in line and old_content in line:
                    line = line.replace(old_content, new_content)
                    flag = False
                    break
            if flag == True:
                print("Invalid Input ID or Old content! Please Try Again!")
                change_admin_details()
            elif flag == False:
                revise_data += line
                with open("admin_details.txt", "w+") as fs:
                    fs.write(revise_data)
                print("\n")
                need_remove_filename = "admin_changed_details_request.txt"
                remove_first_line(need_remove_filename)
                print("\nAdmin ID[", admin_name, "]'s detail was modifying successfully!")
    restart = input("Super User, would you like to continue modify admin staff's details?[Yes/No] \n>").lower()
    if restart == "y" or restart == "yes":
        change_admin_details()
    else:
        print("\nBack to previous page...")
        print("\n")
        super_user_menu()


def cus_change_details_request(user_name):
    filename = "cus_changed_details_request.txt"
    while True:
        print("\n ------------------ CHANGE MY PERSONAL DETAILS PAGE ------------------ ")
        print("\n")
        print("Welcome", user_name, ", what can I help you?")
        choose = input("[1] Modify my personal details \t [2] No, exit from this page \n>")
        if choose == "1":
            send_changed(filename, user_name)
        elif choose == "2":
            print("Back to previous page...")
            customer_menu(user_name)
        else:
            print(user_name, " Invalid Entry!")
        restart = input("\nDo you wish to continue?[Yes/No] \n>").lower()
        if restart == "y" or restart == "yes":
            cus_change_details_request(user_name)
        else:
            print("Back to previous page...")
            customer_menu(user_name)
            break


def send_changed(filename, user_name):
    print("These are the details that you can made a change")
    print("\n[1] Contact Number \t[2] Email Address ")
    option = input("\nPlease enter your option:")
    if option == "1":
        old_number = input("Enter your old contact number:")
        new_number = input("Enter your new contact number:")
        print("\n")
        content = "\n" + user_name + " need to change his/her **CONTACT NUMBER** and the old content is " + old_number + ", the new content is " + new_number
        add_new_content(filename, content)
        print("Dear", user_name,
              "your new detail was successfully updated! Our admin staff will modify your details in a moment")
    elif option == "2":
        old_email = input("Enter your old email address:")
        new_email = input("Enter your new email address:")
        print("\n")
        content = "\n" + user_name + " need to change his/her **EMAIL ADDRESS** and the old content is " + old_email + ", the new content is " + new_email
        add_new_content(filename, content)
        print("Dear", user_name,
              "your new detail was successfully updated! Our Admin Staff/ Super User will modify your details in a moment")
    else:
        print(user_name, "Invalid Entry!")


def change_cus_details(user_name):
    show_request = []
    print("\n\t ------------------ MODIFY CUSTOMER DETAILS PAGE ------------------")
    print("Welcome ", user_name)
    print("\nCustomer Request Loading...")
    print("\n")
    with open("cus_changed_details_request.txt", "r") as request:
        request_count: int = 0
        for line in request:
            if line != "\n":
                request_count += 1
    if request_count == 0:
        print("There is no customer changed details request now! Enjoy you rest!")
        print("\n")
        admin_menu(user_name)
    else:
        print("Got ", request_count, " request at the moment! Enjoy your work! \n")
        with open("cus_changed_details_request.txt", "r") as request:
            for line in request:
                show_request.append(list(line.strip("\n").split(",")))
        print(show_request[0])  # show first line request in file
        print("\n-------------------------------------------------------------------------------------")
        flag = True
        print("This is one of the customer changed details request. Please finish it in a moment!")
        cus_name = input("\nEnter his/her Customer ID:")
        old_content = input("His/Her old content >")
        new_content = input("His/Her new content >")
        revise_data = ""
        with open("done_user_details.txt", "r") as f:
            for line in f:
                if cus_name in line and old_content in line:
                    line = line.replace(old_content, new_content)
                    flag = False
                    break
            if flag == True:
                print("Invalid Input ID or Old content! Please Try Again!")
                change_cus_details(user_name)
            elif flag == False:
                revise_data += line
                with open("done_user_details.txt", "w+") as fs:
                    fs.write(revise_data)
                print("\n")
                need_remove_filename = "cus_changed_details_request.txt"
                remove_first_line(need_remove_filename)
                print("Customer ID[", cus_name, "]'s detail was modifying successfully!")
    restart = input("Dear Admin, would you like to continue modify customer's details?[Yes/No] \n>").lower()
    if restart == "y" or restart == "yes":
        change_cus_details(user_name)
    else:
        print("\nBack to admin menu...")
        print("\n")
        admin_menu(user_name)


def allCusDetails(user_name):
    cus_details = []
    print("\n ------------------ CHECK ALL CUSTOMER PERSONAL DETAILS PAGE ------------------ ")
    print("\n")
    print("Welcome!", user_name)
    print("Here is all customer's details")
    print("\n")
    print(" ================================================================================== ")
    print("\n")
    with open("done_user_details.txt", "r") as show_all_cus_details:
        for line in show_all_cus_details:
            cus_details.append(line.strip("\n").split(","))
        for i in range(len(cus_details)):
            print(cus_details[i])
    print("\n")
    print(" ================================================================================== ")
    print("\nAdmin, what's your next option?")
    print("\n[1] Check Customer's Change Details Request \n[2] Exit from this page \n")
    option = input("Your next option >")
    if option == "1":
        request = open("cus_changed_details_request.txt", "r")  # check got customer's request or not
        request_count: int = 0
        for line in request:
            if line != "\n":
                request_count += 1  # count got how many request
        request.close()
        if request_count == 0:
            print("\nNo customer's changed details request now!")
        else:
            print("Got", request_count, "request at the moment! \n")
        back = input("Do you want to continue to handle the request?[Yes/No] \n>").lower()
        if back == "y" or back == "yes":
            change_cus_details(user_name)
        else:
            print("Back to previous page...")
            admin_menu(user_name)
    elif option == "2":
        print("\nBack to previous page...")
        admin_menu(user_name)
    else:
        print("Invalid Entry!")
    restart = input("Would you like to continue with this page?[Yes/No] \n>").lower()
    if restart == "y" or restart == "yes":
        allCusDetails(user_name)
    else:
        print("Back to Admin Menu...")
        admin_menu(user_name)


def allCusTransaction(user_name):
    print("\n ------------------ CHECK CUSTOMER TRANSACTION PAGE ------------------")
    print("\nWelcome!", user_name)
    print("\nPlease Enter the Customer's User ID Before Check His/Her Transaction")
    cus_name = input("\n His/Her User ID >")
    while True:
        flag = True
        with open("all_customer_login_details.txt", "r") as check_name:
            for line in check_name:
                if cus_name in line:
                    flag = False
                    break
            if flag == False:
                break
            elif flag == True:
                print("Input User ID was not found!")
                back = input("Dear admin, would you like to continue with this page?[Yes/No] \n> ").lower()
                if back == "y" or back == "yes":
                    allCusTransaction(user_name)
                else:
                    print("\nBack to previous page...")
                    admin_menu(user_name)
    print(" [1] Check His/Her transaction \t [2] Generate His/Her transaction report \t [3] Exit")
    choose = input("Please select an option >")
    if choose == "1":
        print("\nWait for a while...")
        print("\nHis/Her all transaction record belows")
        print(" ................................................................................... \n")
        transaction_record = []
        with open("all_customer_transaction.txt", "r") as check_cus_transaction:
            check = check_cus_transaction.readlines()
            for line in check:
                line = line.strip("\n").split(",")
                if cus_name == line[0]:
                    transaction_record.append(line)
            for i in range(len(transaction_record)):
                print(transaction_record[i])
        print("\n")
        print(" ................................................................................... \n")
    elif choose == "2":
        print("\nPlease fill up the started date and ended date that you want to generate in report")
        print("Date Example --> 11/11/2021 > 20211111")
        start_date = input("Started Date >")
        end_date = input("Ended Date >")
        print("\nWait for a while...")
        transaction_list = []
        with open("all_customer_transaction.txt", "r") as check_transaction:
            check = check_transaction.readlines()
            for line in check:
                line = line.strip().split(",")
                if cus_name == line[0] and int(line[6]) >= int(start_date) and int(line[6]) <= int(end_date):
                    content = line[1] + " " + line[0] + "   " + line[2] + "   " + line[3] + "   " + line[4] + "  " + line[5]
                    transaction_list.append(content)
            print("From ", start_date, "to ", end_date, " , Customer ID ", cus_name, "'s report is below")
            print("\n................................................................................... \n")
            for i in range(len(transaction_list)):
                print(transaction_list[i])
            print("\n................................................................................... \n")
    elif choose == "3":
        print("\nBack to previous page...")
        admin_menu(user_name)
    else:
        print("Invalid Input!")
    restart = input("Dear admin, would you like to continue with this page?[Yes/No] \n> ").lower()
    if restart == "n" or restart == "no":
        print("\nBack to previous page...")
        admin_menu(user_name)
    else:
        print("\n")
        allCusTransaction(user_name)


def check_balance(user_name):
    while True:
        print("\n ------------------ CHECK ACCOUNT BALANCE PAGE ------------------ ")
        print("\nWelcome! ", user_name)
        with open("all_customer_login_details.txt", "r") as check_cus:
            for line in check_cus:
                if user_name in line:
                    arrange = line.strip().split(",")
            current = arrange[3]
            savings = arrange[2]
            total_balance = float(current) + float(savings)
            print(user_name, ", your current total account balance is RM", total_balance)
            print(" ================================================================================== ")
            print("\n [Pay & Savings Account] amount is RM", current, "\t[Savings] amount is RM", savings)
            print(
                "\n Remark: Each depositor is protected by the Malaysian Deposit Insurance Institution up to MYR 250,000.")  # reference from Heong Leong Bank
            print(" ================================================================================== ")
            print("\n\t\t\t\t MENU")
            print("\n\t\t\t [1] Savings \n\t\t\t [2] Transferring \n\t\t\t [3] Withdrawal"
                  "\n\t\t\t [4] Check All Transaction \n\t\t\t [5] Back to Menu")
            option = input("\n Enter your option>")
            if option == "1":
                print("\n")
                cus_savings(user_name)
            elif option == "2":
                print("\n")
                cus_transferring(user_name)
            elif option == "3":
                print("\n")
                cus_withdrawal(user_name)
            elif option == "4":
                print("\n")
                my_transaction(user_name)
            elif option == "5":
                print("\n")
                customer_menu(user_name)
            else:
                print("\n Invalid User Input!")
        restart = input("Do you wish to continue with this page?[Yes/No] \n>").lower()
        if restart == "y" or restart == "yes":
            print("\n")
            check_balance(user_name)
            break
        else:
            print("\n")
            exit()
            break


def cus_savings(user_name):
    import datetime
    while True:
        print("\n ------------------ SAVINGS PAGE ------------------ ")
        print("Welcome!", user_name)
        with open("all_customer_login_details.txt", "r") as check_cus_name:
            for line in check_cus_name:
                if user_name in line:
                    arrange = line.strip().split(",")
            my_current = arrange[3]
            my_savings = arrange[2]
            account_number = arrange[4]
            x = datetime.datetime.now()
            r = x.strftime("%d.%m.%Y")
            s = x.strftime("%H:%M:%S")
            t = x.strftime("%Y%m%d")
            print("\n [1] Savings \t [2] Exit")
            choose = input("\nEnter Your choose >")
            if choose == "1":
                print(" ----------------------------------------------------------- ")
                print("\nPlease select an account that you want to save money")
                account = input("[1] Current(Pay & Savings)Account \t[2] Savings Account \n>")
                if account == "1":
                    print("\n")
                    current_save_money(my_current, user_name, account_number, s, r, t)
                elif account == "2":
                    print("\n")
                    savings_save_money(my_savings, user_name, account_number, s, r, t)
                else:
                    print("\nInvalid User Input!")
            elif choose == "2":
                print("\nBack to previous page... \n")
                customer_menu(user_name)
            else:
                print("\nInvalid User Input!")
            restart = input("\nDear customer, do you wish to continue savings?[Yes/No] \n> ").lower()
            if restart == "y" or restart == "yes":
                cus_savings(user_name)
            else:
                print("Back to previous page...")
                customer_menu(user_name)


def current_save_money(my_current, user_name, account_number, s, r, t):
    print(user_name, "Account number:", account_number, "Your current account balance is RM",
          my_current)
    print("\nSavings Amount Example : > RMXX.XX ")
    save_amount = input("\nPlease Enter Savings Amount > RM")
    print("\nProcessing...")
    print("\nAmount RM", save_amount, " had been saved into your account!")
    my_total_current = float(my_current) + float(save_amount)
    renew_current(user_name, my_current, my_total_current)
    filename = "all_customer_transaction.txt"
    content = user_name + "," + account_number + "," + "[Savings]:My Current Account Balance " + ",+" + save_amount + "," + s + "," + r + "," + t + "\n"
    add_new_content(filename, content)
    print("\n")
    print("Now your current account balance is RM", my_total_current)


def savings_save_money(my_savings, user_name, account_number, s, r, t):
    print(user_name, "Account number:", account_number, "Your savings account balance is RM",
          my_savings)
    print("\nSavings Amount Example : > RMXX.XX ")
    save_amount = input("Please Enter Savings Amount > RM ")
    print("\nProcessing...")
    print("\nAmount RM", save_amount, " had been saved into your account!")
    my_total_savings = float(my_savings) + float(save_amount)
    renew_savings(user_name, my_savings, my_total_savings)
    filename = "all_customer_transaction.txt"
    content = user_name + "," + account_number + "," + "[Savings]:My Savings Account Balance " + ",+" + save_amount + "," + s + "," + r + "," + t + "\n"
    add_new_content(filename, content)
    print("\n")
    print("Now your savings account balance is RM", my_total_savings)


def add_new_content(filename, content):
    with open(filename, "a+") as save_record:
        save_record.write(content)


def cus_withdrawal(user_name):
    import datetime
    while True:
        print("\n ------------------ WITHDRAWAL PAGE ------------------ ")
        print("Welcome! ", user_name)
        x = datetime.datetime.now()
        r = x.strftime("%d.%m.%Y")
        s = x.strftime("%H:%M:%S")
        t = x.strftime("%Y%m%d")
        with open("all_customer_login_details.txt", "r") as search_user:
            for line in search_user:
                if user_name in line:
                    arrange = line.strip().split(",")
            my_current = arrange[3]
            my_savings = arrange[2]
            account_number = arrange[4]
            print("\n[1] Withdrawal \n[2] Exit")
            choose = input("\nPlease choose an option:")
            print(" ----------------------------------------------------------- ")
            if choose == "1":
                print("Please select an account to continue withdrawal option \n"
                      "[1] Current Account(Pay & Savings) \n[2] Savings ")
                option = input("\nEnter your choose >")
                if option == "1":
                    print("\n")
                    withdrawal_current_features(account_number, my_current, user_name, s, t, r)
                elif option == "2":
                    print("\n")
                    withdrawal_savings_features(account_number, my_savings, user_name, s, t, r)
                else:
                    print("Invalid User Input!")
            elif choose == "2":
                print("\nBack to previous page...")
                customer_menu(user_name)
            else:
                print("Invalid User Input!")
        restart = input("\nDear customer, would you like to continue?[Yes/No] \n>").lower()
        if restart == "y" or restart == "yes":
            print("\n")
            cus_withdrawal(user_name)
        else:
            end = input("\n[1] Back to previous page \n[2] Exit \n>")
            if end == "1":
                customer_menu(user_name)
            else:
                exit()
                break


def withdrawal_current_features(account_number, my_current, user_name, s, t, r):
    print("\nAccount number", account_number, ", Your current account balance is RM", my_current)
    print(
        "\nRemark : After withdrawal, your current account balance cannot less than RM500! If less than RM500, this system will auto cancel your request!")
    print("Remark : If your current account balance not enough, you can't withdrawal with this account!")
    withdrawal_current = input("\nPlease Enter the amount that you want to withdrawal > RM")
    print("\nProcessing...")
    my_total_current = float(my_current) - float(withdrawal_current)
    if str(withdrawal_current) < str(my_current) and my_total_current > 500:
        print("\nYour withdrawal amount is RM", withdrawal_current)
        print("\nLoading...")
        renew_current(user_name, my_current, my_total_current)
        filename = "all_customer_transaction.txt"
        content = user_name + "," + account_number + "," + "[Withdrawal]:My Current Account Balance ,-" + withdrawal_current + "," + s + "," + r + "," + t + "\n"
        add_new_content(filename, content)
        print("\nWithdrawal succeed! Now your current account balance is RM", my_total_current)
        print("Dear", user_name, ", Thanks for using us!")
    else:
        print("\nYour current account balance was not enough! Withdrawal request failed!")


def withdrawal_savings_features(account_number, my_savings, user_name, s, t, r):
    print("\nYour savings account balance is RM", my_savings)
    print(
        "\nRemark : After withdrawal, your savings account balance cannot less than RM100! If less than RM100, this system will auto cancel your request!")
    print("If your savings account balance not enough, you can't withdrawal with this account!")
    withdrawal_savings = input("\nPlease Enter the amount that you want to withdrawal > RM")
    print("\nProcessing...")
    my_total_savings = float(my_savings) - float(withdrawal_savings)
    if float(withdrawal_savings) < float(my_savings) and my_total_savings > 100:
        print("\nYour withdrawal amount is RM", withdrawal_savings)
        print("\nLoading...")
        renew_savings(user_name, my_savings, my_total_savings)
        filename = "all_customer_transaction.txt"
        content = user_name + "," + account_number + "," + "[Withdrawal]:My Savings Account Balance ,-" + withdrawal_savings + "," + s + "," + r + "," + t + "\n"
        add_new_content(filename, content)
        print("\nWithdrawal succeed! Now your savings account balance is RM", my_total_savings)
        print("Dear", user_name, ", Thanks for using us!")
    else:
        print("\nYour savings account balance was not enough! Withdrawal request failed!")


def cus_transferring(user_name):
    import datetime
    print("\n ------------------ TRANSFERRING PAGE ------------------ ")
    print("\nWelcome!", user_name)
    x = datetime.datetime.now()
    r = x.strftime("%d.%m.%Y")
    s = x.strftime("%H:%M:%S")
    t = x.strftime("%Y%m%d")
    with open("all_customer_login_details.txt", "r") as check_cus_name:
        for line in check_cus_name:
            if user_name in line:
                my_arrange = line.strip().split(",")
        my_current = my_arrange[3]
        my_savings = my_arrange[2]
        my_account_number = my_arrange[4]
        print(" ----------------------------------------------------------- ")
        print("\n [1] Transferring \t [2] Exit")
        choose = input("\n Enter Your choose >")
        if choose == "1":
            print("\nPlease select an account that you want to continue transfer")
            which_account = input("[1] Current Account(Pay & Savings) \t [2] Savings \n>")
            if which_account == "1":
                transfer_with_my_current(user_name, my_current, my_account_number, r, s, t)
            elif which_account == "2":
                transfer_with_my_savings(user_name, my_savings, my_account_number, r, s, t)
            else:
                print("Invalid User Input!")
        elif choose == "2":
            print("\nBack to previous page...")  # exit from transfer page
            customer_menu(user_name)
        else:
            print("Invalid User Input!")  # false input select between transfer or exit
    restart = input("Dear customer, would you like to continue with this page?[Yes/No] \n>").lower()
    if restart == "y" or restart == "yes":
        print("\n")
        cus_transferring(user_name)
    else:
        print("\nBack to customer menu... ")
        customer_menu(user_name)


def transfer_with_my_current(user_name, my_current, my_account_number, r, s, t):
    print("\n")
    print("\nAccount number", my_account_number, ", Your current account balance is RM",
          my_current)  # show i got how many money
    print("\nIf your current account balance not enough, you can't continue transfer with using this account!")
    print("\nTransferring Amount Example : RMXX.XX")  # transfer example
    transfer_current = input("\nPlease Enter the amount that you want to transfer > RM")
    if float(transfer_current) > float(my_current) and str(transfer_current) < str(0):
        print("\nYour current account balance was not enough! Transfer request failed!")
        print("Back to previous option...")
        cus_transferring(user_name)
    else:
        print("\nYour transfer amount is RM", transfer_current)
        print("\nLoading...")
        print("\n Please fill a person's User ID that you want to transfer the money to him/her")
        person_name = input("\n His/Her User ID >")
        flags = True
        with open("all_customer_login_details.txt", "r") as find_person:
            for lines in find_person:
                if person_name in lines:  # i had founded that guy
                    his_arrange = lines.strip().split(",")
                    flags = False
                    break
            if flags == True:
                print("Input Person's User ID was not found! Transfer reject!")
            elif flags == False:
                his_savings = his_arrange[2]
                his_current = his_arrange[3]
                his_account_number = his_arrange[4]
                my_total_current = float(my_current) - float(transfer_current)
                select_acc = input(
                    "\n Select His/Her account type \n[1] Savings \t [2] Current Account(Pay & Savings)\n>")
                if select_acc == "1":
                    print("\nTransfer acceptable!")
                    renew_current(user_name, my_current, my_total_current)
                    his_total_savings = float(his_savings) + float(transfer_current)
                    renew_his_savings(person_name, his_savings, his_total_savings)
                    content = person_name + "," + his_account_number + "," + "[Transfer from " + user_name + "]:My Savings Account Balance +" + transfer_current + \
                              "," + s + "," + r + "," + t + "\n" + user_name + "," + my_account_number + "," + "[Transfer to " + person_name + "]:My Current Account Balance ,-" + transfer_current + \
                              "," + s + "," + r + "," + t + "\n"
                    filename = "all_customer_transaction.txt"
                    add_new_content(filename, content)
                    print("\nTransfer succeed! Now your current account balance is RM", my_total_current)
                    print("\nThanks for using our transferring function!")
                elif select_acc == "2":
                    print("\nTransfer acceptable!")
                    renew_current(user_name, my_current, my_total_current)
                    his_total_current = float(his_current) + float(transfer_current)
                    renew_his_current(person_name, his_current, his_total_current)
                    content = person_name + "," + his_account_number + "," + "[Transfer from " + user_name + "]:My Savings Account Balance ,+" + transfer_current + \
                              "," + s + "," + r + "," + t + "\n" + user_name + "," + my_account_number + "," + "[Transfer to " + person_name + "]:My Current Account Balance ,-" + transfer_current + \
                              "," + s + "," + r + "," + t + "\n"
                    filename = "all_customer_transaction.txt"
                    add_new_content(filename, content)
                    print("\nTransfer succeed! Now your current account balance is RM", my_total_current)
                    print("\nThanks for using our transferring function!")
                else:
                    print("\nInvalid User Input!")


def transfer_with_my_savings(user_name, my_savings, my_account_number, r, s, t):
    print("\n")
    print("\nYour savings account balance is RM", my_savings)
    print(
        "\nIf your savings account balance not enough, you can't transfer with using this account!")
    print("\nTransferring Amount Example : RMXX.XX")
    transfer_savings = input("\nPlease Enter the amount that you want to transfer > RM")
    if float(transfer_savings) > float(my_savings) and str(transfer_savings) < str(0):
        print("\nYour savings account balance was not enough! Transfer request failed!")
        print("Back to previous option...")
        cus_transferring(user_name)
    else:
        print("\nAccount number", my_account_number, "Your transfer amount is RM",
              transfer_savings)  # show the amount i want transfer
        print("\nLoading...")
        print(
            "\n Please fill a person's User ID that you want to transfer the money to him/her")
        person_name = input("\n His/Her User ID >")
        flags = True
        with open("all_customer_login_details.txt", "r") as find_person:
            for lines in find_person:
                if person_name in lines:
                    his_arrange = lines.strip().split(",")
                    flags = False
                    break
            if flags == True:
                print("Input Person's ID was not found! Transfer reject!")
            elif flags == False:
                his_savings = his_arrange[2]
                his_current = his_arrange[3]
                his_account_number = his_arrange[4]
                my_total_savings = float(my_savings) - float(transfer_savings)
                select_acc = input(
                    "\n Select His/Her account type \n[1] Savings \t [2] Current Account(Pay & Savings)\n>")
                if select_acc == "1":
                    print("\nTransfer acceptable!")
                    renew_savings(user_name, my_savings, my_total_savings)
                    his_total_savings = float(his_savings) + float(transfer_savings)
                    renew_his_savings(person_name, his_savings, his_total_savings)
                    content = person_name + "," + his_account_number + "," + "[Transfer from " + user_name + "]:My Savings Account Balance ,+" + transfer_savings + \
                              "," + s + "," + r + "," + t + "\n" + user_name + "," + my_account_number + "," + "[Transfer to " + person_name + "]:My Savings Account Balance ,-" + transfer_savings + \
                              "," + s + " " + r + "," + t + "\n"
                    filename = "all_customer_transaction.txt"
                    add_new_content(filename, content)
                    print("\nTransfer succeed! Now your savings account balance is RM", my_total_savings)
                    print("\nThanks for using our transferring function!")

                elif select_acc == "2":
                    print("\nTransfer acceptable!")
                    renew_savings(user_name, my_savings, my_total_savings)
                    his_total_current = float(his_current) + float(transfer_savings)
                    renew_his_current(person_name, his_current, his_total_current)
                    content = person_name + "," + his_account_number + "," + "[Transfer from " + user_name + "]:My Current Account Balance ,+" + transfer_savings + \
                              "," + s + "," + r + "," + t + "\n" + user_name + "," + my_account_number + "," + "[Transfer to " + person_name + "]:My Savings Account Balance ,-" + transfer_savings + \
                              "," + s + "," + r + "," + t + "\n"
                    filename = "all_customer_transaction.txt"
                    add_new_content(filename, content)
                    print("\nTransfer succeed! Now your savings account balance is RM", my_total_savings)
                    print("\nThanks for using our transferring function!")

                else:
                    print("\nInvalid User Input!")


def renew_current(user_name, my_current, my_total_current):
    file_my_current = ""
    with open("all_customer_login_details.txt", "r") as renew_my_current:
        for all_balance in renew_my_current:
            if user_name in all_balance and my_current in all_balance:
                all_balance = all_balance.replace(str(my_current), str(my_total_current))
            file_my_current += all_balance
    with open("all_customer_login_details.txt", "w+") as renew_balance:
        renew_balance.write(file_my_current)


def renew_savings(user_name, my_savings, my_total_savings):
    file_my_savings = ""
    with open("all_customer_login_details.txt", "r") as renew_my_savings:
        for all_balance in renew_my_savings:
            if user_name in all_balance and my_savings in all_balance:
                all_balance = all_balance.replace(str(my_savings), str(my_total_savings))
            file_my_savings += all_balance
    with open("all_customer_login_details.txt", "w+") as renew_balance:
        renew_balance.write(file_my_savings)


def renew_his_current(person_name, his_current, his_total_current):
    file_his_current = ""
    with open("all_customer_login_details.txt", "r") as renew_person_current:
        for his_balance in renew_person_current:
            if person_name in his_balance and his_current in his_balance:
                his_balance = his_balance.replace(str(his_current), str(his_total_current))
            file_his_current += his_balance
    with open("all_customer_login_details.txt", "w+") as renew_person_current:
        renew_person_current.write(file_his_current)


def renew_his_savings(person_name, his_savings, his_total_savings):
    file_his_savings = ""
    with open("all_customer_login_details.txt", "r") as renew_person_savings:
        for his_balance in renew_person_savings:
            if person_name in his_balance and his_savings in his_balance:
                his_balance = his_balance.replace(str(his_savings), str(his_total_savings))
            file_his_savings += his_balance
    with open("all_customer_login_details.txt", "w+") as renew_person_savings:
        renew_person_savings.write(file_his_savings)


def my_transaction(user_name):
    transaction_list = []
    print("\n ------------------ CHECK MY ALL TRANSACTION PAGE ------------------")
    print("Welcome!", user_name)
    while True:
        print("\nDear Customer, please wait for a while")
        print("\n Your all transaction record bellows")
        print(" ................................................................................... \n")
        with open("all_customer_transaction.txt", "r") as check_my_transaction:
            check = check_my_transaction.readlines()
            for line in check:
                line = line.strip().split(",")
                if user_name == line[0]:
                    transaction_list.append(line)
            for i in range(len(transaction_list)):
                print(transaction_list[i])
            print("\n")
        print(" ................................................................................... \n")
        restart = input("Dear customer, would you like to continue with this page?[Yes/No] \n> ").lower()
        if restart == "n" or restart == "no":
            print("\nBack to previous page...")
            customer_menu(user_name)
        else:
            print("\n")
            my_transaction(user_name)


def remove_first_line(need_remove_filename):
    remove_request = 0  # details line that already show and settle
    delete_request = open(need_remove_filename, "r+")
    delete_line = delete_request.readlines()
    delete_request.close()
    delete_line.pop(remove_request)  # remove already finish approve details
    renew_file = "".join(delete_line)  # use "" to replace a new blank line that generate when i delete something
    renew_request = open(need_remove_filename, "w+")
    renew_request.write(renew_file)
    renew_request.close()


def cus_feedback(user_name):
    print("\nLoading...")
    print("\n\t ------------------ FEEDBACK ------------------")
    print("\n Dear Customer! Your feedback is our motivation for progress! ")
    print("\n")
    choose = input("[1] Leave this page\t [2] Giving Feedback \n>")
    if choose == "1":
        print("Back to previous page...")
        print("\n")
        customer_menu(user_name)
    elif choose == "2":
        print("\n Dear customer, your feedback will be anonymous.")
        write = input("\nWrite something > ")
        content = write + "\n"
        filename = "cus_feedback.txt"
        add_new_content(filename, content)
        print("Uploading your recommend...")
        print("\n\n")
        print("Done! Your recommend was successfully updated! Thanks for your responding! "
              "We will reference your suggest!")
    else:
        print("Invalid User Input!")
    restart = input("Do you wish to continue with this page?[Yes/No] \n>").lower()
    if restart == "yes" or restart == "y":
        print("\n")
        cus_feedback(user_name)
    else:
        print("\n")
        customer_menu(user_name)


def exit():
    print("Exit from Banking System... .... ...")
    print("\n... ... ... \n\n... ... ... ")
    print("\n")
    print(" ================================================================================== ")
    print("                     Thanks for using us! Have a good day! Bye!     ")
    print(" ================================================================================== ")
    return main_menu()


main_menu()
