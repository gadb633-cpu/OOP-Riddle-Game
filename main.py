from game import *
from riddle import *
from player import *
question1 = FourAnswerRiddle(1,"what your name? ","gad","hart","names",["gad","yossi","shlomi","gay"])
question2 = OpenRiddle(2,"what your name? ","gad","hart","names")
question3 =TwoAnswerRiddle(3,"your name is gad? ","yes","hart","names",["yes","no"])
Riddles = [question1,question2,question3]
username.get_username
manager = RiddleGame(username.get_username,Riddles)
manager.print_summary(manager.start())