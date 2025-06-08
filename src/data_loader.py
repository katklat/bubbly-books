import pandas as pd

def load_data(books_path, users_path, ratings_path):
    books = pd.read_csv(books_path)
    users = pd.read_csv(users_path)
    ratings = pd.read_csv(ratings_path)
    return books, users, ratings