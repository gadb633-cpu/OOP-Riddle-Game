class Riddle:
    def __init__(self,id,question,correct_answer,difficulty,category):
        self.riddle_id = id
        self.question =question
        self.correct_answer =correct_answer
        self.difficulty = difficulty
        self.category = category
    def display(self) -> None:
        pass
    def check_answer(self, answer: str) -> bool:
        pass
    def get_type(self) -> str:
        pass
    def to_dict(self) -> dict:
        pass
class MultipleChoiceRiddle(Riddle):
    def __init__(self, id, question, correct_answer, difficulty, category,possible_answers):
        super().__init__(id, question, correct_answer, difficulty, category,possible_answers)
        self.possible_answers = possible_answers
    def display(self) -> None:
        pass
    def check_answer(self, answer: str) -> bool:
        pass
    def get_possible_answers(self) -> list[str]:
        pass
class FourAnswerRiddle(MultipleChoiceRiddle):
    def get_type(self) -> str:
        pass
class TwoAnswerRiddle(MultipleChoiceRiddle):
    def get_type(self) -> str:
        pass
class OpenRiddle(Riddle):
    def display(self) -> None:
        pass
    def get_type(self) -> str: 
        pass                       
