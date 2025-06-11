import pandas as pd

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
    
    cleaned_books = books[
        (books['year_of_publication'] <= 2025) & 
        (books['year_of_publication'] >= 1900)
    ].copy()
    
    return cleaned_books, cleaned_users, cleaned_ratings
