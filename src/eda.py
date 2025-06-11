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

