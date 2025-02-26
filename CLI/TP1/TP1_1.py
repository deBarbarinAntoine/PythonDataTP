from TP1 import *

def cli():
	
	print(Style.add('Retrieving data...', Style.Colors.CYAN, Style.Styles.BOLD), end = '\n\n')
	data = read_csv()
	
	print(Style.add('5 first rows:', Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(str(first_5(data)), Style.Colors.BLUE))
	
	return_menu()