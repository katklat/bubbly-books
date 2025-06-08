import os
import pandas as pd
from src.data_loader import load_data

def setup_module(module):
    """ create dummy data for testing """
    os.makedirs('tests/data', exist_ok=True)
    books_data = {'isbn': ['123456789'], 'title': ['Test Book 1'], 'author': ['Author 1'],'publisher': ['Publisher 1'], 'year_of_publication': [2020]}
    users_data = {'user_id': [1], 'location': ['Location 1'], 'age': [25]}
    ratings_data = {'user_id': [1], 'isbn': ['123456789'], 'rating': [5]}
    
    pd.DataFrame(books_data).to_csv('tests/data/books.csv', index=False)
    pd.DataFrame(users_data).to_csv('tests/data/users.csv', index=False)
    pd.DataFrame(ratings_data).to_csv('tests/data/ratings.csv', index=False)

def test_load_data():
    """ test the load_data function """
    books_path = 'tests/data/books.csv'
    users_path = 'tests/data/users.csv'
    ratings_path = 'tests/data/ratings.csv'
    
    books, users, ratings = load_data(books_path, users_path, ratings_path)
    
    assert not books.empty, "Books data is empty"
    assert 'isbn' in books.columns, "Missing column: isbn"
    assert not users.empty, "Users data is empty"
    assert 'user_id' in users.columns, "Missing column: user_id"
    assert not ratings.empty, "Ratings data is empty"
    assert 'rating' in ratings.columns, "Missing column: rating"

def teardown_module(module):
    """ remove dummy data after testing """
    import shutil
    if os.path.exists('tests/data'):
        shutil.rmtree('tests/data')

