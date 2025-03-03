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
    descr_statistics: list[str] = []
    descr_statistics.append(f'<h3>Descriptive Statistics</h3>')
    
    descr_statistics.append('The descriptive statistics provide a snapshot of the central tendencies and variability within each variable:')
    
    # Print the mean price per region
    print(Style.add('The mean price per genre is:', Style.Colors.CYAN, Style.Styles.BOLD))
    
    descr_statistics.append(f'<h5>The mean price per genre is:</h5>')
    descr_statistics.append('<ul>')
    
    for col, mean in mean_price_per_genre.items():
        print(Style.add(f'{col}: {mean}', Style.Colors.BLUE))
        descr_statistics.append(f'<li>{col}: {mean:.2f}</li>')
    print()
    
    descr_statistics.append('</ul>')
    descr_statistics.append('')
    
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
        
        descr_statistics.append(f"<h5>{col}:</h5>")
        descr_statistics.append('<ul>')
        descr_statistics.append(f'<li>Count: {stats.count:.2f}</li>')
        descr_statistics.append(f'<li>Mean: {stats.mean:.2f}</li>')
        descr_statistics.append(f'<li>Standard Deviation: {stats.std:.2f}</li>')
        descr_statistics.append(f'<li>Minimum: {stats.min:.2f}</li>')
        descr_statistics.append(f'<li>Q1: {stats.q1:.2f}</li>')
        descr_statistics.append(f'<li>Median: {stats.median:.2f}</li>')
        descr_statistics.append(f'<li>Q3: {stats.q3:.2f}</li>')
        descr_statistics.append(f'<li>Maximum: {stats.max:.2f}</li>')
        descr_statistics.append('</ul>')
        descr_statistics.append('')
        
        confirm_continue()
        
    results.append(''.join(descr_statistics))
    
    ##############################
    # 2. Genre Analysis          #
    ##############################
    results.append(f'<h3>Genre Analysis</h3>')
    
    # Print the genre with the greater median of quantity of books sold
    genre, median = genre_with_best_median_sold_quantity(data)
    
    print(Style.add('The genre with the greater median of quantity of books sold is:', Style.Colors.CYAN,
                    Style.Styles.BOLD))
    print(Style.add(f'Genre: {genre}', Style.Colors.BLUE))
    print(Style.add(f'Median: {median}', Style.Colors.BLUE), end = '\n\n')
    
    results.append('<h5>The genre with the greater median of quantity of books sold is:</h5>')
    results.append('<ul>')
    results.append(f'<li>Genre: {genre}</li>')
    results.append(f'<li>Median: {median:.2f}</li>')
    results.append('</ul>')
    results.append('')
    
    confirm_continue()
    
    ##############################
    # 3. Most Expansive Book     #
    ##############################
    results.append(f'<h3>Most Expansive Book</h3>')
    
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
    
    results.append('<h5>The most expensive book is:</h5>')
    results.append('<ul>')
    results.append(f'<li>ISBN: {book_most_expensive.isbn}</li>')
    results.append(f'<li>Title: {book_most_expensive.title}</li>')
    results.append(f'<li>Author: {book_most_expensive.author}</li>')
    results.append(f'<li>Genre: {book_most_expensive.genre}</li>')
    results.append(f'<li>Publication Year: {book_most_expensive.publication_year}</li>')
    results.append(f'<li>Unit Price: {book_most_expensive.unit_price}</li>')
    results.append(f'<li>Quantity Sold: {book_most_expensive.quantity_sold}</li>')
    results.append(f'<li>Region: {book_most_expensive.region}</li>')
    results.append(f'<li>Sold At: {book_most_expensive.sold_at}</li>')
    results.append('</ul>')
    results.append('')
    
    confirm_continue()
    
    ##############################
    # 4. Sold Books Distribution #
    ##############################
    results.append(f'<h3>Sold Books Distribution</h3>')
    
    # Plot the distribution of sold quantities
    plot_sold_quantity_distribution(data)
    results.append('<img alt="Chart showing the distribution of quantity of books sold.">')
    results.append('')
    
    confirm_continue()
    
    ##############################
    # 5. Price Analysis          #
    ##############################
    results.append(f'<h3>Price Analysis</h3>')
    
    # Estimate the probability that a book costs more than 20 euros
    probability_above_20_euros = estimate_probability_above_price(data, 20)
    print(Style.add(f"\nEstimated probability that a book costs more than 20 euros: {probability_above_20_euros:.4f}",
                    Style.Colors.CYAN, Style.Styles.BOLD))
    results.append(f'Estimated probability that a book costs more than 20 euros: {probability_above_20_euros:.4f}')
    results.append('')
    
    confirm_continue()
    
    publish_template(
        title = 'TP2 - Part 1',
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
    print(html_document)
    
    # Generate PDF from HTML/CSS templates
    html_to_pdf(html_content = html_document, output_path = 'test.pdf', css_content = css_document)


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
    html = HTML(string = html_content)
    css = CSS(string = css_content, font_config = font_config)
    html.write_pdf(output_path, stylesheets = [ css ], font_config = font_config)
