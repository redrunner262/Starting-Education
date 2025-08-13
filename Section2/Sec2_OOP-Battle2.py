# IMPORTS
import random
# from . import Sec2_OOP_Characters_Weapons

# GLOBAL FUNCTIONS
def roll_die_six():
    return random.randint(1, 6)

def roll_die_five():
    return random.randint(1, 5)

def roll_die_four():
    return random.randint(1, 4)

def roll_die_three():
    return random.randint(1, 3)

# CLASSES
# CHARACTER CLASSES

class Character:
    def __init__(self, name, health = 30, strength = 0, defense = 0, is_alive = True, weapon_equipped = None, limited_weapon_equipped = None):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.is_alive = is_alive
        self.weapon_equipped = weapon_equipped
        self.limited_weapon_equipped = limited_weapon_equipped

    def __repr__(self):
        return f"{self.name} | Health: {self.health} | Strength: {self.strength} | Defense: {self.defense} | Alive: {self.is_alive}"
    
    def modify_health_amount(self, amount):
        self.health += amount
        return self
    
    def change_health(self, amount):
        health_direction = 'decreased' if amount < 0 else 'increased'
        print(f"{self.name}'s health {health_direction} by {abs(amount)}.")
        print(f"{self.name}'s health is now {0 if self.health <= 0 else self.health}.")
        if self.health + amount > 0:
            self.health += amount
        else:
            self.health = 0
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} has been defeated!")
        elif amount > 0:
            print(f"{self.name}'s health is now {self.health}.")
        else:
            return self

    def defend(self):
        def_boost = random.randint(1, 4)
        defense_value = self.defense + def_boost
        print(f"{self.name} defends and increases defense by {def_boost}. New defense: {defense_value}.")
        return defense_value

    def attack(self, target):
        atk_boost = random.randint(1, 3)
        attack_strength = self.strength + atk_boost
        if attack_strength <= 0:
            print(f"\n{self.name}'s attack is ineffective.")
            return attack_strength
        else:
            print(f"\n{self.name} gets an attack boost of {atk_boost} and attacks {target.name} with {attack_strength} strength!")
        return attack_strength
    
    def counter(self, countering_player, countered_player):
        print(f"\n{countering_player.name} attempts to counter the attack!")
        counter_damage_determination = roll_die_six()
        if counter_damage_determination <= 3:
            print("Counterattack was unsuccessful...\n")
            return 0
        elif counter_damage_determination <= 5:
            counter_damage_value = 2
        else:
            counter_damage_value = 4
        print(f"\n{countering_player.name} counter attacks {countered_player.name} for {counter_damage_value} damage!")
        return counter_damage_value
        # After this function, call the "change_health" function on the countered player, using this function's returned value.
    
    msg_ltd_weapon_depleted = "" # How can I store an f-string with the 'depleted' message in both armed_attack and armed_defend functions? It is the same message so I may as well factor it out, but using 'self.[attribute] in an f-string in a variable results in a warning underline.

    def armed_attack(self, target):
        if self.limited_weapon_equipped:
            armed_attack_power = self.strength + self.limited_weapon_equipped.attack_power_additional
            print(f"{self.name} attacks {target.name} with {self.weapon.item_name}, giving a total strength of {armed_attack_power}!")
            if armed_attack_power < 0:
                armed_attack_power = 0
            self.limited_weapon_equipped.uses_remaining -= 1
            if self.limited_weapon_equipped.uses_remaining <= 0:
                # 'Depleted' message
                print(f"{self.name} depleted his limited-use weapon's uses. {self.limited_weapon_equipped.item_name.capitalize()} will be unequipped after this action.")
                self.limited_weapon_equipped = None
        else:
            print(f"{self.name} cannot perform an armed attack because no limited-use weapon is equipped.")
            armed_attack_power = 0
        return armed_attack_power
    
    def armed_defend(self):
        if self.limited_weapon_equipped:
            armed_defense_power = self.defense + self.limited_weapon_equipped.defense_additional
            self.limited_weapon_equipped.uses_remaining -= 1
            print(f"{self.name} defends with {self.limited_weapon_equipped.item_name} and increases defense by {armed_defense_power}. New defense: {self.defense}. Remaining limited-use weapon uses: {self.limited_weapon_equipped.uses_remaining}.")
            if self.limited_weapon_equipped.uses_remaining <= 0:
                # 'Depleted' message
                print(f"{self.name} depleted his limited-use weapon's uses. {self.limited_weapon_equipped.item_name.capitalize()} will be unequipped.")
                self.limited_weapon_equipped = None
        else:
            print(f"{self.name} cannot perform an armed defend because no limited-use weapon is equipped.")
        return armed_defense_power
    
    def stats(self):
        attributes = self.__dict__
        for key in attributes:
            val = attributes[key]
            print(f"{key.capitalize()}: {val}")

