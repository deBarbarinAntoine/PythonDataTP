from TP1 import *


def cli():
	
	data = read_csv()
	
	print(Style.add('data info:', Style.Colors.CYAN, Style.Styles.BOLD))
	rows, columns = info(data)
	
	confirm_continue()
	
	print(Style.add('describe data:', Style.Colors.CYAN, Style.Styles.BOLD))
	describe(data)
	print()
	
	confirm_continue()
	
	print(Style.add(f'line count: {rows}', Style.Colors.CYAN, Style.Styles.BOLD))
	print(Style.add(f'column count: {columns}', Style.Colors.CYAN, Style.Styles.BOLD))
	print()
	
	return_menu()