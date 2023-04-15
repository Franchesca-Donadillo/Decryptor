# Franchesca Marie Donadillo
# BSCPE 1-5
# ASSIGNMENT 2_Problem 2 - Decryption

# import for design
from rich.console import Console
from rich.theme import Theme
from rich import print

# encode title
design = Theme({"title": "bold magenta", "decrypt": "underline bold yellow", "blinky": "bold green blink"})
console = Console(theme = design)

title = "Problem_2 - Decryption"
new_title = title.center(55).upper()
console.print("\n" + new_title + "\n", style = "title")

# ask user input
user_input = input("Enter some characters: ")
output = ""

# loop all throughout the user input
# change * into a
# change & into e
# change # into i
# change + into o
# change ! into u
# add partition
# print the decrypted text of the user