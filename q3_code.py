from q3_driver import PersonData
import sys

def print_menu():
    menu = [
        "1. Create a person",
        "2. Remove a person",
        "3. Show results",
        "4. Exit"
    ]

    print_border_box(menu)


def print_border_box(items):
    global max_length

    if isinstance(items, str):
        items = [items]

    current_max_length = max(len(item) for item in items)

    if current_max_length > max_length:
        max_length = current_max_length

    border_length = max_length + 4
    print("*" * border_length)

    for item in items:
        print(f"* {item.ljust(max_length)} *")

    print("*" * border_length)



if __name__ == "__main__":
    max_length = 0
    person = PersonData()
    while True:
        print_menu()
        operation = int(input("\nWhat would you like to do? "))
        print("\n")
        if operation == 1:
            user_id = int(input("Enter User's ID: "))
            name = str(input("Enter User's Name: "))
            age = int(input("Enter User's Age: "))
            phone = str(input("Enter User's Phone: "))
            person.add_data(user_id, name, age, phone)
            print_border_box("Created Successfully")
            print("\n")

        elif operation == 2:
            user_id = int(input("Enter User's ID: "))
            person.remove_data(user_id)
            print_border_box("Removed Successfully")
            print("\n")

        elif operation == 3:
            person.fetch_data()
            print("\n")

        elif operation == 4:
            person.close_conn()
            del person
            sys.exit(1)

        else:
            print_border_box("INVALID OPERATION")
            print("\n")