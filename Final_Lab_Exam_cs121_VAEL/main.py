from utils.user_manager import UserManager

class Main:
    def __init__(self):
        self.user_manager = UserManager()
        
    def main(self):
        while True:
            try:
                print("\nWELCOME TO THE DICE GAME!")
                print("_" * 100, "\n")
                print("\t 1. Register")
                print("\t 2. Login")
                print("\t 3. Exit")

                choice = int(input("\n\t> Please enter the number of your choice: "))

                if choice == 1:
                    self.user_manager.register()
                elif choice == 2:
                   self.user_manager.login()
                elif choice == 3:
                    print("\nExiting...\n\n")
                    exit()
                else:
                    print("\nInvalid choice. Please enter a valid choice")
                    continue
            except ValueError as e:
                print("\n", e)

if __name__ == "__main__":
    game = Main()
    game.main() 