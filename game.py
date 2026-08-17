from result import *
from riddle import *
from player import *
from time import *
from datetime import *
class RiddleGame():
    def __init__(self,player,riddles):
        self.__player = player
        self.__riddles = riddles
        self.__results = []
    def start(self) -> GameResult:
        total_time = 0
        print(f"hello {player}! ")
        for riddle in self.__riddles:    
            start_time = perf_counter()
            self.__results.append(self.ask_riddle(riddle))
            end_time = perf_counter()
            execution_time = end_time - start_time
            print(f"time run: {execution_time:.2f} Seconds")
            total_time += execution_time
            print(f"hi {player} \ntotal time is: {total_time:.2f}")
            result1 = GameResult(player,strftime("%d/%m/%Y"),total_time,self.__results)
            print(f"num of correct is: {result1.get_total_riddles}")
        return result1        
            
    def ask_riddle(self, riddle: Riddle) -> QuestionResult:
        while True:
            riddle.display()
            print(riddle.question)
            enswer = input("enter enswer: ")
            if riddle.check_answer(enswer):
                print("corrent!")
                return QuestionResult(riddle.riddle_id,riddle.get_type,riddle.category,0)
            print("try agen! ")
    def print_summary(self, result: GameResult) -> None:
        pass
player = input("enter usernsme: ")

manager = RiddleGame(player,Riddles)
manager.start()
