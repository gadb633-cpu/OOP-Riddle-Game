class Player():
    def __init__(self,username):
        self.__username = username
    @property
    def get_username(self) -> str:
        return self.__username
    @setattr
    def rename(self, new_username: str) -> None:
        self.__username = new_username
        

