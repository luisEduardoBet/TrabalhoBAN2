from flask_login import UserMixin


class User(UserMixin): 
    def __init__(self, user_data):
        self.user_data =  user_data

    def get_id(self):
        return str(self.user_data['_id']) 


