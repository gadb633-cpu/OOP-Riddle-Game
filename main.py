from game import *
from riddle import *
from player import *
from repository import *
manager = RiddleGame(username.get_username,riddles_list.load_riddles())
manager.print_summary(manager.start())