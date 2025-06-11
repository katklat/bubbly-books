import pandas as pd
from datetime import datetime

def clean_data(books, users, ratings):
    """
    Clean the input data by removing invalid entries.
    
    Args:
        books: DataFrame containing book information
        users: DataFrame containing user information
        ratings: DataFrame containing user ratings
        
    Returns:
        Tuple of (cleaned_books, cleaned_users, cleaned_ratings)
    """
    # Remove ratings with 0 as they are placeholder values
    cleaned_ratings = ratings[ratings['rating'] > 0].copy()
    cleaned_users = users[users['age'] < 100].copy()

    # Remove picture urls
    cleaned_books = books.drop(columns=['image_url_s', 'image_url_m', 'image_url_l']).copy()
    
    cleaned_books = cleaned_books[
        (cleaned_books['year_of_publication'] <= 2025) & 
        (cleaned_books['year_of_publication'] >= 1900)
    ].copy()
    
    return cleaned_books, cleaned_users, cleaned_ratings


def add_book_features(books, current_year):

    books = books.copy()
    books['book_age'] = current_year - books['year_of_publication']
    return books

def add_user_features(ratings):

    return ratings.groupby('user_id')['rating'].agg([
        ('user_avg_rating', 'mean'),
        ('user_rating_count', 'count')
    ]).reset_index()

def add_book_statistics(ratings):

    return ratings.groupby('isbn')['rating'].agg([
        ('book_avg_rating', 'mean'),
        ('book_rating_count', 'count')
    ]).reset_index()

def add_features(books, users, ratings):
 
    current_year = datetime.now().year
    books = add_book_features(books, current_year)
    
    user_stats = add_user_features(ratings)
    
    book_stats = add_book_statistics(ratings)
    
    df = pd.merge(ratings, users, on='user_id')
    df = pd.merge(df, books, on='isbn')
    
    df = df.merge(user_stats, on='user_id')
    df = df.merge(book_stats, on='isbn')
   
    df['rating_deviation'] = df['rating'] - df['book_avg_rating']
    
    
    return df

