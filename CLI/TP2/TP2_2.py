from TP2 import *
from Utils import *


def cli():
    # Retrieve the CSV data
    data = read_csv()

    ten_most_expensive_books(data)
    matrix_data(data, cols = [ 'Prix_Unitaire', 'Quantite_Vendue', 'Region' ])
    covariance, correlation = cov_corr(data, col1 = 'Prix_Unitaire', col2 = 'Quantite_Vendue')
    print(Style.add(f'correlation: {correlation:.2f}', Style.Colors.CYAN, Style.Styles.BOLD), end = '\n\n')
    scatter_plot(data, col1 = 'Prix_Unitaire', col2 = 'Quantite_Vendue')
    slope, intercept = linear_regression_after_2010(data)
    print(f'slope: {slope}\nintercept: {intercept}')

    return_menu()
