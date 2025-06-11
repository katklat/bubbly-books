import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from eda import explore_data
from data_loader import load_data
from data_preprocessor import preprocess_data

    
def main():
    print("Loading data...")
    books, users, ratings = load_data("data/books.csv", "data/users.csv", "data/ratings.csv")
    
    explore_data(books, users, ratings)

    print("\nPreprocessing data...")


if __name__ == "__main__":
    main()