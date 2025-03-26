from datetime import datetime
import pytz
from TP2 import *
from Utils import *
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def cli():
    # Create the results part of the analysis report
    results: list[ str ] = [ ]

    # Retrieve the CSV data
    data = read_csv()

    # Analyze the CSV data
    (stats, mean_price_per_genre) = analyze(data)

    ##############################
    # 1. Descriptive Statistics  #
    ##############################
    descr_statistics: list[ str ] = [ ]
    descr_statistics.append(f'<h3>1. Descriptive Statistics</h3>')

    descr_statistics.append(
        'The descriptive statistics provide a snapshot of the central tendencies and variability within each variable:')

    # Print the mean price per region
    print(Style.add('The mean price per genre is:', Style.Colors.CYAN, Style.Styles.BOLD))

    descr_statistics.append(f'<h5>The mean price per genre is:</h5>')
    descr_statistics.append('<ul>')

    for col, mean in mean_price_per_genre.items():
        column_name = col.replace('_', ' ').capitalize()
        print(Style.add(f'{column_name}: {mean}€', Style.Colors.BLUE))
        descr_statistics.append(f'<li><strong>{column_name}</strong>: {mean:.2f}€</li>')
    print()

    descr_statistics.append('</ul>')
    descr_statistics.append('')

    confirm_continue()

    # Print the analyzed data for each numerical column
    print(Style.add('Analysis of each numerical column:', Style.Colors.CYAN, Style.Styles.BOLD))

    for col, stats in stats.items():
        column_name = col.replace('_', ' ').capitalize()
        print(Style.add(f"Descriptive statistics for column '{column_name}':", Style.Colors.CYAN, Style.Styles.BOLD))
        print(Style.add(f"Count: {stats.count}", Style.Colors.BLUE))
        print(Style.add(f"Mean: {stats.mean}", Style.Colors.BLUE))
        print(Style.add(f"Standard Deviation: {stats.std}", Style.Colors.BLUE))
        print(Style.add(f"Minimum: {stats.min}", Style.Colors.BLUE))
        print(Style.add(f"Q1: {stats.q1}", Style.Colors.BLUE))
        print(Style.add(f"Median: {stats.median}", Style.Colors.BLUE))
        print(Style.add(f"Q3: {stats.q3}", Style.Colors.BLUE))
        print(Style.add(f"Maximum: {stats.max}", Style.Colors.BLUE), end = '\n\n')

        descr_statistics.append(f"<h5>{column_name}:</h5>")
        descr_statistics.append('<ul>')
        descr_statistics.append(f'<li><strong>Count</strong>: {stats.count:.2f}</li>')
        descr_statistics.append(f'<li><strong>Mean</strong>: {stats.mean:.2f}</li>')
        descr_statistics.append(f'<li><strong>Standard Deviation</strong>: {stats.std:.2f}</li>')
        descr_statistics.append(f'<li><strong>Minimum</strong>: {stats.min:.2f}</li>')
        descr_statistics.append(f'<li><strong>Q1</strong>: {stats.q1:.2f}</li>')
        descr_statistics.append(f'<li><strong>Median</strong>: {stats.median:.2f}</li>')
        descr_statistics.append(f'<li><strong>Q3</strong>: {stats.q3:.2f}</li>')
        descr_statistics.append(f'<li><strong>Maximum</strong>: {stats.max:.2f}</li>')
        descr_statistics.append('</ul>')

        confirm_continue()

    results.append(''.join(descr_statistics))
    facts_statistics: list[ str ] = [ '<h5>Facts about those statistics:</h5>',
                                      '<ul>',
                                      '<li>The philosophy genre is much more expensive than other genres, and young people literature is the second most expensive.</li>'
                                      "<li>While the average publication year is relatively recent, a significant portion of books were published earlier in the dataset's timeframe.</li>",
                                      '<li>The median unit price slightly exceeds the mean, suggesting a possible skew towards higher-priced books in the dataset.</li>',
                                      '<li>The high standard deviation in the quantity sold indicates considerable variation in book sales performance, with some books selling significantly more units than others.</li>',
                                      '</ul>' ]
    results.append(''.join(facts_statistics))
    results.append('')

    ##############################
    # 2. Genre Analysis          #
    ##############################
    results.append(f'<h3>2. Genre Analysis</h3>')
    genre_analysis: list[ str ] = [ ]

    # Print the genre with the greater median of quantity of books sold
    genre, median = genre_with_best_median_sold_quantity(data)

    print(Style.add('Genre with the greater median of sold books:', Style.Colors.CYAN,
                    Style.Styles.BOLD))
    print(Style.add(f'Genre: {genre}', Style.Colors.BLUE))
    print(Style.add(f'Median: {median}', Style.Colors.BLUE), end = '\n\n')

    genre_analysis.append('<h5>Genre with the greater median of sold books:</h5>')
    genre_analysis.append('<ul>')
    genre_analysis.append(f'<li><strong>Genre</strong>: {genre}</li>')
    genre_analysis.append(f'<li><strong>Median</strong>: {median:.2f}</li>')
    genre_analysis.append('</ul>')
    results.append(''.join(genre_analysis))

    confirm_continue()
    results.append('')

    ##############################
    # 3. Most Expansive Book     #
    ##############################
    results.append(f'<h3>3. Most Expensive Book</h3>')
    most_expensive_books: list[ str ] = [ ]

    # Print the most expensive book
    book_most_expensive = find_most_expensive(data)
    print(Style.add('The most expensive book is:', Style.Colors.CYAN, Style.Styles.BOLD))
    print(Style.add(f"ISBN: {book_most_expensive.isbn}", Style.Colors.BLUE))
    print(Style.add(f"Title: {book_most_expensive.title}", Style.Colors.BLUE))
    print(Style.add(f"Author: {book_most_expensive.author}", Style.Colors.BLUE))
    print(Style.add(f"Genre: {book_most_expensive.genre}", Style.Colors.BLUE))
    print(Style.add(f"Publication Year: {book_most_expensive.publication_year}", Style.Colors.BLUE))
    print(Style.add(f"Unit Price: {book_most_expensive.unit_price}€", Style.Colors.BLUE))
    print(Style.add(f"Quantity Sold: {book_most_expensive.quantity_sold}", Style.Colors.BLUE))
    print(Style.add(f"Region: {book_most_expensive.region}", Style.Colors.BLUE))
    print(Style.add(f"Sold At: {book_most_expensive.sold_at}", Style.Colors.BLUE), end = '\n\n')

    most_expensive_books.append('<h5>The most expensive book is:</h5>')
    most_expensive_books.append('<ul>')
    most_expensive_books.append(f'<li><strong>ISBN</strong>: {book_most_expensive.isbn}</li>')
    most_expensive_books.append(f'<li><strong>Title</strong>: {book_most_expensive.title}</li>')
    most_expensive_books.append(f'<li><strong>Author</strong>: {book_most_expensive.author}</li>')
    most_expensive_books.append(f'<li><strong>Genre</strong>: {book_most_expensive.genre}</li>')
    most_expensive_books.append(f'<li><strong>Publication Year</strong>: {book_most_expensive.publication_year}</li>')
    most_expensive_books.append(f'<li><strong>Unit Price</strong>: {book_most_expensive.unit_price}€</li>')
    most_expensive_books.append(f'<li><strong>Quantity Sold</strong>: {book_most_expensive.quantity_sold}</li>')
    most_expensive_books.append(f'<li><strong>Region</strong>: {book_most_expensive.region}</li>')
    most_expensive_books.append(f'<li><strong>Sold At</strong>: {book_most_expensive.sold_at}</li>')
    most_expensive_books.append('</ul>')
    results.append(''.join(most_expensive_books))

    confirm_continue()
    results.append('')

    ##############################
    # 4. Sold Books Distribution #
    ##############################
    results.append(f'<h3>4. Sold Books Distribution</h3>')
    sold_books_distribution: list[ str ] = [ ]

    # Plot the distribution of sold quantities
    plot_sold_quantity_distribution(data)
    sold_books_distribution.append('<div class="center">')
    sold_books_distribution.append('<img src="templates/assets/sold_quantity_distribution.png"'
                                   ' alt="Chart showing the distribution of sold books.">')
    sold_books_distribution.append('</div>')
    results.append(''.join(sold_books_distribution))

    confirm_continue()
    results.append('')

    ##############################
    # 5. Price Analysis          #
    ##############################
    results.append(f'<h3>5. Price Analysis</h3>')
    price_analysis: list[ str ] = [ ]

    # Estimate the probability that a book costs more than 20 euros
    probability_above_20_euros = estimate_probability_above_price(data, 20)
    print(Style.add(f"\nEstimated probability that a book costs more than 20€: {probability_above_20_euros:.4f}", Style.Colors.CYAN, Style.Styles.BOLD))

    price_analysis.append(
        f'<strong>The estimated probability that a book costs more than 20€ is</strong> {probability_above_20_euros:.4f}')
    price_analysis.append('<br>')

    sum_prices, product_prices = ten_most_expensive_books(data)

    price_analysis.append(
        f'<strong>The sum of prices of top 10 most expensive books is</strong>: {sum_prices:.2f}€')
    price_analysis.append('<br>')
    price_analysis.append(
        f'<strong>The product of prices of the top 10 most expensive books is</strong>: {product_prices:.2f}€')
    price_analysis.append('<br>')
    price_analysis.append('<br>')

    # TODO -> finish this part here!
    matrix_prices = matrix_data(data,
                                cols = [ 'Prix_Unitaire', 'Quantite_Vendue' ],
                                groupBy = 'Region')
    prices_table = matrix_prices.to_html()
    price_analysis.append(prices_table)
    price_analysis.append('<br>')

    covariance, correlation = cov_corr(data,
                                       col1 = 'Prix_Unitaire',
                                       col2 = 'Quantite_Vendue')
    price_analysis.append(f'<p>The correlation is {correlation:.2f} and the covariance is {covariance[0][0]:.2f}.</p>')
    print(Style.add(f'correlation: {correlation:.2f}', Style.Colors.CYAN, Style.Styles.BOLD), end = '\n\n')
    scatter_plot(data,
                 col1 = 'Prix_Unitaire',
                 col2 = 'Quantite_Vendue')

    price_analysis.append('<div class="center">')
    price_analysis.append('<img src="templates/assets/scatter_price_quantity-sold.png"'
        ' alt="Scatter plot showing the books sold according to their prices.">')
    price_analysis.append('</div>')
    price_analysis.append('<p></p>')
    slope, intercept = linear_regression_after_2010(data)
    print(f'slope: {slope}\nintercept: {intercept}')
    price_analysis.append(f'<div>The slope is {slope} and the intercept is {intercept}.</div>')

    price_analysis.append('<p></p>')
    price_analysis.append('<p></p>')
    price_analysis.append('<div class="center">')
    price_analysis.append('<img src="templates/assets/scatter_price_quantity-sold_linear-regression.png"'
        ' alt="Scatter plot showing the books sold according to their prices with a linear regression.">')
    price_analysis.append('</div>')

    price_analysis.append(f'<div>According to the linear regression, we can say that the most expensive books tend to sell better.</div>')

    results.append(''.join(price_analysis))
    results.append('')

    ##############################
    # 6. Selling dynamics          #
    ##############################
    results.append(f'<h3>5. Selling dynamics</h3>')
    selling_dynamics: list[ str ] = [ ]

    # Draw a Fast Fourier Transformation per date
    plot_fft_of_sales(data)

    selling_dynamics.append('<div class="center">')
    selling_dynamics.append('<img src="templates/assets/fast_fourier_weekly.png" '
                            'alt="Fast Fourier Weekly Price Analysis">')
    selling_dynamics.append('</div>')

    selling_dynamics.append('<div>According to this Fast Fourier Transformation, there is a slight increase in quantity of books sold every 3 days and a half.</div>')
    selling_dynamics.append('<div>Except for this increase, it seems that the data are not very regular in that weekly visualization.</div>')

    # Draw a Fast Fourier Transformation per month
    plot_fft_of_monthly_sales(data)

    selling_dynamics.append('<div class="center">')
    selling_dynamics.append('<img src="templates/assets/fast_fourier_monthly.png" '
                            'alt="Fast Fourier Monthly Price Analysis">')
    selling_dynamics.append('</div>')

    selling_dynamics.append(
        '<div>According to this other plot, there is also a slight increase in quantity of books sold every 3 months approximately.</div>')
    selling_dynamics.append(
        '<div>That increase may correspond to special moments of the year, like feasts or promotion times.</div>')
    selling_dynamics.append(
        '<div>But apart that increase, the data are not extremely consistent in a monthly repartition.</div>')


    results.append(''.join(selling_dynamics))
    results.append('')

    confirm_continue()

    publish_template(
        title = 'TP2',
        overview = '''This report presents an in-depth analysis of book sales data collected over a specific period (from 1990 to 2024).<br>
        <br>
        The goal is to provide valuable insights into market trends, consumer preferences, and potential opportunities within the publishing industry. By examining various factors influencing book sales, including genre, price, publication year, and region, this report aims to illuminate key patterns and inform strategic decision-making for publishers, retailers, and authors.''',
        data_used = '''The analysis is based on a comprehensive dataset containing detailed information about individual book sales transactions. The data encompasses the following variables:<br>
        <br>
        <ul>
        <li><strong>ISBN</strong>: Unique book identifier.</li>
        <li><strong>Titre</strong>: Title of the book.</li>
        <li><strong>Auteur</strong>: Name of the author.</li>
        <li><strong>Genre</strong>: The literary genre to which each book belongs, categorized based on</li> established industry standards (e.g.: Roman, Science-fiction, Jeunesse, etc.).
        <li><strong>Annee_Publication</strong>: The year of publication for each book.</li>
        <li><strong>Prix_Unitaire</strong>: The unit price (in Euros) at which each book was sold.</li>
        <li><strong>Quantite_Vendue</strong>: The number of units sold for each specific book.</li>
        <li><strong>Region</strong>: The geographical region (in France) where the sale occurred.</li>
        <li><strong>Date_Vente</strong>: Date in which the book was sold.</li>
        </ul>''',
        results = results,
        conclusion = '''This analysis reveals several key insights into book sales trends:
        <ul>
        <li>A strong preference for History genre among consumers.</li>
        <li>Potential for growth in genres with lower median quantity sold.</li>
        <li>A good opportunity with more expansive books.</li>
        <li>Interesting dynamics in important moment of the year, maybe festivities and promotion times.</li>
        <li>The need for a deeper understanding of pricing strategies and factors influencing unit price variations.</li>
        </ul>
        <br>
        Further research could delve deeper into these findings, utilizing advanced statistical techniques and exploring the relationship between variables like genre, publication year, and sales performance. These insights can guide publishers in identifying promising trends, developing targeted marketing strategies, and ultimately contributing to the growth and success of the publishing industry.''',
        footer = '© Antoine de Barbarin. All rights reserved.',
    )

    return_menu()


