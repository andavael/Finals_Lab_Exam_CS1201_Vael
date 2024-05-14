import os
from datetime import datetime

class Score:
    def load_scores(self):
        score_folder = "data"
        score_file_path = os.path.join(score_folder, "rankings.txt")

        if not os.path.exists(score_folder):
            os.makedirs(score_folder)

        try:
            with open(score_file_path, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("No scores found.")
            return []
        except Exception as e:
            print(f"Error occurred while loading scores: {e}")
            return []

    def save_scores(self, new_scores):
        score_folder = "data"
        score_file_path = os.path.join(score_folder, "rankings.txt")

        if not os.path.exists(score_folder):
            os.makedirs(score_folder)

        try:
            existing_scores = []
            if os.path.exists(score_file_path):
                with open(score_file_path, "r") as file:
                    existing_scores = file.readlines()

            new_scores_with_stages = [score for score in new_scores if score['stages_won'] > 0]
            new_score_strings = [f"{score['username']}, Points - {score['total_score']} point/s, Wins - {score['stages_won']} stage/s, Date: {score['date'].strftime('%m/%d/%y')}\n" for score in new_scores_with_stages]

            all_scores = existing_scores + new_score_strings
            sorted_scores = sorted(all_scores, key=lambda x: int(x.split(" - ")[1].split(" ")[0]) if len(x.split(" - ")) >= 2 else 0, reverse=True)

            with open(score_file_path, "w") as file:
                file.writelines(sorted_scores)

        except Exception as e:
            print(f"Error occurred while saving scores: {e}")

    def record_scores(self, username, total_score, stages_won):
        game_details = {
            "username": username,
            "total_score": total_score,
            "stages_won": stages_won,
            "date": datetime.now()
        }
        self.save_scores([game_details])

    def get_top_scores(self, scores):
        try:
            sorted_scores = sorted(scores, key=lambda x: int(x.split(" - ")[1].split(" ")[0]) if len(x.split(" - ")) >= 2 else 0, reverse=True)
            return sorted_scores[:10]  
        except Exception as e:
            print(f"Error occurred while sorting scores: {e}")
            return [] 