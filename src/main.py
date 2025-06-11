import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from eda import explore_data
from data_loader import load_data
from data_preprocessor import clean_data

    
def main():
    print("Loading data...")
    books, users, ratings = load_data("data/books.csv", "data/users.csv", "data/ratings.csv")
    
    #explore_data(books, users, ratings)

    print("\nPreprocessing data...")
    cleaned_books, cleaned_users, cleaned_ratings = clean_data(books, users, ratings)
    
    explore_data(cleaned_books, cleaned_users, cleaned_ratings)

if __name__ == "__main__":
    main()