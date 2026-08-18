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
        print(f"hello {username.get_username}! ")
        for riddle in self.__riddles:    
            start_time = perf_counter()
            self.__results.append(self.ask_riddle(riddle))
            end_time = perf_counter()
            execution_time = end_time - start_time
            print(f"time run: {execution_time:.2f} Seconds")
            total_time += execution_time
        print(f"hi {username.get_username} \ntotal time is: {total_time:.2f} Seconds")
        result1 = GameResult(username.get_username,strftime("%d/%m/%Y"),total_time,self.__results)
        print(f"num of correct is: {result1.get_total_riddles}")
        return result1        
            
    def ask_riddle(self, riddle: Riddle) -> QuestionResult:
        start_time = perf_counter()
        while True:
            riddle.display()
            print(riddle.question)
            enswer = input("enter enswer: ")
            if riddle.check_answer(enswer):
                print("corrent!")
                end_time = perf_counter()
                execution_time = end_time - start_time
                question_result = QuestionResult(riddle.riddle_id,riddle.get_type(),riddle.category,execution_time)
                return question_result
            print("try agen! ")
    def print_summary(self, result: GameResult) -> None:
        print(result.average_time_by_type())
        print(result.average_time_by_category())