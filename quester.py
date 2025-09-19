#!/usr/bin/env python3
"""
Quester - A Python Text Console Game
A colorful text-based adventure game using colorama for enhanced visual experience.
"""

import os
import random
import sys
import time
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

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

class Game:
    """Main game class."""
    
    def __init__(self):
        self.player = None
        self.quests_completed = 0
        self.running = True
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_title(self):
        """Print the game title with colorful ASCII art."""
        title = f"""
{Fore.MAGENTA}{Style.BRIGHT}
 ██████╗ ██╗   ██╗███████╗███████╗████████╗███████╗██████╗ 
██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║   ██║██║   ██║█████╗  ███████╗   ██║   █████╗  ██████╔╝
██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║   ██║   ███████╗██║  ██║
 ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{Fore.CYAN}      A Colorful Text Adventure Game{Style.RESET_ALL}
"""
        print(title)
    
    def get_user_input(self, prompt, options=None):
        """Get user input with colored prompt."""
        if options:
            print(f"\n{Fore.CYAN}Options:")
            for i, option in enumerate(options, 1):
                print(f"{Fore.WHITE}{i}. {Fore.GREEN}{option}")
        
        while True:
            try:
                user_input = input(f"\n{Fore.YELLOW}{prompt}{Fore.WHITE}: ").strip()
                if options:
                    choice = int(user_input)
                    if 1 <= choice <= len(options):
                        return choice - 1
                    else:
                        print(f"{Fore.RED}Invalid choice. Please select 1-{len(options)}")
                else:
                    return user_input
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number.")
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}Game interrupted. Goodbye!")
                sys.exit(0)
    
    def create_character(self):
        """Character creation process."""
        self.clear_screen()
        self.print_title()
        print(f"{Fore.GREEN}{Style.BRIGHT}=== Character Creation ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}Welcome, brave adventurer!")
        
        name = self.get_user_input("Enter your character's name")
        while not name or len(name) < 2:
            print(f"{Fore.RED}Name must be at least 2 characters long.")
            name = self.get_user_input("Enter your character's name")
        
        self.player = Player(name)
        print(f"\n{Fore.GREEN}✨ Character '{name}' created successfully!")
        time.sleep(1.5)
    
    def show_main_menu(self):
        """Display the main game menu."""
        self.clear_screen()
        self.print_title()
        
        if self.player:
            self.player.display_stats()
            print(f"\n{Fore.MAGENTA}Quests Completed: {self.quests_completed}")
        
        options = [
            "🗡️  Go on a Quest",
            "🏪 Visit Shop",
            "🧙 Character Stats",
            "💤 Rest (Restore Health)",
            "🚪 Exit Game"
        ]
        
        choice = self.get_user_input("What would you like to do?", options)
        return choice
    
    def go_on_quest(self):
        """Quest system with random encounters."""
        quest_types = [
            {
                "name": "Goblin Camp Raid",
                "description": "Clear out a goblin camp terrorizing nearby villages",
                "difficulty": "Easy",
                "rewards": {"exp": 50, "gold": 30, "items": ["Rusty Sword", "Health Potion"]}
            },
            {
                "name": "Dragon's Lair",
                "description": "Face the mighty dragon in its lair",
                "difficulty": "Hard",
                "rewards": {"exp": 200, "gold": 100, "items": ["Dragon Scale", "Magic Gem"]}
            },
            {
                "name": "Mysterious Forest",
                "description": "Explore the enchanted forest and its secrets",
                "difficulty": "Medium",
                "rewards": {"exp": 100, "gold": 60, "items": ["Elven Bow", "Healing Herb"]}
            },
            {
                "name": "Ancient Ruins",
                "description": "Investigate ancient ruins filled with traps and treasures",
                "difficulty": "Medium",
                "rewards": {"exp": 120, "gold": 80, "items": ["Ancient Artifact", "Gold Ring"]}
            }
        ]
        
        quest = random.choice(quest_types)
        
        print(f"\n{Fore.BLUE}{Style.BRIGHT}=== Quest Available ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}Quest: {Fore.YELLOW}{quest['name']}")
        print(f"{Fore.WHITE}Description: {Fore.CYAN}{quest['description']}")
        print(f"{Fore.WHITE}Difficulty: {Fore.RED if quest['difficulty'] == 'Hard' else Fore.YELLOW if quest['difficulty'] == 'Medium' else Fore.GREEN}{quest['difficulty']}")
        
        accept = self.get_user_input("Do you accept this quest?", ["Yes", "No"])
        
        if accept == 0:  # Yes
            print(f"\n{Fore.GREEN}🎯 Quest accepted! Embarking on adventure...")
            time.sleep(2)
            
            # Simulate quest with random outcome
            success_chance = 0.8 if quest['difficulty'] == 'Easy' else 0.6 if quest['difficulty'] == 'Medium' else 0.4
            
            if random.random() < success_chance:
                print(f"{Fore.GREEN}{Style.BRIGHT}🎉 Quest completed successfully!")
                
                # Award rewards
                self.player.gain_experience(quest['rewards']['exp'])
                self.player.gold += quest['rewards']['gold']
                
                reward_item = random.choice(quest['rewards']['items'])
                self.player.add_item(reward_item)
                
                print(f"{Fore.YELLOW}💰 Gained {quest['rewards']['gold']} gold")
                print(f"{Fore.BLUE}⭐ Gained {quest['rewards']['exp']} experience")
                
                self.quests_completed += 1
            else:
                print(f"{Fore.RED}{Style.BRIGHT}💀 Quest failed!")
                damage = random.randint(10, 30)
                died = self.player.take_damage(damage)
                print(f"{Fore.RED}❤️ You took {damage} damage!")
                
                if died:
                    print(f"{Fore.RED}{Style.BRIGHT}💀 You have died! Game Over!")
                    time.sleep(3)
                    self.running = False
                    return
        else:
            print(f"{Fore.YELLOW}Quest declined. Maybe next time!")
        
        input(f"\n{Fore.WHITE}Press Enter to continue...")
    
    def visit_shop(self):
        """Shop system for buying items."""
        shop_items = [
            {"name": "Health Potion", "price": 25, "description": "Restores 50 health"},
            {"name": "Magic Scroll", "price": 50, "description": "Grants 25 experience"},
            {"name": "Lucky Charm", "price": 100, "description": "Increases quest success rate"},
            {"name": "Steel Sword", "price": 150, "description": "A sturdy weapon for adventures"},
        ]
        
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}=== Welcome to the Shop ==={Style.RESET_ALL}")
        print(f"{Fore.WHITE}Your Gold: {Fore.YELLOW}💰 {self.player.gold}")
        
        options = [f"{item['name']} - {item['price']} gold ({item['description']})" for item in shop_items]
        options.append("Leave Shop")
        
        choice = self.get_user_input("What would you like to buy?", options)
        
        if choice < len(shop_items):
            item = shop_items[choice]
            if self.player.gold >= item['price']:
                self.player.gold -= item['price']
                self.player.add_item(item['name'])
                
                # Apply item effects
                if item['name'] == "Health Potion":
                    self.player.heal(50)
                    print(f"{Fore.GREEN}❤️ Health restored!")
                elif item['name'] == "Magic Scroll":
                    self.player.gain_experience(25)
                
                print(f"{Fore.GREEN}✅ Purchase successful!")
            else:
                print(f"{Fore.RED}❌ Not enough gold!")
        else:
            print(f"{Fore.YELLOW}👋 Thanks for visiting!")
        
        input(f"\n{Fore.WHITE}Press Enter to continue...")
    
    def rest(self):
        """Rest to restore health."""
        print(f"\n{Fore.BLUE}😴 You rest at a nearby inn...")
        time.sleep(2)
        
        cost = 10
        if self.player.gold >= cost:
            self.player.gold -= cost
            self.player.health = self.player.max_health
            print(f"{Fore.GREEN}✨ Health fully restored! (Cost: {cost} gold)")
        else:
            # Free but partial rest
            heal_amount = random.randint(20, 40)
            self.player.heal(heal_amount)
            print(f"{Fore.YELLOW}💤 You rest under the stars and recover {heal_amount} health (Free)")
        
        input(f"\n{Fore.WHITE}Press Enter to continue...")
    
    def run(self):
        """Main game loop."""
        self.clear_screen()
        self.print_title()
        
        print(f"{Fore.GREEN}Welcome to Quester!")
        print(f"{Fore.WHITE}A colorful text-based adventure game.")
        input(f"\n{Fore.YELLOW}Press Enter to start...")
        
        # Character creation
        self.create_character()
        
        # Main game loop
        while self.running and self.player.health > 0:
            choice = self.show_main_menu()
            
            if choice == 0:  # Quest
                self.go_on_quest()
            elif choice == 1:  # Shop
                self.visit_shop()
            elif choice == 2:  # Stats
                input(f"\n{Fore.WHITE}Press Enter to continue...")
            elif choice == 3:  # Rest
                self.rest()
            elif choice == 4:  # Exit
                self.running = False
        
        # Game over
        self.clear_screen()
        self.print_title()
        
        if self.player.health <= 0:
            print(f"{Fore.RED}{Style.BRIGHT}💀 GAME OVER 💀")
            print(f"{Fore.WHITE}Your brave adventurer has fallen...")
        else:
            print(f"{Fore.GREEN}{Style.BRIGHT}👋 Thanks for playing!")
            print(f"{Fore.WHITE}Final Stats:")
            self.player.display_stats()
            print(f"{Fore.MAGENTA}Quests Completed: {self.quests_completed}")
        
        print(f"\n{Fore.CYAN}Come back anytime for more adventures!")

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