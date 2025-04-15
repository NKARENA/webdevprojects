import csv
import utility
log = 0

def checking_id():
    try:
        f = open("jetdata.csv", "r", newline='')
        r = csv.reader(f)
        id_check = len(list(r))-1
        f.close()
        return id_check
    except FileNotFoundError:
        print("File not found!!!")

def duplicate(lst):
    f = open("jetdata.csv", "r", newline='') 
    r = csv.reader(f)
    l = list(r)
    f.close()
    for i in l:
        if i[1:] == lst[1:]:
            return True
    return False

def search_jet():
    try:
        print("\n----------------SEARCH----------------\n")
        budget = int(input("Enter your budget: ")) 
        range = int(input("Enter the desired range (in nautical miles less than 10000): "))
        seats = int(input("Enter the minimum number of seats: "))
        f = open("jetdata.csv", "r", newline="")
        r = csv.reader(f)
        result = []
        for i in r:
            if i == ['ID','MODEL','AGE','MAX RANGE','SEATS','PRICE','OPERATING COST']:
                result.append(i)
            else: 
                price = float(i[5])
                max_range = int(i[3])
                seat = int(i[4])
                if price <= budget and max_range >= range and seat >= seats:
                    result.append(i)
        if len(result) == 1:
            msg = "No matching JETS for your requirement!!"
            print()
            print("-"*len(msg))
            print(msg)
            print("-"*len(msg))
        else:
            utility.styling_list(result)
        f.close()
    except ValueError:
        print("\nInvalid input! Please try again.\n")
    except FileNotFoundError:
        print("File not found!!!")


def insert_jet():
    try:
        print("\n----------------INSERT DATA----------------\n")
        no_of_insertions = int(input("How many entries do you want to enter? "))
        id_change = checking_id()
        with open("jetdata.csv", "a",newline='') as f:
            w = csv.writer(f)
            for i in range(no_of_insertions):
                print("Entry number", i+1)
                id = id_change+1
                model = input("Enter the model name: ")
                age = int(input("Enter the age of plane: "))
                max_range = int(input("Enter the maximum travel distance (in nautical miles less than 10000): "))
                seats = int(input("Enter the number of seats: "))
                price = float(input("Enter the price of the plane: "))
                operating_cost = float(input("Enter the operating cost of the plane: "))
                new_record = [str(id),str(model),str(age),str(max_range),str(seats),str(price),str(operating_cost)]
                if duplicate(new_record):
                    print("This entry already exists! Duplicate entry cannont be inserted!")
                else:
                    w.writerow(new_record)
                    id_change+=1
                    print("Data entry successful!!!")
                
    except ValueError:
        print("\nInvalid input! Please try again.\n")
    except FileNotFoundError:
        print("File not found!!!")

def recent():
    try:
        print("\n----------------RECENTLY ADDED JETS----------------\n")
        with open("jetdata.csv", 'r', newline="") as f:
            r = csv.reader(f) 
            l = list(r)
            headings = l[0]
            l.reverse()
            most_recent = l[0:5]
            resultant = [headings] + most_recent
            utility.styling_list(resultant)
            
    except FileNotFoundError:
        print("File not found!!!")

def login():
    try:
        f = open("admin.csv", "r")
        r = csv.reader(f)
        all_users = {}
        global log
        for row in r:
            all_users[row[0]] = row[1]
        while True:
            print("\n----------------LOGIN----------------\n")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in all_users and all_users[username] == password:
                log = 1
                print("\nLogin successful!\n")
                break
            else:
                print("\nInvalid credentials! Enter valid credentials.\n")
                log = 0
                break
    except ValueError:
        print("\nInvalid input! Please try again.\n")


def main():
    global log
    print("\nWelcome to Jet Database!\n")
    while log == 0:    
        print("\n-------------------MAIN MENU------------------\n")
        print("1. Search for a jet")
        print("2. Display the most recent jets")
        print("3. Admin Login")
        print("4. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                search_jet()
            elif choice == 2:
                recent()
            elif choice == 3:
                login()
            elif choice == 4:
                print("\n------Thank you for using Jet Database!------\n")
                break
            else:
                print("Please enter valid input (1 to 4)")
        except ValueError:
            print("Please enter valid input (1 to 4)")
    while log == 1:
        print("\n----------------ADMIN PANEL------------------\n")
        print("1. Insert new data")
        print("2. Logout")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            insert_jet()
        elif choice == 2:
            print("\nLogout successful!\n")
            log = 0
            main()
        else:
            print("\nInvalid choice! Please try again.\n")

if __name__ == "__main__":
    main()