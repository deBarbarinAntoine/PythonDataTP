import pandas as pd


def read_csv() -> pd.DataFrame:
    """
    Reads data from a CSV file named 'ventes_livres.csv'.

    :return: A DataFrame containing the data from the CSV file.
    """
    _data = pd.read_csv('ventes_livres.csv', sep = ',')
    
    # Uncomment the following line to print the entire DataFrame in blue color
    # print(Style.add(str(_data), Style.Colors.BLUE))
    
    if _data is None:
        exit(1)
    
    return _data


def analyze(_data: pd.DataFrame) -> tuple [ dict [ str, 'Stats' ], dict [ str, int|float ] ]:
    """
    Analyzes the data and returns a dictionary of Stats instances for each numeric column and mean price per genre.

    :param _data: DataFrame containing the data.
    :return: A tuple containing a dictionary where keys are column names and values are Stats instances, and another one where keys are genres and values are mean price per genre.
    """
    
    # Calculate the mean price per genre
    mean_price_per_genre = {}
    _mean_price_per_genre = _data.groupby('Genre')['Prix_Unitaire'].mean()
    
    # Get the list of existent genres
    genres = _data['Genre'].unique()
    
    # Fill the mean_price_per_genre dictionary with the genre name as key and its mean price as value
    for genre in genres:
        mean_price_per_genre[genre] = _mean_price_per_genre.loc[genre]
    
    # Create the dictionary of Stats instances
    stats_instances = {}
    
    # Iterate through the columns of the DataFrame
    for col in _data.columns:
        
        # Check if the column is numeric
        if pd.api.types.is_numeric_dtype(_data[col]):
            
            # Create an instance of Stats and store it in the dictionary
            stats_instances[col] = Stats(_data, col)
    
    return stats_instances, mean_price_per_genre

def genre_with_best_median_sold_quantity(_data: pd.DataFrame) -> tuple [ str, int|float ]:
    median_sold_quantity_per_genre = _data.groupby('Genre')['Quantite_Vendue'].median()
    
    best_genre = None
    genre: str
    median: int|float
    for genre, median in median_sold_quantity_per_genre.items():
        if best_genre is None:
            best_genre = (genre, median)
        else:
            best_median = best_genre[1]
            if best_median < median:
                best_genre = (genre, median)
    
    return best_genre


class Stats:
    """
    A class to store descriptive statistics for a specific column in a DataFrame.
    
    :param _data: The DataFrame containing the data.
    :param col: The name of the column to analyze.
    """
    
    
    def __init__(self, _data: pd.DataFrame, col: str) -> None:
        self.data = _data
        self.col = col
        
        # Calculate descriptive statistics for the specified column
        _stats = self.data[ self.col].describe()
        
        # Store individual statistical values as attributes
        self.count = _stats['count']  # Number of non-null observations
        self.mean = _stats['mean']    # Arithmetic mean of the values
        self.std = _stats['std']      # Standard deviation of the values
        self.min = _stats['min']      # Minimum value
        self.q1 = _stats['25%']       # First quartile (25th percentile)
        self.median = _stats['50%']   # Median (50th percentile)
        self.q3 = _stats['75%']       # Third quartile (75th percentile)
        self.max = _stats['max']      # Maximum value

class Book:
    """
    A class representing a book.
    
    :param _data: The DataFrame containing the data for one book.
    """
    
    def __init__(self, _data: pd.DataFrame) -> None:
        self.isbn = _data['ISBN']
        self.title = _data['Titre']
        self.author = _data['Auteur']
        self.genre = _data['Genre']
        self.publication_year = _data['Annee_Publication']
        self.unit_price = _data['Prix_Unitaire']
        self.quantity_sold = _data['Quantite_Vendue']
        self.region = _data['Region']
        self.sold_at = _data['Date_Vente']


def find_most_expensive(_data: pd.DataFrame) -> 'Book':
    """
    Finds the book with the highest price.
    
    :param _data: DataFrame containing the data for multiple books.
    :return: An instance of Book representing the book with the highest price.
    """
    max_price_index = _data['Prix_Unitaire'].idxmax()
    max_price_book_data = _data.loc[max_price_index]
    
    return Book(max_price_book_data)
        