import pickle


class Password:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def display(self):
        print("\n----------------------------")
        print("Website :", self.website)
        print("Username:", self.username)
        print("Password:", self.password)
        print("----------------------------")


class PasswordManager:

    def __init__(self):
        self.passwords = []
        self.load_passwords()

    def save_passwords(self):
        try:
            with open("passwords.dat", "wb") as file:
                pickle.dump(self.passwords, file)
                file.close()

        except Exception as e:
            print("Error Saving Data")
            print(e)

    def load_passwords(self):
        try:
            with open("passwords.dat", "rb") as file:
                self.passwords = pickle.load(file)
                file.close()

        except:
            self.passwords = []

    def check_strength(self, password):

        if len(password) < 8:
            return "Weak"

        has_upper = False
        has_lower = False
        has_digit = False

        for ch in password:

            if ch.isupper():
                has_upper = True

            elif ch.islower():
                has_lower = True

            elif ch.isdigit():
                has_digit = True

        if has_upper and has_lower and has_digit:
            return "Strong"

        return "Medium"

    def add_password(self):

        website = input("Enter Website Name: ")

        for p in self.passwords:
            if p.website.lower() == website.lower():
                print("Website Already Exists.")
                return

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        strength = self.check_strength(password)

        print("Password Strength:", strength)

        p = Password(website,username,password)

        self.passwords.append(p)

        self.save_passwords()

        print("Password Added Successfully!")

    def view_passwords(self):

        if len(self.passwords) == 0:
            print("No Passwords Stored.")
            return

        for p in self.passwords:
            p.display()

    def search_password(self):

        website = input("Enter Website To Search: ")

        found = False

        for p in self.passwords:

            if p.website.lower() == website.lower():

                p.display()

                found = True
                break

        if not found:
            print("Website Not Found.")

    def update_password(self):

        website = input("Enter Website To Update: ")

        found = False

        for p in self.passwords:

            if p.website.lower() == website.lower():

                print("\nCurrent Details")
                p.display()

                new_username = input("Enter New Username: ")

                new_password = input("Enter New Password: ")

                strength = self.check_strength(new_password)

                print("Password Strength:",strength)

                p.username = new_username
                p.password = new_password

                self.save_passwords()

                print("Password Updated Successfully!")

                found = True
                break

        if not found:
            print("Website Not Found.")

    def delete_password(self):

        website = input("Enter Website To Delete: ")

        found = False

        for p in self.passwords:

            if p.website.lower() == website.lower():

                self.passwords.remove(p)

                self.save_passwords()

                print("Password Deleted Successfully!")

                found = True
                break

        if not found:
            print("Website Not Found.")

    def statistics(self):

        print("\n===== STATISTICS =====")
        print("Total Passwords Stored:",len(self.passwords))


manager = PasswordManager()

while True:

    print("\n")
    print("=" * 35)
    print("      PASSWORD MANAGER")
    print("=" * 35)

    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Update Password")
    print("5. Delete Password")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_password()

    elif choice == "2":
        manager.view_passwords()

    elif choice == "3":
        manager.search_password()

    elif choice == "4":
        manager.update_password()

    elif choice == "5":
        manager.delete_password()

    elif choice == "6":
        manager.statistics()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