def publish_template(title: str, overview: str, data_used: str, results: list[ str ], conclusion: str, footer: str):
    # Initialize a template environment from a directory
    env = Environment(loader = FileSystemLoader('CLI/TP2/templates'))

    # Load the templates
    html_template = env.get_template('test.tmpl.jinja')
    css_template = env.get_template('style.css.jinja')

    # Render the templates with document data
    document = Document(title, overview, data_used, results, conclusion, footer)
    html_document = html_template.render(document = document)
    css_document = css_template.render(document = document)

    # Print the rendered template for testing
    # print(html_document)

    # Generate the current date in 'YYYY-MM-DD' format
    current_date = datetime.now(tz = pytz.timezone('Europe/Paris')).strftime('%Y-%m-%d')

    # Generate PDF from HTML/CSS templates
    html_to_pdf(html_content = html_document, output_path = f'books-report_{current_date}.pdf', css_content = css_document)


class Document:

    def __init__(self, title: str, overview: str, data_used: str, results: list[ str ], conclusion: str, footer: str):
        self.title = title
        self.overview = overview
        self.data_used = data_used
        self.results = results
        self.conclusion = conclusion
        self.footer = footer


def html_to_pdf(html_content: str, output_path: str, css_content: str = None):
    if css_content is None:
        HTML(string = html_content).write_pdf(output_path)
        return
    font_config = FontConfiguration()

    # CLI/TP2 path
    base_url = os.path.dirname(os.path.realpath(__file__))

    html = HTML(string = html_content, base_url = base_url)
    css = CSS(string = css_content, font_config = font_config, base_url = base_url)
    html.write_pdf(output_path, stylesheets = [ css ], font_config = font_config)
