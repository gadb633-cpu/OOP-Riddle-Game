import os
import csv
from result import *
class LeaderboardRepository:
    def __init__(self,__file_path: str):
        self.__file_path = __file_path
    def add_result(self, result: GameResult) -> None: 
        pass
    def load_results(self) -> list[dict]:
        pass
    def sort_results(self,results: list[dict],field: str,descending: bool = False) -> list[dict]:   
        pass
    def print_results(self, results: list[dict]) -> None:
        pass
