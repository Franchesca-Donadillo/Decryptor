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

# ask user input
# loop all throughout the user input
# change * into a
# change & into e
# change # into i
# change + into o
# change ! into u
# add partition
# print the decrypted text of the user