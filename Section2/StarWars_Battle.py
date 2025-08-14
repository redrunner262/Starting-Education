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
    
    def change_health(self, amount, activity = "battle"):
        if amount == 0: # Do nothing if no change occurred to health
            print("No damage was dealt this attack!")
            return self
        # Change the affected character's health value
        health_direction = 'decreased' if amount < 0 else 'increased'
        new_health_value = self.health + amount
        print(f"{self.name}'s health {health_direction} by {abs(amount)}.")
        if new_health_value > 0:
            if new_health_value <= 30:
                self.health = new_health_value
            elif new_health_value > 30:
                self.health = 30
            print(f"{self.name}'s health is now {0 if self.health <= 0 else self.health}.") if activity != "heal" else None
        else:
            self.health = 0
        # Set character to "defeated"
        if self.health == 0:
            self.is_alive = False
            print(f"\n{self.name} has been defeated!")
            return self
        # Print "heal" statements and stats
        elif activity == "heal" and new_health_value < 30:
            print(f"\n{self.name} heals for {amount} health.")
        elif activity == "heal" and new_health_value >= 30:
            print(f"\n{self.health} heals to full health.")

    def defend(self):
        def_boost = random.randint(1, 4)
        defense_value = self.defense + def_boost
        print(f"\n{self.name} defends and increases defense by {def_boost}. This round's defense: {defense_value}.")
        return defense_value

    def attack(self):
        atk_boost = random.randint(1, 3)
        attack_strength = self.strength + atk_boost
        if attack_strength <= 0:
            print(f"\n{self.name}'s attack is ineffective.")
            attack_strength = 0
            return attack_strength
        else:
            print(f"\n{self.name} gets an attack boost of {atk_boost} and attacks with {attack_strength} strength!")
        return attack_strength
    
    def counter(self):
        counter_damage_determination = roll_die_six()
        if counter_damage_determination <= 3:
            print("Counterattack was unsuccessful...\n")
            return 0
        elif counter_damage_determination <= 5:
            counter_damage_value = 4
        else:
            counter_damage_value = 6
        print(f"\n{self.name} counterattacks for {counter_damage_value} damage!\n")
        return counter_damage_value
        # After this function, call the "change_health" function on the countered player, using this function's returned value.

    def char_heal(self):
        if self.health >= 30:
            print(f"\n{self.name} is already at full health and cannot heal further.")
            self.health = 30
            return self
        heal_amount = roll_die_three()
        self.change_health(heal_amount, "heal")
        return self
    
    # How can I store an f-string with the 'depleted' message in both armed_attack and armed_defend functions?
    # It is the same message so I may as well factor it out, but using 'self.[attribute] in an f-string in a variable results in a warning underline.
    # msg_ltd_weapon_depleted = f"{self.name} depleted his limited-use weapon's uses. {self.limited_weapon_equipped.item_name.capitalize()} will be unequipped after this action."

    def armed_attack(self):
        if self.limited_weapon_equipped:
            armed_attack_power = self.strength + self.limited_weapon_equipped.attack_power_additional
            print(f"{self.name} attacks with {self.weapon_equipped.item_name}, giving a total strength of {armed_attack_power}!")
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

class Jedi(Character):
    def __init__(self, name, health = 30, strength = 5, defense = 5, char_type = "Jedi", weapon_equipped = None, limited_weapon_equipped = None):
        super().__init__(name, health, weapon_equipped, limited_weapon_equipped)
        self.strength = strength
        self.defense = defense
        self.char_type = char_type

class Sith(Character):
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
    def __init__(self, item_name = "Basic Knife", attack_power_additional = 1, defense_additional = 1, char_type = "Neutral", limited_use = False):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Limited_Weapon(Weapon):
    def __init__(self, item_name, attack_power_additional, defense_additional, char_type, limited_use = True, uses_remaining = 0):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)
        self.uses_remaining = uses_remaining

