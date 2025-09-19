#!/usr/bin/env python3


import os
import random
import sys
import time
from colorama import Fore, Back, Style, init

from src.game import Game

# Initialize colorama for cross-platform colored output
init(autoreset=True)




def main():
    """Main entry point."""
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Game interrupted. Goodbye!")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")
        print(f"{Fore.YELLOW}Please report this issue!")

if __name__ == "__main__":
    main()