import pytest
from DataManager.SQLlite_data_manager import SQLiteDataManager

@pytest.fixture
def db_manager():
    return SQLiteDataManager(":memory:")

def test_get_all_users():
    user_names = db_manager.get_all_users()
    expected_user_names = ["Alice", "Bob"]  # Replace with your expected names
    assert user_names == expected_user_names
