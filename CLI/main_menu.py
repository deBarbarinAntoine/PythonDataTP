from CLI import *
from Utils import *


def cli():
	while True:
		print('-' * 31)
		print(Style.add(f"Welcome to Antoine's Python Data TP!)"), Style.Colors.CYAN, Style.Styles.BOLD)
		print('-' * 31)
		menu = MenuCLI.new(
			'TP1.1 Load and explore the data',
			'TP1.2 Understand the data structure',
			'TP1.3 Identify and handle missing data',
			'TP1.4 Rapid exploration',
			'TP1.5 Advanced topics',
			title='Main Menu'
		)
		match menu.run():
			case 0:
				print("Bye!")
				exit(0)
			case 1:
				TP1_1.cli()
			case 2:
				TP1_2.cli()
			case 3:
				TP1_3.cli()
			case 4:
				TP1_4.cli()
			case 5:
				TP1_5.cli()