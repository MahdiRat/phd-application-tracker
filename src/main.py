from models import Application


app1 = Application(
    "Bilkent University",
    "Dr. Bahrami",
    "Turkey"
)

print(app1.university)
print(app1.professor)
print(app1.country)

def show_menu():
    print("\n==============================")
    print("   PhD Application Tracker")
    print("==============================")
    print("1. Add application")
    print("2. View applications")
    print("3. Update application")
    print("4. Delete application")
    print("5. Exit")
    print("6. Search applications")

def add_application():
    university = input("University: ")
    professor = input("Professor: ")
    country = input("Country: ")
    
    app = Application(
        university,
        professor,
        country
    )
    applications.append(app)

    print("\nApplication added successfully!")
    print(app.university)

def view_applications():
    if len(applications) == 0:
        print("No applications found.")
        return

    print("\nYour Applications:")
    
    for index, app in enumerate(applications, start=1):
        print("\nApplication", index)
        print("University:", app.university)
        print("Professor:", app.professor)
        print("Country:", app.country)


applications = []

while True:
    show_menu()

    choice = input("\nChoose an option: ")

    if choice == "1":
    	add_application()

    elif choice == "2":
    	view_applications()

    elif choice == "3":
        print("You selected Update application")

    elif choice == "4":
        print("You selected Delete application")

    elif choice == "5":
        print("Good Bye 👋")
        break

    elif choice == "6":
        print("Search selected")

    else:
        print("Invalid option")


