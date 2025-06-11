import pandas as pd

def load_data(books_path, users_path, ratings_path):
    books = pd.read_csv(books_path, header=0, dtype={'isbn': str, 'year_of_publication': int})
    users = pd.read_csv(users_path, header=0, dtype={'user_id': int, 'age': float})
    ratings = pd.read_csv(ratings_path, header=0, dtype={'user_id': int, 'isbn': str, 'rating': int})
    return books, users, ratings