import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(books, users, ratings):
    """
    Explore and visualize the loaded data
    
    Args:
        books: Books DataFrame
        users: Users DataFrame
        ratings: Ratings DataFrame
    """
    print("\n=== Data Overview ===")
    print("\nBooks DataFrame:")
    print(f"Shape: {books.shape}")
    print("\nFirst few rows:")
    print(books.head())
    
    print("\n=== Basic Statistics ===")
    print("\nNumerical features:")
    print(books.describe())
    
    print("\n=== Data Types ===")
    print(books.dtypes)

    # Publication year analysis
    print("\n=== Years of publication ===")
    year_counts = books['year_of_publication'].value_counts().sort_index()
    print("\nYear counts (first 20 years):")
    print(year_counts.head(20))
    print("\nYear counts (last 20 years):")
    print(year_counts.tail(20))
    
    # Check for years that might be invalid
    current_year = pd.Timestamp.now().year
    print(f"\nBooks published after {current_year}:")
    print(books[books['year_of_publication'] > current_year][['title', 'year_of_publication']])
    
    print("\n=== User ages ===")
    print(users['age'].value_counts())
    
    # Plot distributions

    plt.figure(figsize=(10, 5))
    sns.countplot(x='rating', data=ratings)
    plt.title('Distribution of Ratings')
    plt.show()
    

    plt.figure(figsize=(10, 5))
    sns.histplot(books['year_of_publication'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Publication Years')
    plt.xlabel('Publication Year')
    plt.show()


    plt.figure(figsize=(10, 5))
    sns.histplot(users['age'].dropna(), bins=30, kde=True)
    plt.title('Distribution of User Ages')
    plt.xlabel('User Age')
    plt.show()

def explore_features(features):

    plt.figure(figsize=(10, 5))
    sns.histplot(features['rating_deviation'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Rating Deviation')
    plt.xlabel('Rating Deviation')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(features['user_avg_rating'].dropna(), bins=30, kde=True)
    plt.title('Distribution of User Average Rating')
    plt.xlabel('User Average Rating')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(features['book_avg_rating'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Book Average Rating')
    plt.xlabel('Book Average Rating')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(features['user_rating_count'].dropna(), bins=30, kde=True)
    plt.title('Distribution of User Rating Count')
    plt.xlabel('User Rating Count')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(features['book_rating_count'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Book Rating Count')
    plt.xlabel('Book Rating Count')
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.histplot(features['book_age'].dropna(), bins=30, kde=True)
    plt.title('Distribution of Book Age')
    plt.xlabel('Book Age')
    plt.show()