class Jedi_Lightsaber(Unlimited_Weapon):
    def __init__(self, item_name = "Jedi Lightsaber", attack_power_additional = 1, defense_additional = 2, char_type = "Jedi", limited_use = False):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Sith_Lightsaber(Unlimited_Weapon):
    def __init__(self, item_name = "Sith Lightsaber", attack_power_additional = 3, defense_additional = 0, char_type = "Sith", limited_use = False):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)

class Ninja_Stars(Limited_Weapon):
    def __init__(self, item_name = "Ninja Stars", attack_power_additional = 5, defense_additional = 0, char_type = "Neutral", limited_use = True, uses_remaining = 3):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)
        self.uses_remaining = uses_remaining

class Gun(Weapon):
    def __init__(self, item_name = "Gun", attack_power_additional = 4, defense_additional = 1, char_type = "Neutral", limited_use = True, uses_remaining = 5):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)
        self.uses_remaining = uses_remaining

class Shield(Weapon):
    def __init__(self, item_name = "Shield", attack_power_additional = 0, defense_additional = 5, char_type = "Neutral", limited_use = True, uses_remaining = 5):
        super().__init__(item_name, attack_power_additional, defense_additional, char_type, limited_use)
        self.uses_remaining = uses_remaining

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
    
    # Gameplay timing functions
    def choose_starting_player(self):
        starting_turn_num = random.randint(1,10)
        start_determination = starting_turn_num % 2

        if start_determination == 0:
            self.active_player = self.player1
            self.target_player = self.player2
        else:
            self.active_player = self.player2
            self.target_player = self.player1
    
    def switch_turns(self):
        self.active_player, self.target_player = self.target_player, self.active_player
        self.turn_count += 1
        print(f"\n*Beginning of turn {str(self.turn_count)}*\n" + "-" * 40 + "\n")

    def start_game(self):
        self.is_playing = True
        print(f"\nA Star Wars battle game has begun! This will be a contest pitting {self.player1.name} against {self.player2.name}!")
        player1_char_type = "Jedi" if self.player1.char_type == "Jedi" else "Sith"
        player2_char_type = "Jedi" if self.player2.char_type == "Jedi" else "Sith"
        print(f"\n{self.player1.name.capitalize()} is a {player1_char_type},\nwhile {self.player2.name.capitalize()} is a {player2_char_type}!")
        self.choose_starting_player()
        print(f"The active player in the first round has been selected as {self.active_player.name}!")
        print("\nLet the game begin!\n")
        print("-" * 40 + "\n")

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
        print("-" * 40 + "\n")
    
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

    # Player Action functions

    def input_action_active_player(self):
        print(f"\n{self.active_player.name.capitalize()}, select an action from these options.")
        armed_actions_txt = ", Armed Attack" if self.active_player.limited_weapon_equipped else ""
        player_action = input(f"Attack, Heal{armed_actions_txt}\n>>>").strip().lower()
        return player_action
    
    def input_action_target_player(self):
        print(f"\n{self.target_player.name.capitalize()}, select an action from these options.")
        armed_actions_txt = ", Armed Defend" if self.target_player.limited_weapon_equipped else ""
        player_action = input(f"Defend, Counter{armed_actions_txt}\n>>>").strip().lower()
        return player_action

    # Weapons Gain Phase functions

    def equip_new_unl_weapon(self, new_unl_weapon):
        self.active_player.weapon_equipped = new_unl_weapon
        # Check if the new unlimited-use weapon is of a different character type
        if new_unl_weapon.char_type != self.active_player.char_type:
            self.active_player.strength += Weapon().attack_power_additional  # Neutral type weapon
            self.active_player.defense += Weapon().defense_additional  # Neutral type weapon
            print(f"{self.active_player.name}'s character type does not match that of {new_unl_weapon.item_name}. The newly-equipped weapon will increase {self.active_player.name}'s stats by that of the base-level weapon.")
        else:
            self.active_player.strength += new_unl_weapon.attack_power_additional
            self.active_player.defense += new_unl_weapon.defense_additional
            print(f"\n{self.active_player.name} equipped {new_unl_weapon.item_name}. {self.active_player.name}'s new total strength is {self.active_player.strength} and new total defense is {self.active_player.defense}.")
    
    def replace_unl_weapon(self, old_unl_weapon, new_unl_weapon):
        print(f"\n{self.active_player.name} already has an unlimited-use weapon equipped. Replacing {old_unl_weapon.item_name} with {new_unl_weapon.item_name}.")
        self.active_player.strength -= self.active_player.weapon_equipped.attack_power_additional
        self.active_player.defense -= self.active_player.weapon_equipped.defense_additional
        self.equip_new_unl_weapon
        print(f"\n{self.active_player.name} equipped {new_unl_weapon}. {self.active_player.name}'s new total strength is {self.active_player.strength} and new total defense is {self.active_player.defense}.")

    def equip_new_ltd_weapon(self, new_ltd_weapon):
        self.active_player.limited_weapon_equipped = new_ltd_weapon
        return self

    def replace_ltd_weapon(self, old_ltd_weapon, new_ltd_weapon):
        print(f"\n{self.active_player.name} already has a limited-use weapon equipped. Replacing {old_ltd_weapon.item_name} with {new_ltd_weapon.item_name}.")
        self.active_player.limited_weapon_equipped = new_ltd_weapon

    def equip_choice_weapon(self, new_weapon):
        equip_choice = input("\nDo you want to equip this weapon? (yes/no)\n>>>")
        if equip_choice == "yes":
            if new_weapon.limited_use == None and self.active_player.weapon_equipped == None:
                self.replace_unl_weapon(self.active_player.weapon_equipped, new_weapon)
            elif new_weapon.limited_use == None and self.active_player.limited_weapon_equipped == None:
                self.replace_ltd_weapon(self.active_player.limited_weapon_equipped, new_weapon)
            elif new_weapon.limited_use == None and self.active_player.weapon_equipped == None:
                self.equip_new_unl_weapon(new_weapon)
            else:
                self.equip_new_ltd_weapon(new_weapon)
        else:
            print(f"\n{self.active_player.name.capitalize()} chose not to equip the weapon.")
        return self

    def choice_unl_weapon(self):
        print(f"\n{self.active_player.name.capitalize()} gained an unlimited-use weapon!\n")
        die_result = roll_die_five()
        if die_result <= 3:
            weapon_selected = Unlimited_Weapon()
        elif die_result == 4:
            weapon_selected = Jedi_Lightsaber()
        elif die_result == 5:
            weapon_selected = Sith_Lightsaber()
        msg_unl_weapon_stats = f"{self.active_player.name.capitalize()} gained a {weapon_selected.item_name}!\nAttack value: {weapon_selected.attack_power_additional} | Defense value: {weapon_selected.defense_additional}\n"
        print(msg_unl_weapon_stats)
        self.equip_choice_weapon(weapon_selected)
        return self

    def choice_ltd_weapon(self):
        print(f"\n{self.active_player.name} gained a limited-use weapon!\n")
        ltd_weapon_result = roll_die_three()
        if ltd_weapon_result == 1:
            weapon_selected = Ninja_Stars()
        elif ltd_weapon_result == 2:
            weapon_selected = Gun()
        else:
            weapon_selected = Shield()
        msg_ltd_weapon_stats = f"{self.active_player.name.capitalize()} gained a {weapon_selected.item_name}!\nAttack value: {weapon_selected.attack_power_additional} | Defense value: {weapon_selected.defense_additional} | Uses: {weapon_selected.uses_remaining}\n"
        print(msg_ltd_weapon_stats)
        self.equip_choice_weapon(weapon_selected)
        return self

    def chance_any_weapon(self):
        weapon_chance = roll_die_six()
        weapon_choice = roll_die_six()
        if weapon_chance <= 3:
            print(f"\n***NO BONUS***\n{self.active_player.name} did not gain a weapon this round.\n")
            return self
        print(f"\n***BONUS***\n{self.active_player.name} gained a weapon!")
        if weapon_choice != 6:
            self.choice_unl_weapon()
        else:
            self.choice_ltd_weapon()
                
            


