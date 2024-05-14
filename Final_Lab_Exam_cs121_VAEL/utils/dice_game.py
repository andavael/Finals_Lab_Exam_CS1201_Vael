from utils.user import User
from utils.score_manager import Score
import random
import os

class DiceGame:
    def __init__(self):
        self.total_rounds = 3
        self.current_stage = 1
        self.total_score = 0
        self.stages_won = 0
        self.records = []
        self.score_manager = Score()

    def play_game(self, username):
        print("\t\n TIME TO GET THE DICE ROLLING!")
        print("_" * 100, "\n")
        
        while True:  
            self.records = []
            print(f"\n\tSTAGE {self.current_stage}...\n")  

            user_points = 0
            CPU_points = 0

            while user_points == CPU_points:
                user_points = 0
                CPU_points = 0

                for _ in range(self.total_rounds): 
                    user_num = random.randint(1, 6)
                    CPU_num = random.randint(1, 6)

                    print(f"\t      You rolled      : {user_num}")
                    print(f"\t      CPU rolled      : {CPU_num}")

                    if user_num > CPU_num:
                        print("\n\t> You win this round!\n")
                        user_points += 1
                    elif user_num < CPU_num:
                        print("\n\t> You lose this round!\n")
                        CPU_points += 1
                    else:
                        print("\n\t> It's a tie!\n")

                if user_points == CPU_points:
                    print("\tTIED POINTS!")
                    print("\tBreaking the tie...\n")

            self.total_score += user_points  
            if user_points > CPU_points: 
                print("\tCongratulations! You won the round!")
                self.stages_won += 1
                self.total_score += 3
                print(f"\tStage won         : {self.stages_won}")
                print(f"\tStage {self.current_stage} points    : {user_points}")
                print(f"\tTotal score       : {self.total_score}\n")
                self.current_stage += 1 

                continue_choice = input("\n\t> Would you like to play the next stage? (yes/no): ")
                while continue_choice.lower() not in ["yes", "no"]:
                    print("\nInvalid input. Please enter 'yes' or 'no'.")
                    continue_choice = input("\n\t> Would you like to play the next stage? (yes/no): ")

                if continue_choice.lower() != "yes":
                    print("\nGoing back to game menu...\n") 
                    self.score_manager.record_scores(username, self.total_score, self.stages_won)
                    self.reset_game()
                    return
            else:  
                print("\tYou lost this stage. Better luck next time!\n")
                print(f"\tStage won         : {self.stages_won}")
                print(f"\tStage {self.current_stage} points    : {user_points}")
                print(f"\tTotal Score       : {self.total_score}\n")   
                self.score_manager.record_scores(username, self.total_score, self.stages_won) 
                self.reset_game() 
                return

    def reset_game(self):
        self.total_score = 0
        self.current_stage = 1
        self.stages_won = 0

    def show_top_scores(self):
        print("\t\n\n TOP TEN SCORERS")
        print("_" * 100, "\n")
        scores = self.score_manager.load_scores()
        top_scores = self.score_manager.get_top_scores(scores)

        for i, score in enumerate(top_scores, start=1):
            print(f"\t\t{i}. {score.rstrip()}")

        choice = input("\n\t> Enter 'yes' to go back to game menu: ")
        if choice.lower() == "yes":
            print("\n\nGoing back to the main menu...")
        else:
            print("\n\nInvalid choice. Exiting...")

    def logout(self, user_manager):
        print("\n\nThank you for playing,", user_manager.loggedin_user, "!")
        print("Logging out...\n\n")
        from main import Main
        main = Main()
        main.main()

    def menu(self, user_manager):
        while True:
            try:
                print("\t\n LOGGED AS ", user_manager.loggedin_user.upper()) 
                print("_" * 100, "\n")
                print("\t 1. Start Game")
                print("\t 2. Top Scores")
                print("\t 3. Log Out")

                choice = int(input("\n\t> Please enter the number of your choice: "))

                if choice == 1:
                   self.play_game(user_manager.loggedin_user)
                elif choice == 2:
                    self.show_top_scores()
                elif choice == 3:
                    self.logout(user_manager)
                else:
                    print("\nInvalid choice. Please enter a valid choice\n")
                    continue

            except ValueError as e:
                print("\n", e)