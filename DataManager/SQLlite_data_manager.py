from flask_sqlalchemy import SQLAlchemy
from DataManager.data_manager_interface import DataManagerInterface

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db = SQLAlchemy(db_file_name)


    def get_all_users(self):
        """To get a list of all the users who have an account in the moviweb app"""
        sql_query = "SELECT name FROM users"
        result = self.db.engine.execute(sql_query)

        user_names = [row[0] for row in result]
        return user_names

   
    def get_user_movies(self, user_id):
        """To get and return a list of the favourite movies for the specidied uesr_id"""
        pass

    
    def add_new_user(self):
        """To add a new user account to the moviweb app"""
        pass

    
    def add_new_movie(self):
        """To add a new movie to a users list of favourite movies in the moviweb app"""
        pass