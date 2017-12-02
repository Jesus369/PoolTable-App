import poolClasses
import time
from time import time as my_timer


admin_func = {1: "Available",
			  2: "Available",
			  3: "Available",
			  4: "Available",
			  5: "Available",
			  6: "Available",
			  7: "Available",
			  8: "Available",
			  9: "Available",
			  10: "Available",
			  11: "Available",
			  12 : "Available"}


taken = "available"
check_in = "r"
check_out = "c"
yes = "y"
no = "n"
my_tuple = tuple(admin_func.items())

print("Would you like to Reserve/Checkout a table?:\t R/C")
user = raw_input("")
print("\n")
if user.lower() == check_in.lower():
    for i in my_tuple:
        table, availability = i
        print("Table: " + str(table) + " Status: " + availability)
        print("\n")
# -------------------------------------------------------------------------------------------------

print("Select an open table number to occupy.")
choice = int(raw_input(""))

while True:
    if taken in admin_func[choice]:
        print("Sorry that table is taken. Please try again")
    elif taken not in admin_func[choice]:
        print("\n")
        print("Enjoy your time at the pool table")
        print("\n")
        if choice == 1:
            poolClasses.table1.yes_occupied()
            admin_func[1] = poolClasses.table1.status

    # -------------------------------------------------------------------------------------------------

    print("Would you like to checkout:\t Y/N?")
    response = raw_input("")
    print("\n")
    if response.lower() == yes.lower():
        print("What is you're table number?")
        choice = int(raw_input(""))
        print("\n")
        if choice == 1:
            poolClasses.table1.checkOut()
            admin_func[1] = poolClasses.table1.status
            print("You have spent a total time of {0} seconds playing.".format(int(poolClasses.table1.totalTime)))
            with open('11-30-2017.txt', 'a') as file_object:
                file_object.write("\n")
                file_object.write(str(poolClasses.table1.totalTime))
        break
