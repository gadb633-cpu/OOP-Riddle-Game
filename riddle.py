from abc import ABC,abstractmethod
class Riddle(ABC):
    def __init__(self,id,question,correct_answer,difficulty,category):
        self.__riddle_id = id
        self.__question =question
        self.__correct_answer =correct_answer
        self.__difficulty = difficulty
        self.__category = category
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError
    def check_answer(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
        else:
            return False
    def get_type(self) -> str:
        pass
    def to_dict(self) -> dict:
        pass
    @property
    def riddle_id(self):
        return self.__riddle_id
    @property
    def question(self):
        return self.__question
    @property
    def correct_answer(self):
        return self.__correct_answer
    @property
    def difficulty(self):
        return self.__difficulty
    @property
    def category(self):
        return self.__category
class MultipleChoiceRiddle(Riddle):
    def __init__(self, id, question, correct_answer, difficulty, category,possible_answers):
        super().__init__(id, question, correct_answer, difficulty, category)
        self.__possible_answers = possible_answers
    @property
    def possible_answers(self):
        return list(self.__possible_answers)  
    def display(self) -> None:
        print(f"id is: {self.riddle_id},\n{self.possible_answers}")
    def check_answer(self, answer: str) -> bool:
        if answer == self.correct_answer:
            return True
        else:
            return False
class FourAnswerRiddle(MultipleChoiceRiddle):
    def get_type(self) -> str:
        return "multiple_4"
class TwoAnswerRiddle(MultipleChoiceRiddle):
    def get_type(self) -> str:
        return "multiple_2"
class OpenRiddle(Riddle):
    def display(self) -> None:
        print(f"id is: {self.riddle_id}")
    def get_type(self) -> str: 
        return "open"
question1 = FourAnswerRiddle(1,"what your name? ","gad","hart","names",["gad","yossi","shlomi","gay"])
question2 = OpenRiddle(2,"what your name? ","gad","hart","names")
question3 =TwoAnswerRiddle(3,"your name is gad? ","yes","hart","names",["yes","no"])
Riddles = [question1,question2,question3]