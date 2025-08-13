# IMPORTS
import random

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
class Character:
    def __init__(self, name, weapon_equipped=None, limited_weapon_equipped=None):
        self.name = name
        self.health = 30
        self.strength = 0
        self.defense = 0
        self.is_alive = True
        self.weapon_equipped = weapon_equipped
        self.limited_weapon_equipped = limited_weapon_equipped

    def __repr__(self):
        return f"{self.name} | Health: {self.health} | Strength: {self.strength} | Defense: {self.defense} | Alive: {self.is_alive}"
    
    def change_health(self, amount):
        if amount < 0:
            print(f"{self.name}'s health decreased by {abs(amount)}.")
            self.health += amount
            print(f"{self.name}'s health is now {self.health}.")
            if self.health <= 0:
                self.is_alive = False
                print(f"{self.name} has been defeated!")
                return self
            else:
                return self
        elif amount > 0:
            print(f"{self.name}'s health increased by {abs(amount)}.")
            self.health += amount
            print(f"{self.name}'s health is now {self.health}.")
            return self
        else:
            print(f"{self.name}'s health remains unchanged.")
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
    
    
    def stats(self):
        attributes = self.__dict__
        for key in attributes:
            val = attributes[key]
            print(f"{key.capitalize()}: {val}")

class Weapon:
    def __init__(self, item_name="Basic Knife", attack_power_additional=1, defense_additional=1, char_type="Neutral", uses_remaining=None, limited_use=False):
        self.item_name = item_name
        self.attack_power_additional = attack_power_additional # Additional attack power provided by the weapon
        self.defense_additional = defense_additional # Additional defense provided by the weapon
        self.char_type = char_type # Character type that benefits most from use of the weapon (e.g., Jedi, Sith, Neutral)
        self.uses_remaining = uses_remaining  # Default to None for weapons without limited uses
        self.limited_use = limited_use  # Indicates whether the weapon has limited uses

class Weapon_Type_Jedi(Weapon):
    def __init__(self):
        self.item_name = "Jedi Lightsaber"
        self.attack_power_additional = 1
        self.defense_additional = 2
        self.char_type = "Jedi"

class Weapon_Type_Sith(Weapon):
    def __init__(self):
        self.item_name = "Sith Lightsaber"
        self.attack_power_additional = 3
        self.defense_additional = 0
        self.char_type = "Sith"

class Weapon_Type_Ninja_Stars(Weapon):
    def __init__(self):
        self.item_name = "Ninja Stars"
        self.attack_power_additional = 5
        self.defense_additional = 0
        self.char_type = "Neutral"  # Neutral type for Ninja Stars, can be used by any character type
        self.uses_remaining = 3  # Limited uses for Ninja Stars
        self.limited_use = True  # Indicates that this weapon has limited uses

class Weapon_Type_Gun(Weapon):
    def __init__(self):
        self.item_name = "Gun"
        self.attack_power_additional = 4
        self.defense_additional = 0
        self.char_type = "Neutral"  # Neutral type for Gun, can be used by any character type
        self.uses_remaining = 5  # Limited uses for Gun
        self.limited_use = True  # Indicates that this weapon has limited uses

class Weapon_Type_Shield(Weapon):
    def __init__(self):
        self.item_name = "Shield"
        self.attack_power_additional = 0
        self.defense_additional = 3
        self.char_type = "Neutral"  # Neutral type for Shield, can be used by any character type
        self.uses_remaining = 7  # Limited uses for Shield
        self.limited_use = True  # Indicates that this weapon has limited uses

