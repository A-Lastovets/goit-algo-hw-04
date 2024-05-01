import colorama
from colorama import Fore, Back
from pathlib import Path
colorama.init(autoreset=True)

try:
    parent_folder_path = Path('.')


    def parse_folder(path):

        for element in path.iterdir():
            if element.is_dir():
                print(Fore.RED+Back.GREEN + f"Parse folder: This is folder - {element.name}")

            if element.is_file():
                print(Fore.BLUE+Back.YELLOW + f"Parse folder: This is file - {element.name}")
except FileNotFoundError:
    print("File not found")

parse_folder(parent_folder_path)