class Char_Type_Jedi(Character):
    def __init__(self, name, health = 30, strength = 5, defense = 5, char_type = "Jedi", weapon_equipped = None, limited_weapon_equipped = None):
        super().__init__(name, health, weapon_equipped, limited_weapon_equipped)
        self.strength = strength
        self.defense = defense
        self.char_type = char_type

class Char_Type_Sith(Character):
    def __init__(self, name, health = 30, strength = 7, defense = 3, char_type = "Sith", weapon_equipped = None, limited_weapon_equipped = None):
        super().__init__(name, health, weapon_equipped, limited_weapon_equipped)
        self.strength = strength
        self.defense = defense
        self.char_type = char_type

# WEAPON CLASSES

class Weapon:
    def __init__(self, item_name = "Basic Knife", attack_power_additional = 1, defense_additional = 1, char_type = "Neutral", limited_use = False):
        self.item_name = item_name
        self.attack_power_additional = attack_power_additional # Additional attack power provided by the weapon
        self.defense_additional = defense_additional # Additional defense provided by the weapon
        self.char_type = char_type # Character type that benefits most from use of the weapon (e.g., Jedi, Sith, Neutral)
        self.limited_use = limited_use  # Indicates whether the weapon has limited uses

class Unlimited_Weapon(Weapon):
    def __init__(self, item_name, attack_power_additional, defense_additional, char_type, limited_use = False):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Limited_Weapon(Weapon):
    def __init__(self, item_name, attack_power_additional, defense_additional, char_type, limited_use = True, uses_remaining = 0):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)
        self.uses_remaining = uses_remaining

class Jedi_Lightsaber(Unlimited_Weapon):
    def __init__(self, item_name = "Jedi Lightsaber", attack_power_additional = 1, defense_additional = 2, char_type = "Jedi", limited_use = False):
        super().__init__(self, item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Sith_Lightsaber(Unlimited_Weapon):
    def __init__(self, item_name = "Sith Lightsaber", attack_power_additional = 3, defense_additional = 0, char_type = "Sith", limited_use = False):
        super().__init__(self, item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Ninja_Stars(Limited_Weapon):
    def __init__(self, item_name = "Ninja Stars", attack_power_additional = 5, defense_additional = 0, char_type = "Neutral", limited_use = True, uses_remaining = 3):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, uses_remaining, limited_use)

class Gun(Weapon):
    def __init__(self, item_name = "Gun", attack_power_additional = 4, defense_additional = 1, char_type = "Neutral", limited_use = True, uses_remaining = 5):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, uses_remaining, limited_use)

class Shield(Weapon):
    def __init__(self, item_name = "Shield", attack_power_additional = 0, defense_additional = 5, char_type = "Neutral", limited_use = True, uses_remaining = 5):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, uses_remaining, limited_use)

