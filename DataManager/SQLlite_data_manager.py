import sqlite3
from DataManager.data_manager_interface import DataManagerInterface

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, db_file_name):
        self.db_connection = sqlite3.connect(db_file_name)

    def get_all_users(self):
        """To get a list of all the users who have an account in the moviweb app"""
        sql_query = "SELECT name FROM Users"
        cursor = self.db_connection.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()

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




""" test_class = SQLiteDataManager("movie_web_app.db")
print(test_class.get_all_users())
test_class.db_connection.close() """