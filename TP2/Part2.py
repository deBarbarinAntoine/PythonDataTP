import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def ten_most_expensive_books(_data: pd.DataFrame):
    # Sort by 'Prix_Unitaire' in descending order
    top_10 = _data.sort_values(by = 'Prix_Unitaire', ascending = False).head(10)

    # Calculate the sum and product
    sum_prices = top_10[ 'Prix_Unitaire' ].sum()
    product_prices = np.prod(top_10[ 'Prix_Unitaire' ])

    print("Sum of prices of top 10 most expensive books:", sum_prices)
    print("Product of prices of top 10 most expensive books:", product_prices)


def matrix_data(_data: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    if cols is None:
        return _data
    _matrix_data = _data[ cols ].values
    print(_matrix_data)
    return _matrix_data


def cov_corr(_data: pd.DataFrame, col1: str = None, col2: str = None) -> tuple:
    if col1 is None or col2 is None:
        return 0, 0
    covariance = np.cov(_data[ col1 ], _data[ col2 ])
    correlation = np.corrcoef(_data[ col1 ], _data[ col2 ])[ 0, 1 ]

    print("Covariance:", covariance)
    print("Correlation:", correlation)

    return covariance, correlation


def scatter_plot(_data: pd.DataFrame, col1: str = None, col2: str = None):
    if col1 is None or col2 is None:
        return

    plt.scatter(_data[ col1 ], _data[ col2 ])
    col1 = col1.replace('_', ' ').title()
    col2 = col2.replace('_', ' ').title()
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f'Scatter Plot of {col1} and {col2}')
    plt.show()


def linear_regression_after_2010(_data: pd.DataFrame,
                                 col1: str = 'Prix_Unitaire',
                                 col2: str = 'Quantite_Vendue') -> tuple:

    post_2010_data = _data[ _data[ 'Annee_Publication' ] > 2010 ]

    x = post_2010_data[ [ col1 ] ]
    y = post_2010_data[ col2 ]

    model = LinearRegression()
    model.fit(x, y)

    slope = model.coef_[ 0 ]
    intercept = model.intercept_

    plt.scatter(_data[ col1 ], _data[ col2 ])

    plt.plot(_data[ col1 ], (slope * _data[ col1 ]) + intercept, color = 'red')

    col1 = col1.replace('_', ' ').title()
    col2 = col2.replace('_', ' ').title()
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f'Scatter Plot and linear regression of {col1} and {col2}')
    plt.show()

    return slope, intercept
