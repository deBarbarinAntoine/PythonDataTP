import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_fft_of_sales(_data: pd.DataFrame) -> None:
    """
    Plots the FFT of sales data to analyze dominant frequencies.

    :param _data: DataFrame containing the data for multiple books.
    """
    # Convert Date_Vente to datetime
    _data['Date_Vente'] = pd.to_datetime(_data['Date_Vente'])

    # Aggregate sales by day
    daily_sales = _data.groupby(_data['Date_Vente'].dt.date)['Quantite_Vendue'].sum()
    daily_sales = daily_sales.sort_index()

    # Convert the sales data to a numpy array
    sales_data = daily_sales.values

    # Compute the FFT
    fft_result = np.fft.fft(sales_data)

    # Compute the frequencies corresponding to the FFT result
    freqs = np.fft.fftfreq(len(sales_data), d = 7)

    # Ignore the 0 frequency when plotting
    mask = freqs > 0
    freqs_positive = freqs[mask]
    fft_positive = np.abs(fft_result)[mask]

    # Convert frequencies to cycles per week
    frequencies_weekly = freqs_positive * 7

    # Plot the FFT result
    plt.figure(figsize = (10, 6))
    plt.plot(frequencies_weekly,fft_positive)
    plt.title('FFT of Sales Data')
    plt.xlabel('Frequency (1/week)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.savefig('CLI/TP2/templates/assets/fast_fourier_weekly.png', bbox_inches='tight')
    plt.close()


def plot_fft_of_monthly_sales(_data: pd.DataFrame) -> None:
    """
    Plots the FFT of sales data to analyze dominant monthly frequencies.

    :param _data: DataFrame containing the data for multiple books.
    """
    _data['Date_Vente'] = pd.to_datetime(_data['Date_Vente'])

    # Aggregate sales by month
    _data.set_index('Date_Vente', inplace = True)
    monthly_sales = _data.resample('ME')['Quantite_Vendue'].sum()

    # Convert to numpy arrays
    months = np.array(monthly_sales.index)
    sales_data = monthly_sales.values

    # Compute FFT
    fft_result = np.fft.fft(sales_data)

    # Calculate frequencies
    freqs = np.fft.fftfreq(len(fft_result), d = 1)

    # Ignore the 0 frequency when plotting
    mask = freqs > 0
    freqs_positive = freqs[mask]
    fft_positive = np.abs(fft_result)[mask]

    # Plotting
    plt.figure(figsize = (10, 6))
    plt.plot(freqs_positive, fft_positive)
    plt.title('FFT of Monthly Sales Data')
    plt.xlabel('Frequency (1/month)')
    plt.ylabel('Amplitude')

    plt.grid(True)
    plt.savefig('CLI/TP2/templates/assets/fast_fourier_monthly.png', bbox_inches='tight')
    plt.close()