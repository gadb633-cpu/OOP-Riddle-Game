from game import *
from riddle import *
from player import *
from repository import *
import questionary
riddles_list = RiddleRepository("riddles.json")
manager = RiddleGame(username.get_username,riddles_list.load_riddles())
def main():
    choice = questionary.select(
        "enter your choice: ",
        choices=[
            "1. Play game",
            "2. Manage riddles",
            "3. View leaderboard",
            "4. Exit"
        ],
    ).ask()
    if choice == "1. Play game":
        manager.print_summary(manager.start())
    if choice == "2. Manage riddles":
        choice_ = questionary.select(
                "enter your choice: ",
                choices=[
                    "1. Add riddle",
                    "2. Show all riddles",
                    "3. Update riddle",
                    "4. Delete riddle",
                    "5. Return"
                ],
            ).ask()
        if choice_ == "1. Add riddle":
            riddles_list.save_riddles(riddles_list.add_riddle())
        if choice_ == "2. Show all riddles":
            print(riddles_list.get_all_riddles())
        if choice_ == "3. Update riddle":
            riddles_list.save_riddles(riddles_list.update_riddle(riddles_list.get_all_riddles()))
        if choice_ == "4. Delete riddle":
            riddles_list.save_riddles(riddles_list.delete_riddle(riddles_list.get_all_riddles()))
        if choice_ == "5. Return":
           main()              
main()    