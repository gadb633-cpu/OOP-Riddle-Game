class QuestionResult():
    def __init__(self,riddle_id,riddle_type,category,time_taken):
        self.__riddle_id =riddle_id
        self.__riddle_type = riddle_type
        self.__category =category
        self.__time_taken =time_taken
class GameResult():
    def __init__(self,username,date,total_time,question_results):
        self. __username = username
        self.__date = date
        self.__total_time = total_time
        self.__question_results = question_results
    @property
    def get_total_riddles(self) -> int:
        return len(self.__question_results)
    def average_time_by_type(self) -> dict[str, float]:
        pass
    def average_time_by_category(self) -> dict[str, float]:
        pass
    def to_csv_row(self) -> list:
        pass