# BODY (PLAY GAME)
# Create characters
jedi_placeholder = Jedi("A")
sith_placeholder = Sith("B")
msg_name_request_start = "Player "
msg_name_request_end = ", enter your first name.\n>>>"
p1_name = input(msg_name_request_start + "1" + msg_name_request_end)
p2_name = input(msg_name_request_start + "2" + msg_name_request_end)

msg_choose_char_type = f", choose your character type: {Jedi("A").char_type} or {Sith("B").char_type}.\n{Jedi("A").char_type} starts with {Jedi("A").strength} attack power and {Jedi("A").defense} defense power.\n{Sith("B").char_type} starts with {Sith("B").strength} attack power and {Sith("B").defense} defense power.\n>>>"
p1_char_type = input("\n" + p1_name + msg_choose_char_type).lower()
p2_char_type = input("\n" + p2_name + msg_choose_char_type).lower()

if p1_char_type == "sith":
    p1 = Sith(p1_name)
else: p1 = Jedi(p1_name)

if p2_char_type == "sith":
    p2 = Sith(p2_name)
else:
    p2 = Jedi(p2_name)

# Commence game
game = Game(p1, p2)

# Comment out beginning here for testing
game.start_game()

# Gameplay code
while game.is_playing:
    active_player = game.active_player
    target_player = game.target_player
    attack_value = 0
    defend_value = 0
    heal_value = 0
    
    # Action Phase
    # Receive each player's action choices
    p1_action = game.input_action_active_player()
    

    # Respond to action choices
    # Player 1 action
    if p1_action == "heal":
        game.active_player.char_heal()
        print(f"{active_player.name.capitalize()} chooses to heal!")
    else:
        print(f"{active_player.name.capitalize()} chooses to attack!")

        # Player 2 action taken if Player 1 does not choose to heal
        p2_action = game.input_action_target_player()
        if p2_action != "counter" and p2_action != "armed defend":
            print(f"{target_player.name.capitalize()} chooses to defend!")
            defend_value = game.target_player.defend()
        elif p2_action == "armed defend":
            print(f"{target_player.name.capitalize()} performs an armed defend!")
            defend_value = game.target_player.armed_defend()
        
        if p1_action == "armed attack":
            attack_value = game.active_player.armed_attack()
        else:
            attack_value = game.active_player.attack()

        # Resolve battle damage, if any
        resulting_damage = attack_value - defend_value
        if resulting_damage:
            if resulting_damage < 0:
                game.active_player.change_health(resulting_damage)
            elif resulting_damage > 0:
                game.target_player.change_health(-resulting_damage)
            else:
                print("No damage was dealt for this attack!")
        
        # Resolve counter damage, if any
        if p2_action == "counter":
            print(f"{target_player.name.capitalize()} chooses to attempt a counterattack!")
            counter_value = game.target_player.counter()
            if counter_value > 0:
                game.active_player.change_health(-counter_value)

    print("\n" + "-" * 40 + "\nACTION PHASE COMPLETE\n" + "-" * 40 + "\n")

    # End-of-game conditions checked. If one or more condition is met, the game ends immediately. If not, the game continues to the Weapons Gain Phase.
    is_game_ended = game.end_game_check()
    if is_game_ended == True:
        game.end_game_declaration()
        break
    
    # Weapons Gain Phase
    game.chance_any_weapon()
    
    # End Phase (Progress to next turn)
    game.show_stats()
    game.switch_turns()

    # While loop continues from the top, beginning the next turn.

# Testing ground
