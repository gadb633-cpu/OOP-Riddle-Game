from json import *
from riddle import *
import os
import json
from json import JSONDecodeError
class RiddleRepository:
    def __init__(self,file_path):
        self.__file_path = file_path
    def load_riddles(self) -> list[Riddle]:    
        with open("riddles.json", "r", encoding="utf-8-sig") as file:
            data = load(file)
        riddles= []
        for i in data:
            if i["type"] == "multiple_4":
                instance1 = FourAnswerRiddle(i["id"],i["question"],i["correct_answer"],i["difficulty"],i["category"],i["possible_answers"])
                riddles.append(instance1)
            elif i["type"] == "multiple_2":
                instance2 = TwoAnswerRiddle(i["id"],i["question"],i["correct_answer"],i["difficulty"],i["category"],i["possible_answers"])
                riddles.append(instance2)
            elif i["type"] == "open":
                instance3 = OpenRiddle(i["id"],i["question"],i["correct_answer"],i["difficulty"],i["category"])
                riddles.append(instance3)
        return riddles 
    def add_riddle(self) -> None:
        id_ = int(input("enter id: "))
        question = input("enter question: ")
        correct_answer = input("enter correct_answer: ")
        difficulty = input("enter difficulty: ")
        category = input("enter category: ")
        type = input("enter type: ")
        f = open("riddles.json","r")
        riddles =load(f)
        f.close()
        if type == "multiple_4":
            possible_answers = input("enter 4 option possible_answers: ")
            possible_answers= possible_answers.split(" ")
            riddles.append({"id":id_, "question":question,"type":type,"correct_answer":correct_answer,"difficulty":difficulty,"category":category,"possible_answers":possible_answers})
        elif type == "multiple_2":
            possible_answers = input("enter 2 option possible_answers: ")
            possible_answers= possible_answers.split(" ")
            riddles.append({"id":id_, "question":question,"type":type,"correct_answer":correct_answer,"difficulty":difficulty,"category":category,"possible_answers":possible_answers})
        elif type == "open":
            riddles.append({"id":id_, "question":question,"type":type,"correct_answer":correct_answer,"difficulty":difficulty,"category":category})    
        return riddles       
    def get_all_riddles(self) -> list[Riddle]:
        f = open("riddles.json","r")
        riddles =load(f)
        f.close()
        return riddles
    def update_riddle(self,riddles) -> bool:
        new_riddles = []
        riddle_id = int(input("enter id: "))
        status = True
        while status:
            new_key_to_change = input("Enter the key: ")
            new_value_to_change = input("Enter the value: ")
            for riddle in riddles:
                if riddle_id == riddle["id"]:
                    if new_key_to_change in riddle:
                        riddle[new_key_to_change] = new_value_to_change
                        new_riddles.append(riddle)
                        print(riddle)      
                    else:
                        # print("the key is not excist! ")
                        new_riddles.append(riddle)
                        continue    
                else:
                    # print("the id is not excist! ")
                    new_riddles.append(riddle)
                    continue
            x = input("you want to update more? ")
            if x == "no":
                status = False
        return new_riddles     
    def delete_riddle(self, riddle_id: int) -> bool:
        pass   
    def save_riddles(self, riddles: list) -> None:
        with open(self.__file_path, "w") as file:
            dump(riddles, file,indent=4)
           