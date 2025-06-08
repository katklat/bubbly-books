import pandas as pd
from src.data_preprocessor import preprocess_data

def test_preprocess_data():
    books_data = {'isbn': ['123456789'], 'title': ['Test Book 1'], 'author': ['Author 1']}
    users_data = {'user_id': [1], 'name': ['Test User']}
    ratings_data = {'user_id': [1], 'isbn': ['123456789'], 'rating': [5]}
    
    books = pd.DataFrame(books_data)
    users = pd.DataFrame(users_data)
    ratings = pd.DataFrame(ratings_data)
    
    df = preprocess_data(books, users, ratings)
    
    assert not df.empty, "Merged DataFrame is empty"
    assert 'user_id' in df.columns, "Missing column: user_id"
    assert 'isbn' in df.columns, "Missing column: isbn"
    assert 'rating' in df.columns, "Missing column: rating"
    assert 'title' in df.columns, "Missing column: title"
    assert 'author' in df.columns, "Missing column: author"
    assert 'name' in df.columns, "Missing column: name"
