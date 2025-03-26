from TP2 import *
from Utils import *


def cli():

    # Retrieve the CSV data
    data = read_csv()

    # Draw a Fast Fourier Transformation per date
    plot_fft_of_sales(data)

    confirm_continue()

    # Draw a Fast Fourier Transformation per month
    plot_fft_of_monthly_sales(data)

    return_menu()