class Char_Type_Jedi(Character):
    def __init__(self, name, weapon_equipped=None, limited_weapon_equipped=None):
        super().__init__(name, weapon_equipped, limited_weapon_equipped)
        self.health = 20
        self.strength = 5
        self.defense = 5
        self.char_type = "Jedi"

    def armed_attack(self, target):
        if self.weapon_equipped and self.weapon_equipped.limited_use and self.weapon_equipped.uses_remaining > 0:
            armed_attack_power = (self.strength + self.weapon.attack_power_additional)
            if armed_attack_power < 0:
                armed_attack_power = 0
            self.weapon_equipped.uses_remaining -= 1
            if self.weapon_equipped.uses_remaining == 0:
                print(f"{self.weapon_equipped.item_name} has no uses remaining and is now unequipped.")
                self.weapon_equipped = None
            print(f"{self.name} attacks {target.name} with {self.weapon.item_name}, giving a total strength of {armed_attack_power}!")
            return armed_attack_power
        else:
            print(f"{self.name} cannot perform an armed attack because no weapon is equipped.")
            armed_attack_power = 0
            return armed_attack_power
    
    def armed_defend(self):
        if self.weapon_equipped and self.weapon_equipped.char_type == "Jedi":
            self.defense += self.weapon.defense_additional
            print(f"{self.name} defends with {self.weapon.item_name} and increases defense by {self.weapon.defense_additional}. New defense: {self.defense}.")
        elif not self.weapon_equipped:
            print(f"{self.name} cannot perform an armed defend because no weapon is equipped.")
        else:
            print(f"{self.name} is untrained in using {self.weapon.item_name} because it is a Sith weapon. The weapon is treated as Neutral type.")
            self.weapon_equipped.char_type = "Neutral"

