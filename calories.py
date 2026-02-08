entries = []

# ------------------------- 
# LOGIN SCREEN
# -------------------------
def login_screen():
    print("=== LOGIN ===\n")
    print("Log in to access your food tracking data.\n")

    while True:
        email = input("Email: ")
        password = input("Password: ")

        # Temporary placeholder login
        if email == "gutherys@oregonstate.edu" and password == "password":
            print("\nLogin successful.\n")
            return
        else:
            print("\n[ERROR] Invalid login. Try again.\n")

# ----------------
# DASHBOARD 
# ----------------
def dashboard():
    while True:
        print("\n=== DASHBOARD ===\n")
        print("Welcome back Stephen!\n")

        total_calories = sum(e["calories"] for e in entries)
        print(f"Today's Total Calories: {total_calories}\n")

        print("Today's Food Entries:")
        print("---------------------")

        if not entries:
            print("No food entries for today. Add a food entry to your log to get started!")
        else:
            for i, entry in enumerate(entries, start=1):
                print(f"{i}. {entry['name']} - {entry['calories']} cal")

        print("\nOptions:")
        print("1) Add Food Entry")
        print("2) Delete Entry")
        print("3) Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            add_food_entry()
        elif choice == "2":
            delete_entry()
        elif choice == "3":
            print("\nGoodbye.")
            break

# ----------------
# ADD FOOD ENTRY 
# ----------------
def add_food_entry():
    print("\n=== ADD FOOD ENTRY ===\n")
    print("Enter food name and calories, then press 'Enter' to add it to today’s log.")
    print("Type 'cancel' at any time to return to the dashboard.\n")

    while True:
        name = input("Food Name: ")
        if name.lower() == "cancel":
            print("\nCancelled.\n")
            return

        calories = input("Calories: ")
        if calories.lower() == "cancel":
            print("\nCancelled.\n")
            return

        if not name or not calories:
            print("\n[ERROR] Please fill out both entry fields before proceeding.\n")
            continue

        if not calories.isdigit():
            print("\n[ERROR] Calories must be a number.\n")
            continue

        entries.append({"name": name,"calories": int(calories)})

        print("\nEntry saved.\n")
        return

# ----------------
# DELETE ENTRY
# ----------------
def delete_entry():
    if not entries:
        print("\nNo entries to delete.\n")
        return

    try:
        num = int(input("Enter entry number to delete: "))
        entries.pop(num - 1)
        print("Entry deleted.\n")
    except:
        print("[ERROR] Invalid selection.\n")


def main():
    login_screen()
    dashboard()

if __name__ == "__main__":
    main()
