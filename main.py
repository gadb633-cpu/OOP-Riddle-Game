from game import *
from riddle import *
from player import *
from repository import *
riddles_list = RiddleRepository("riddles.json")
riddles_list.save_riddles(riddles_list.add_riddle())
print(riddles_list.get_all_riddles())
manager = RiddleGame(username.get_username,riddles_list.load_riddles())
manager.print_summary(manager.start())