class Char_Type_Sith(Character):
    def __init__(self, name, weapon_equipped=None, limited_weapon_equipped=None):
        super().__init__(name, weapon_equipped, limited_weapon_equipped)
        self.health = 20
        self.strength = 7
        self.defense = 3
        self.char_type = "Sith"
        self.weapon_equipped = weapon_equipped
        self.limited_weapon_equipped = None

    def armed_attack(self, target):
        if self.weapon_equipped:
            armed_attack_power = (self.strength + self.weapon.attack_power_additional)
            if armed_attack_power < 0:
                armed_attack_power = 0
            print(f"{self.name} attacks {target.name} with {self.weapon.item_name}, giving a total strength of {armed_attack_power}!")
            return armed_attack_power
        else:
            print(f"{self.name} cannot perform an armed attack because no weapon is equipped.")
            armed_attack_power = 0
            return armed_attack_power

    def armed_defend(self):
        if self.weapon_equipped and self.weapon_equipped.char_type == "Sith":
            self.defense += self.weapon.defense_additional
            print(f"{self.name} defends with {self.weapon.item_name} and increases defense by {self.weapon.defense_additional}. New defense: {self.defense}.")
        elif not self.weapon_equipped:
            print(f"{self.name} cannot perform an armed defend because no weapon is equipped.")
        else:
            print(f"{self.name} is untrained in using {self.weapon.item_name} because it is a Jedi weapon. The weapon is treated as Neutral type.")
            self.weapon_equipped.char_type = "Neutral"

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_turn = player1
        self.awaiting_turn = player2
        self.winner = None
        self.is_playing = False
        self.turn_count = 1

    def choose_starting_player(self):
        starting_turn_num = random.randint(1,10)
        start_determination = starting_turn_num % 2

        if start_determination == 0:
            self.current_turn = self.player1
            self.awaiting_turn = self.player2
        else:
            self.current_turn = self.player2
            self.awaiting_turn = self.player1

    def switch_turns(self):
        self.current_turn, self.awaiting_turn = self.awaiting_turn, self.current_turn
        self.turn_count += 1
    
    def show_stats(self):
        print(f"Player on current turn: {self.current_turn.name}")
        print(f"Player awaiting turn: {self.awaiting_turn.name}")
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

    def replace_unl_weapon(self, player, old_unl_weapon, new_unl_weapon):
        print(f"\n{player.name} already has an unlimited-use weapon equipped. Replacing {old_unl_weapon.item_name} with {new_unl_weapon.item_name}.")
        player.strength -= player.weapon_equipped.attack_power_additional
        player.defense -= player.weapon_equipped.defense_additional
        player.weapon_equipped = new_unl_weapon
        # Check if the new unlimited weapon is of a different character type
        if new_unl_weapon.char_type != player.char_type:
            player.strength += Weapon().attack_power_additional  # Neutral type weapon
            player.defense += Weapon().defense_additional  # Neutral type weapon
        else:
            player.strength += new_unl_weapon.attack_power_additional
            player.defense += new_unl_weapon.defense_additional
        print(f"\n{player.name} equipped {new_unl_weapon}. {player.name}'s new total strength is {player.strength} and new total defense is {player.defense}.")

    def replace_ltd_weapon(self, player, old_ltd_weapon, new_ltd_weapon):
        print(f"\n{player.name} already has a limited-use weapon equipped. Replacing {old_ltd_weapon.item_name} with {new_ltd_weapon.item_name}.")
        player.strength -= player.limited_weapon_equipped.attack_power_additional
        player.defense -= player.limited_weapon_equipped.defense_additional
        player.limited_weapon_equipped = new_ltd_weapon
        player.strength += new_ltd_weapon.attack_power_additional
        player.defense += new_ltd_weapon.defense_additional

    def equip_choice_unl_weapon(self, player, new_weapon):
        print(f"Weapon gained is {new_weapon.item_name}.")
        equip_choice = input(f"\n{player.name} received {new_weapon.item_name}. Do you want to equip this weapon? (yes/no)\n>>>")
        if equip_choice == "yes":
            if player.weapon_equipped:
                self.replace_unl_weapon(self.active_player, self.active_player.weapon_equipped, new_weapon.item_name)
            else:
                
        else:
            print(f"\n{player.name} chose not to equip the weapon.")
        return self

    def gain_unl_weapon(self, player, die_result):
        msg_equip_from_naught = f"\n{player.name} equipped {weapon_selected.item_name}. {player.name}'s new total strength is {player.strength} and new total defense is {player.defense}."
        msg_decline_equip = f"\n{player.name} chose not to equip the weapon."
        if die_result <= 4:
            self.equip_choice_unl_weapon(player, Weapon())
        elif die_result == 5:
            weapon_selected = Weapon_Type_Jedi()
            equip_choice = input(f"\n{player.name} received {weapon_selected.item_name}. Do you want to equip this weapon? (yes/no)\n>>>")
            if equip_choice == "yes":
                if player.weapon_equipped:
                    self.replace_unl_weapon(self.active_player, self.active_player.weapon_equipped, weapon_selected)
                else:
                    player.weapon_equipped = Weapon_Type_Jedi()
                    player.strength += player.weapon_equipped.attack_power_additional
                    player.defense += player.weapon_equipped.defense_additional
                    print(msg_equip_from_naught)
            else:
                print(msg_decline_equip)
        else:
            weapon_selected = Weapon_Type_Sith()
            equip_choice = input(f"\n{player.name} received {weapon_selected.item_name}. Do you want to equip this weapon? (yes/no)\n>>>")
            if equip_choice == "yes":
                if player.weapon_equipped:
                    self.replace_unl_weapon(self.active_player, self.active_player.weapon_equipped, weapon_selected)
                else:
                    player.weapon_equipped = Weapon_Type_Sith()
                    player.strength += player.weapon_equipped.attack_power_additional
                    player.defense += player.weapon_equipped.defense_additional
                    print(msg_equip_from_naught)
            else:
                print(msg_decline_equip)

    def choose_weapon_unlimited(self, unl_weapon_recipient):
        weapon_gain_chance = roll_die_six()
        if weapon_gain_chance > 4:
            print(f"\n***BONUS***\n{unl_weapon_recipient.name} gained an unlimited weapon!")
            weapon_gain_die_result = roll_die_six()
            self.gain_unl_weapon(unl_weapon_recipient, weapon_gain_die_result)
        else:
            print(f"\n***NO BONUS***\n{unl_weapon_recipient.name} did not gain a weapon this round.")

    def choose_weapon_limited(self, player):
        ltd_weapon_gain_chance = roll_die_six()
        if ltd_weapon_gain_chance < 5:
            print(f"\n***No Bonus***\n{player.name} did not gain a limited-use weapon this round.")
        else:
            print(f"\n***Bonus***\n{player.name} gained a limited-use weapon!")
            ltd_weapon_selection = roll_die_five()
            if ltd_weapon_selection <= 2:
                print(f"\n{player.name} received the weapon Ninja Stars!")
                equip_choice = input(f"\n{player.name} received Ninja Stars. Do you want to equip this weapon? (yes/no)\n>>>")
                if equip_choice != "yes":
                    print(f"\n{player.name} chose not to equip the weapon.")
                else:
                    if player.limited_weapon_equipped:
                        print(f"\n{player.name} already has a limited-use weapon equipped. Replacing it with Ninja Stars.")
                        player.strength -= player.limited_weapon_equipped.attack_power_additional
                    player.limited_weapon_equipped = Weapon_Type_Ninja_Stars()

    def battle(self):
        self.is_playing = True
        self.choose_starting_player()

        while self.is_playing and self.player1.is_alive and self.player2.is_alive and self.turn_count < 21:
            active_player = self.current_turn
            target_player = self.awaiting_turn
            attack_damage = 0
            print(f"\n" + "-" * 40 + f"\nTurn {self.turn_count}\n")
            self.show_stats()
            #input_action_player1 = input(f"\n{self.current_turn.name}, choose to attack, heal, or do an armed attack.\n>>>").strip().lower()
            input_action_player1 = input(f"\n{self.current_turn.name}, choose to attack or heal.\n>>>")  # Before adding limited-use weapons, either attack or heal
            # input_action_player2 = input(f"\n{self.awaiting_turn.name}, choose to counter, defend, or do an armed defend.\n>>>").strip().lower()
            if input_action_player1 == "heal":
                continue
            else:
                input_action_player2 = input(f"\n{self.awaiting_turn.name}, choose to counter or defend.\n>>>").strip().lower() # Remove armed defend option until limited-use weapons are implemented
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

            # Player 1 chose armed attack
            else:
                print(f"\n{active_player.name} performs an armed attack on {target_player.name}!")
                armed_attack_battle_power = active_player.armed_attack(target_player)
                
                # Player 2 chose defend
                if input_action_player2 == "defend" or input_action_player2 != "armed defend" and input_action_player2 != "counter":
                    print(f"\n{target_player.name} defends against the armed attack!")
                    print(f"")
                    armed_attack_battle_power -= target_player.defend()
                    if armed_attack_battle_power < 0:
                        active_player.change_health(armed_attack_battle_power)
                        print(f"\n{active_player.name} received {abs(armed_attack_battle_power)} damage due to high defense of {target_player.name}.")
                    else:
                        target_player.change_health(-armed_attack_battle_power)
                
                # Player 2 chose armed defend
                elif input_action_player2 == "armed defend":
                    print(f"\n{target_player.name} makes an armed defense against the attack!")
                    armed_defense_value = target_player.armed_defend()
                    if armed_defense_value <= 0:
                        print(f"\n{target_player.name} failed to defend against the armed attack!")
                        target_player.change_health(armed_attack_damage)
                    else:
                        target_player.change_health(-armed_attack_damage + armed_defense_value)
                
                # Player 2 chose counter
                else:
                    print(f"\n{target_player.name} attempts to counter the armed attack!")
                    armed_attack_damage = active_player.armed_attack(target_player)
                    counter_damage_determination = roll_die_six()
                    if counter_damage_determination <= 4:
                        print(f"\n{target_player.name}'s counter attack was ineffective!")
                    elif counter_damage_determination == 5:
                        print(f"\n{target_player.name} counter attacks {active_player.name} for 1 damage!")
                        active_player.change_health(-1)
                    else:
                        print(f"\n{target_player.name} counter attacks {active_player.name} for 2 damage!")
                        active_player.change_health(-2)

            # End of action phase message
            print("\n" + "-" * 40 + "\nACTION PHASE COMPLETE\n" + "-" * 40 + "\n")

            # Check for weapon gain for active player
            if input_action_player1 != "heal" and active_player.is_alive == False or target_player.is_alive == False:
                print(f"Weapon gain phase skipped because one of the players has been defeated.")
                break
            else:
                self.choose_weapon_unlimited(active_player)
        
            # Switch turns after round resolution
            self.switch_turns()
        
        # End of game determination and messages
        # Determined by defeated player
        if self.player1.is_alive == False or self.player2.is_alive == False:
            if self.player1.is_alive:
                self.winner = self.player1
            else:
                self.winner = self.player2
        # Determined by expired turn count
        else:
            if self.player1.health > self.player2.health:
                self.winner = self.player1
                print(f"\n{self.player1.name} has {self.player1.health} health remaining, while {self.player2.name} has {self.player2.health} remaining.")
            elif self.player2.health > self.player1.health:
                self.winner = self.player2
                print(f"\n{self.player1.name} has {self.player1.health} health remaining, while {self.player2.name} has {self.player2.health} remaining.")
            else:
                print("\n" + "-" * 40 + "\nIt's a draw!\n" + "-" * 40)
                return
        print("\n" + "-" * 40 + f"\n{self.winner.name} wins!\n" + "-" * 40)
        print("\n" + "-" * 40 + "\nGame Over\n" + "-" * 40)

# BODY
# Create characters
player1 = Char_Type_Jedi("Chris")
player2 = Char_Type_Sith("Mark")

# Commence game
game = Game(player1, player2)
game.battle()

# Testing ground
