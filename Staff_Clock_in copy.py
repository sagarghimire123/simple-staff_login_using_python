# Import date and time to display date and time.
import datetime
now = datetime.datetime.now()

# Create a staff list.
staff_list = ["Syed Roshaan", "Anonna Khan", "Iqra Choudhary", "Sagar Ghimire"]

# Create staff id and password.
x = id =[1111, 1121, 1131, 1141]
z = password = ["Roshaan11", "Khan21", "Choudhary31", "Ghimire41"]

# Assign a restart or try again value.
restart = "y"
try_again = 'y'

regular_weekly_hours = 40

# Assign numbers for main menu choice.
Clock_in = 1
clock_out = 2
Staff_list = 3
Add_staff = 4
Delete_staff = 5
Change_password = 6
weekly_pay = 7
Log_out = 0

# Creat a main function.
def main():
    # Create sub-functions.
    welcome()
    staff_login()
    staff_choice()

def welcome():
    # Display welcome message to user.
    print("****************** WELCOME  TO OCEAN IT SOLUTION EMPLOYEE PORTAL *****************")
    print("                                 129-11 APPLE AVE\n"
          "                                    BROOKLYN NY\n"
          "                                       11221\n")
    print()
    print()
    print("\n######Please enter you credentials to start.######")
    print()

def staff_login():
    # Ask user for id and password.
    try:
        x = int(input("Employee id = "))
        z = str(input("Password = "))
        print()

        if x == 1111 and z == "Roshaan11":               # Check for the particular user id and password
            print("####Welcome Mr.Syed Roshaan.####")    # and display name and department of work.
            print("Dept: Security")
            print()


        elif x == 1121 and z == "Khan21":
            print("####Welcome Miss Anonna Khan.####")
            print("Dept: Reception")
            print()


        elif x == 1131 and z == "Choudhary31":
            print("####Welcome Miss Iqra Choudhary####")
            print("Dept: Finance")
            print()


        elif x == 1141 and z == "Ghimire41":
            print("####Welcome Mr. Sagar Ghimire####")
            print("Dept: Supply")
            print()

        else:
            print("Please enter correct credentials.")
            return staff_login()

    # If wrong id and password entered take back to staff_login.
    except ValueError:
        print("Please enter correct credentials.")
        return staff_login()