# GAME CLASS

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.active_player = player1
        self.target_player = player2
        self.winner = None
        self.is_playing = False
        self.turn_count = 1

    def choose_starting_player(self):
        starting_turn_num = random.randint(1,10)
        start_determination = starting_turn_num % 2

        if start_determination == 0:
            self.active_player = self.player1
            self.target_player = self.player2
        else:
            self.active_player = self.player2
            self.target_player = self.player1
    
    def start_game(self, player1, player2):
        print(f"\nA Star Wars battle game has begun! This will be a contest pitting {player1.name} against {player2.name}!")
        player1_char_type = "Jedi" if self.player1.char_type == "Jedi" else "Sith"
        player2_char_type = "Jedi" if self.player2.char_type == "Jedi" else "Sith"
        print(f"\n{self.player1.name.capitalize()} is a {player1_char_type},\nwhile {self.player2.name} is a {player2_char_type}!")
        self.choose_starting_player()
        print(f"The active player in the first round has been selected as {self.active_player.name}! This means {self.target_player.name} will be the first to defend!")
        print("\nLet the game begin!\n")
        print("-" * 40 + "\n")

    def switch_turns(self):
        self.active_player, self.target_player = self.target_player, self.active_player
        self.turn_count += 1

    def show_stats(self):
        print(f"Player on current turn: {self.active_player.name}")
        print(f"Player awaiting turn: {self.target_player.name}")
        print("Player Stats:")
        print("-" * 40)
        print("Player 1:")
        self.player1.stats()
        print("-" * 40)
        print("Player 2:")
        self.player2.stats()
        if self.turn_count > 1:
            print("\n*NEXT TURN*\n" + "-" * 40 + "\n")
        else:
            print("\n*STARTING TURN*\n" + "-" * 40 + "\n")

    def equip_new_unl_weapon(self, player, new_unl_weapon):
        player.weapon_equipped = new_unl_weapon
        # Check if the new unlimited-use weapon is of a different character type
        if new_unl_weapon.char_type != player.char_type:
            player.strength += Weapon.attack_power_additional  # Neutral type weapon
            player.defense += Weapon.defense_additional  # Neutral type weapon
            print(f"{player.name}'s character type does not match that of {new_unl_weapon.item_name}. The newly-equipped weapon will increase {player.name}'s stats by that of the base-level weapon.")
        else:
            player.strength += new_unl_weapon.attack_power_additional
            player.defense += new_unl_weapon.defense_additional
            print(f"\n{player.name} equipped {new_unl_weapon.item_name}. {player.name}'s new total strength is {player.strength} and new total defense is {player.defense}.")
    
    def replace_unl_weapon(self, player, old_unl_weapon, new_unl_weapon):
        print(f"\n{player.name} already has an unlimited-use weapon equipped. Replacing {old_unl_weapon.item_name} with {new_unl_weapon.item_name}.")
        player.strength -= player.weapon_equipped.attack_power_additional
        player.defense -= player.weapon_equipped.defense_additional
        self.equip_new_unl_weapon
        print(f"\n{player.name} equipped {new_unl_weapon}. {player.name}'s new total strength is {player.strength} and new total defense is {player.defense}.")

    def equip_new_ltd_weapon(self, player, new_ltd_weapon):
        player.limited_weapon_equipped = new_ltd_weapon
        return self

    def replace_ltd_weapon(self, player, old_ltd_weapon, new_ltd_weapon):
        print(f"\n{player.name} already has a limited-use weapon equipped. Replacing {old_ltd_weapon.item_name} with {new_ltd_weapon.item_name}.")
        player.limited_weapon_equipped = new_ltd_weapon

    def equip_choice_weapon(self, player, new_weapon):
        equip_choice = input("\nDo you want to equip this weapon? (yes/no)\n>>>")
        if equip_choice == "yes":
            if new_weapon.limited_use == False and player.weapon_equipped:
                self.replace_unl_weapon(player, self.active_player.weapon_equipped, new_weapon)
            elif new_weapon.limited_use and player.limited_weapon_equipped:
                self.replace_ltd_weapon(player, player.limited_weapon_equipped, new_weapon)
            elif new_weapon.limited_use == False and player.weapon_equipped == False:
                self.equip_new_unl_weapon(player, new_weapon)
            else:
                self.equip_new_ltd_weapon(player, new_weapon)
        else:
            print(f"\n{player.name} chose not to equip the weapon.")
        return self

    def choice_unl_weapon(self, player):
        print(f"\n***Bonus***\n{player.name} gained an unlimited-use weapon!\n")
        die_result = roll_die_five()
        if die_result <= 3:
            weapon_selected = Unlimited_Weapon()
        elif die_result == 4:
            weapon_selected = Jedi_Lightsaber()
        elif die_result == 5:
            weapon_selected = Sith_Lightsaber()
        self.equip_choice_weapon(player, weapon_selected)
        return self

    def choice_ltd_weapon(self, player):
        print(f"\n***Bonus***\n{player.name} gained a limited-use weapon!\n")
        ltd_weapon_result = roll_die_three()
        if ltd_weapon_result == 1:
            weapon_selected = Ninja_Stars()
        elif ltd_weapon_result == 2:
            weapon_selected = Gun()
        else:
            weapon_selected = Shield()
        print(f"\n{player.name} received {weapon_selected.item_name}!")
        equip_choice = input("Do you want to equip this weapon? (yes/no)\n>>>")
        self.equip_choice_weapon(player, weapon_selected)
        return self

    def chance_any_weapon(self, player):
        weapon_chance = roll_die_six()
        weapon_choice = roll_die_six()
        if weapon_chance <= 3:
            print(f"\n***NO BONUS***\n{player.name} did not gain a weapon this round.")
            return self
        print(f"\n***BONUS***\n{player.name} gained a weapon!")
        if weapon_choice != 6:
            self.choice_unl_weapon(player)
        else:
            self.choice_ltd_weapon(player)
    
    def end_game_declaration(self):
        player1_health = self.player1.health
        player2_health = self.player2.health
        msg_game_over = "\n" + "-" * 40 + "\nGame Over\n" + "-" * 40
        if player1_health == player2_health:
            print("\n" + "-" * 40 + "\nIt's a draw!\n" + "-" * 40)
            print(msg_game_over)
            return self
        if player1_health > player2_health:
            self.winner = self.player1
            self.defeated = self.player2
        else:
            self.winner = self.player2
            self.defeated = self.player1
        print(f"\n{self.winner.name} has {self.winner.health} health remaining, while {self.defeated.name} has {self.defeated.health} remaining.")
        print("\n" + "-" * 40 + f"\n{self.winner.name} wins!\n" + "-" * 40)
        print(msg_game_over)
        self.is_playing == False
        return self

    def end_game_check(self):
        if self.is_playing and self.player1.is_alive and self.player2.is_alive and self.turn_count < 21:
            return False
        else:
            return True
    
    def battle(self):
        self.is_playing = True
        self.start_game(self.player1, self.player2)

        
         
            print(f"\n" + "-" * 40 + f"\nTurn {self.turn_count}\n")
            self.show_stats()
            #input_action_player1 = input(f"\n{self.active_player.name}, choose to attack, heal, or do an armed attack.\n>>>").strip().lower()
            input_action_player1 = input(f"\n{self.active_player.name}, choose to attack or heal.\n>>>")  # Before adding limited-use weapons, either attack or heal
            # input_action_player2 = input(f"\n{self.target_player.name}, choose to counter, defend, or do an armed defend.\n>>>").strip().lower()
            if input_action_player1 == "heal":
                continue
            else:
                input_action_player2 = input(f"\n{self.target_player.name}, choose to counter or defend.\n>>>").strip().lower() # Remove armed defend option until limited-use weapons are implemented
            print("\n" + "-" * 40 + "\nACTION PHASE\n" + "-" * 40 + "\n")

            # Player 1 chose to heal
            if input_action_player1 == "heal":
                if active_player.health < 30:
                    heal_amount = roll_die_three()
                    active_player.change_health(heal_amount)
                    print(f"\n{active_player.name} heals for {heal_amount} health. New health: {active_player.health}.")
                else:
                    print(f"\n{active_player.name} is already at full health and cannot heal.")
            else:
                pass

            # Player 1 chose attack
            if input_action_player1 == "attack" or input_action_player1 != "armed attack":
                
                # Player 2 chose defend
                if input_action_player2 == "defend" or input_action_player2 != "counter":
                    attack_damage = active_player.attack(target_player) - target_player.defend()
                    if attack_damage < 0:
                        active_player.change_health(attack_damage)
                        print(f"\n{active_player.name} received {abs(attack_damage)} damage due to high defense of {target_player.name}.")
                    elif attack_damage == 0:
                        print(f"\n{target_player.name} defended sufficiently to take no damage.")
                    else:
                        target_player.change_health(-attack_damage)
                
                # Player 2 chose counter
                else:
                    print(f"\n{target_player.name} attempts to counter the attack!")
                    attack_damage = active_player.attack(target_player)
                    counter_damage_determination = roll_die_six()
                    if counter_damage_determination <= 3:
                        print(f"\n{target_player.name}'s counter attack was ineffective!")
                    elif counter_damage_determination == 4:
                        print(f"\n{target_player.name} counter attacks {active_player.name} for 1 damage!")
                        active_player.change_health(-1)
                    elif counter_damage_determination == 5:
                        print(f"\n{target_player.name} counter attacks {active_player.name} for 2 damage!")
                        active_player.change_health(-2)
                    else:
                        print(f"\n{target_player.name} counter attacks {active_player.name} for 3 damage!")
                        active_player.change_health(-3)
                
                    

# End of refactoring 'battle' function. Delete this comment when refactoring of 'battle' function is complete.
            



# BODY (PLAY GAME)
# Create characters
player1 = Char_Type_Jedi("Chris")
player2 = Char_Type_Sith("Mark")

# Commence game
game = Game(player1, player2)
game.start_game()
# Insert body code of game here
while game.is_playing and game.player1.is_alive and game.player2.is_alive and game.turn_count < 21:
    active_player = game.active_player
    target_player = game.target_player
    attack_damage = 0

    # Insert player 1 and player 2 choices here
    # [insert here a function which requests each player's chosen action]

    print("\n" + "-" * 40 + "\nACTION PHASE COMPLETE\n" + "-" * 40 + "\n")
    # End of game conditions checked. If one or more condition is met, the game ends immediately. If not, the game continues to the Weapons Gain phase.
    is_game_ended = game.end_game_check()
    if is_game_ended == True:
        game.end_game_declaration()
        break
    
    # Weapons Gain phase
    game.chance_any_weapon(active_player)
    
    # Progress to next turn
    game.switch_turns()

    # While loop continues from the top, beginning the next turn.

# Testing ground
