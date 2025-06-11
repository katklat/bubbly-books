from data_loader import load_data
from eda import explore_data, explore_features
from data_preprocessor import clean_data, add_features

    
def main():
    print("Loading data...")
    books, users, ratings = load_data("data/books.csv", "data/users.csv", "data/ratings.csv")
    
    # explore_data(books, users, ratings)

    print("\nPreprocessing data...")
    cleaned_books, cleaned_users, cleaned_ratings = clean_data(books, users, ratings)
    
    # explore_data(cleaned_books, cleaned_users, cleaned_ratings)]

    print("\nAdding features...")
    featured_df = add_features(cleaned_books, cleaned_users, cleaned_ratings)

    explore_features(featured_df)

if __name__ == "__main__":
    main()