import os


def take_input(msg = ''):
	val = input(msg)
	return val

def take_float(msg = ''):
	val = take_input(msg)
	try:
		return float(val)
	except ValueError as e:
		raise e

def take_int(msg = ''):
	while True:
		val = take_input(msg)
		try:
			return int(val)
		except ValueError:
			continue

def set_precision(val, precision = 2):
	return round(val, precision)

def return_menu():
	print("type [ENTER] to return")
	input()
	return

def confirm_continue():
	print("type [ENTER] to continue")
	input()
	return

def clear():
	# Windows
	if os.name == 'nt':
		_ = os.system('cls')
	# other OS
	else:
		_ = os.system('clear')