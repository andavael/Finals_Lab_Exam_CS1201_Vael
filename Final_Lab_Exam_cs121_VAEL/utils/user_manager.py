from utils.user import User
from utils.dice_game import DiceGame
import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.loggedin_user = None 
        self.load_users()

    def load_users(self):
        user_file_path = os.path.join("data", "users.txt")
        if os.path.exists(user_file_path):
            with open(user_file_path, "r") as file:
                user_records = file.readlines()
                for index, record in enumerate(user_records, start=1):
                    try:
                        username, password = record.strip().split(", ")
                        self.users[username] = User(username, password)
                    except ValueError:
                        print(f"Error parsing line {index} in users.txt. Skipping.")

    def save_users(self):
        user_folder = "data"
        user_file_path = os.path.join(user_folder, "users.txt")

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        with open(user_file_path, "w") as file:
            for username, user in self.users.items():
                file.write(f"{username}, {user.password}\n")

    def validate_username(self, username):
        if username in self.users:
            print("\nUsername already exists. Please enter a new one.\n")
            return False
        elif len(username) >= 4:
            return True 
        else:
            print("\nUsername must be at least 4 characters long. Please enter a new one.\n")
            return False

    def validate_password(self, password):
        if len(password) >= 8:
            return True
        else:
            print("\nPassword must be at least 8 characters long. Please enter a new one.\n")
            return False

    def register(self):
        print("\n\tUSER REGISTRATION")
        print("_" * 100, "\n")
        while True:
            try:
                username = input("\t> Please enter a username or leave blank to cancel: ")
                if not username:
                    print("\nRegistration cancelled.")
                    break
                
                if not self.validate_username(username):
                    continue

                password = input("\t> Please enter a password or leave blank to cancel: ")
                if not password:
                    print("\nRegistration cancelled.")
                    break
                
                if not self.validate_password(password):
                    continue 

                else:
                    self.users[username] = User(username, password)
                    print("\n\tUser Registered Succesfully!")
                    print(f"\tWelcome to the Dice Game, {username}!\n")
                    self.save_users()
                    return
            except ValueError as e:
                print(e)

    def login(self):
        print("\n\tUSER LOGIN")
        print("_" * 100, "\n")
        while True:
            try:
                username = input("\t> Please enter your username or leave blank to cancel: ")
                if not username:
                    print("\nLogin cancelled.")
                    break
                
                if username not in self.users:
                    print("\nUser not found. Please register first")
                    return
                
                password = input("\t> Please input your password or leave blank to cancel: ")
                if not password:
                    print("\nLogin cancelled.")
                    return
                
                stored_password = self.users[username].password
                if password == stored_password:
                    self.loggedin_user = username
                    print("\n\tLogin Successful!\n")
                    game = DiceGame()
                    game.menu(self)
                    break
                else:
                    print("\nIncorrect password.\n")
            except ValueError as e:
                print(e)

    