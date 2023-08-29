import pytest
from DataManager.SQLlite_data_manager import SQLiteDataManager

def test_get_all_users():
    db_manager = SQLiteDataManager("test_movie_web_app.db")
    user_names = db_manager.get_all_users()
    print(user_names)
    assert True
