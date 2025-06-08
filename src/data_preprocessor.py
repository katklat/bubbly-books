import pandas as pd

def preprocess_data(books, users, ratings):
    df = pd.merge(ratings, users, on='user_id')
    df = pd.merge(df, books, on='isbn')
    return df