def staff_choice():
    # Display options for staff to choose.
    print("Please choose one of the following options.\n")
    print("1 == Clock in "
          "\n2 == Clock out"
          "\n3 == Check Staff list"
          "\n4 == Add new staff"
          "\n5 == Delete a staff"
          "\n6 == Change Password"
          "\n7 == weekly_pay"
          "\n0 == Log out")
    print()
    # Ask user to enter choice.
    try:
        a = int(input("enter your choice: "))
        if a == 1:                                       # Check for the entered choice and display
            print("\n######You are Clocked in######")    # content of respective choice.
            print(now.strftime("%B/%d/%Y\n%H:%M:%S%p"))
            print()
            restart = input("Would you like to go back(enter 'y' or 'n')?: \n")  # Ask option to return to choice menu
            if restart in ('n', 'NO', 'N', 'no'):                                # or log out the system.
                print("You are being logged out please wait.........")
                print("******Logged out successfully******")
                print("******Thank You for using employee portal.******")
                exit()
            else:
                return staff_choice()
        elif a == 2:
            print("\n######You are clocked out######")
            print(now.strftime("%B/%d/%Y\n%H:%M:%S%p"))
            print()
            restart = input("Would you like to go back(enter 'y' or 'n')?: \n")
            if restart in ('n', 'NO', 'N', 'no'):
                print("You are being logged out please wait.........")
                print("******Logged out successfully******")
                print("******Thank You for using employee portal.******")
                exit()
            else:
                return staff_choice()

        elif a == 3:
            print(*staff_list, sep="\n")
            print()
            restart = input("Would you like to go back(enter 'y' or 'n')?: \n")
            if restart in ('n', 'NO', 'N', 'no'):
                print("You are being logged out please wait.........")
                print("******Logged out successfully******")
                print("******Thank You for using employee portal.******")
                exit()
            else:
                return staff_choice()

        elif a == 4:
            while try_again:
                print("\n######You are adding a new staff into the employee portal.######")
                print()
                new_staff = str(input("Please enter First and Last name of the new employee: "))
                if (new_staff in staff_list):
                    print("######This staff is already in the list.######")

                else:
                    staff_list.append(new_staff)
                    print("\nNew staff added successfully.")
                    print(*staff_list, sep="\n")                          # Print new staff list.
                    print()
                    restart = input("Would you like to go back(enter 'y' or 'n')?: \n")
                    if restart in ('n', 'NO', 'N', 'no'):
                        print("You are being logged out please wait.........")
                        print("******Logged out successfully******")
                        print("******Thank You for using employee portal.******")
                        exit()
                    else:
                        return staff_choice()

        elif a == 5:
            while try_again:

                print("######You are deleting a staff.######")
                print()
                staff = str(input("enter the first and last name of the staff: "))
                if (staff not in staff_list):
                    print("This staff is not in the list.\n")

                else:
                    staff_list.remove(staff)
                    print("######You have successfully removed", staff, "from the list.######\n")
                    print("The new staff list is:\n", *staff_list, sep="\n")     # print new staff list.
                    print()
                    restart = input("Would you like to go back(enter 'y' or 'n'?: \n")
                    if restart in ('n', 'NO', 'N', 'no'):
                        print("You are being logged out please wait.........")
                        print("******Logged out successfully******")
                        print("******Thank You for using employee portal.******")
                        exit()
                    else:
                        return staff_choice()

        elif a == 6:
            while try_again:
                print("********you are about to change your password********")
                print()
                new_password = input("Please enter your new password: ")
                if new_password not in password:
                    print("\n******You have successfully changed your password.******")
                    print("\n********Your password has been saved.********")  # Display conformation message.
                    print()
                    restart = input("Would you like to go back(enter 'y' or 'n')?: \n")
                    if restart in ('n', 'NO', 'N', 'no'):
                        print("You are being logged out please wait.........")
                        print("******Logged out successfully******")
                        print("******Thank You for using employee portal.******")
                        exit()
                    else:
                        return staff_choice()
                else:
                    print("#####This password is already in use by our system.#####\n")

        elif a == 7:
            while try_again:
                # Ask user to enter hours worked and hourly pay.
                try:
                    hours = float(input("\nHow many hours did you work this week: "))
                    wage = float(input("\nEnter your hourly salary:$"))
                    over_time = hours - 40
                    if hours > 0 and hours <= 40:
                        weekly_pay = hours*wage
                        print("\nYour pay for this week is $", format(weekly_pay, ".2f"), sep="")
                        print()
                        restart = input("Would you like to go back(enter 'y' or 'n')?:\n")
                        if restart in ('n', 'NO', 'N', 'no'):
                            print("You are being logged out please wait.........")
                            print("******Logged out successfully******")
                            print("******Thank You for using employee portal.******")
                            exit()
                        else:
                            return staff_choice()

                    else:
                        print("You worked", over_time,"hours overtime this week.")
                        weekly_pay = (40*wage) + (over_time *(1.5*wage))
                        print("Your pay for this week is $", format(weekly_pay, ".2f"), sep="")
                        print()
                        restart = input("Would you like to go back(enter 'y' or 'n')?: \n")
                        if restart in ('n', 'NO', 'N', 'no'):
                            print("You are being logged out please wait.........")
                            print("******Logged out successfully******")
                            print("******Thank You for using employee portal.******")
                            exit()
                        else:
                            return staff_choice()
                except ValueError:
                    print("######Value must be numbers######\n")

        elif a == 0:
            print("Please wait.........")
            print("######You are log out of employee portal.######")
            print("######Thank You!######")

        else:
            print("***Please enter your choice correctly: ***")
            return staff_choice()
    except ValueError:                                   # Display error message and return back to staff_ choice menu.
        print("***Please enter your choice correctly: ***")
        return staff_choice()

# Call the main function.
main()
