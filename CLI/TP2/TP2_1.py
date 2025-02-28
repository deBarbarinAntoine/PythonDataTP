from TP2 import *
from Utils import *

def cli():
    
    # Retrieve the CSV data
    data = read_csv()
    
    # Analyze the CSV data
    (stats, mean_price_per_genre) = analyze(data)
    
    # Print the mean price per region
    print(Style.add('The mean price per genre is:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    for col, mean in mean_price_per_genre.items():
        print(Style.add(f'{col}: {mean}', Style.Colors.BLUE))
    print()
    
    confirm_continue()
    
    
    # Print the analyzed data for each numerical column
    print(Style.add('Analysis of each numerical column:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    for col, stats in stats.items():
        print(Style.add(f"Descriptive statistics for column '{col}':", Style.Colors.CYAN, Style.Styles.BOLD))
        print(Style.add(f"Count: {stats.count}", Style.Colors.BLUE))
        print(Style.add(f"Mean: {stats.mean}", Style.Colors.BLUE))
        print(Style.add(f"Standard Deviation: {stats.std}", Style.Colors.BLUE))
        print(Style.add(f"Minimum: {stats.min}", Style.Colors.BLUE))
        print(Style.add(f"Q1: {stats.q1}", Style.Colors.BLUE))
        print(Style.add(f"Median: {stats.median}", Style.Colors.BLUE))
        print(Style.add(f"Q3: {stats.q3}", Style.Colors.BLUE))
        print(Style.add(f"Maximum: {stats.max}", Style.Colors.BLUE), end = '\n\n')
        
        confirm_continue()
        
    
    # Print the genre with the greater median of quantity of books sold
    genre, median = genre_with_best_median_sold_quantity(data)
    
    print(Style.add('The genre with the greater median of quantity of books sold is:', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(f'Genre: {genre}', Style.Colors.BLUE))
    print(Style.add(f'Median: {median}', Style.Colors.BLUE), end = '\n\n')
    
    confirm_continue()
    
    # Print the most expensive book
    book_most_expensive = find_most_expensive(data)
    print(Style.add('The most expensive book is:', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(f"ISBN: {book_most_expensive.isbn}", Style.Colors.BLUE))
    print(Style.add(f"Title: {book_most_expensive.title}", Style.Colors.BLUE))
    print(Style.add(f"Author: {book_most_expensive.author}", Style.Colors.BLUE))
    print(Style.add(f"Genre: {book_most_expensive.genre}", Style.Colors.BLUE))
    print(Style.add(f"Publication Year: {book_most_expensive.publication_year}", Style.Colors.BLUE))
    print(Style.add(f"Unit Price: {book_most_expensive.unit_price}", Style.Colors.BLUE))
    print(Style.add(f"Quantity Sold: {book_most_expensive.quantity_sold}", Style.Colors.BLUE))
    print(Style.add(f"Region: {book_most_expensive.region}", Style.Colors.BLUE))
    print(Style.add(f"Sold At: {book_most_expensive.sold_at}", Style.Colors.BLUE), end = '\n\n')
    
    
    return_menu()
    