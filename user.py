import re

class User:
    def __init__(self, name:str, email:str, password:str, ID:int, check:bool) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.id = ID
        self.check = check
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    @staticmethod
    def check_email(txt:str):
        return re.match('[a-z0-9]+@[a-z]+\.[a-z]{2,3}',txt)
    @staticmethod
    def check_name(txt:str):
        return re.match('[A-Za-z]',txt)
    @staticmethod
    def check_password(txt:str):
        return re.match('[a-z!-9]')
    def get_id(self):
        return self.id
    def send_message_bot(self):
        pass
    def register(self):
        pass
    def exist(self):
        pass 
    