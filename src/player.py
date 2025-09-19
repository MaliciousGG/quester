from colorama import Fore, Style
import time
class Player:
    """Player class to manage character stats and inventory."""

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.experience = 0
        self.gold = 50
        self.inventory = []

    def gain_experience(self, amount):
        """Add experience and handle level ups."""
        self.experience += amount
        # Level up every 100 experience points
        while self.experience >= self.level * 100:
            self.experience -= self.level * 100
            self.level += 1
            self.max_health += 20
            self.health = self.max_health  # Full heal on level up
            print(f"{Fore.YELLOW}{Style.BRIGHT}🎉 Level Up! You are now level {self.level}!{Style.RESET_ALL}")
            time.sleep(1.5)

    def heal(self, amount):
        """Heal the player."""
        self.health = min(self.max_health, self.health + amount)

    def take_damage(self, amount):
        """Take damage."""
        self.health = max(0, self.health - amount)
        return self.health <= 0

    def add_item(self, item):
        """Add item to inventory."""
        self.inventory.append(item)
        print(f"{Fore.GREEN}📦 Added {item} to inventory!")

    def display_stats(self):
        """Display player statistics."""
        health_bar = "█" * (self.health // 5) + "░" * ((self.max_health - self.health) // 5)
        print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Character Stats ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}Name: {Fore.YELLOW}{self.name}")
        print(f"{Fore.WHITE}Level: {Fore.YELLOW}{self.level}")
        print(f"{Fore.WHITE}Health: {Fore.RED}{health_bar} {self.health}/{self.max_health}")
        print(f"{Fore.WHITE}Experience: {Fore.BLUE}{self.experience}/{self.level * 100}")
        print(f"{Fore.WHITE}Gold: {Fore.YELLOW}💰 {self.gold}")
        if self.inventory:
            print(f"{Fore.WHITE}Inventory: {Fore.GREEN}{', '.join(self.inventory)}")
        else:
            print(f"{Fore.WHITE}Inventory: {Fore.RED}Empty")