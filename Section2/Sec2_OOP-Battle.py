# IMPORTS
import random

# CLASSES
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 30
        self.strength = 0
        self.defense = 0
        self.is_alive = True

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
    def __init__(self):
        self.item_name = "Basic Knife"
        self.attack_power_additional = 1
        self.defense_additional = 0
        self.char_type = "Neutral"

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

class Char_Type_Jedi(Character):
    def __init__(self, name, weapon_equipped=None):
        super().__init__(name)
        self.health = 20
        self.strength = 5
        self.defense = 5
        self.weapon_equipped = weapon_equipped
        self.weapon_name = weapon_equipped.item_name if weapon_equipped else "No weapon equipped"
        self.char_type = "Jedi"

    # def defend(self):
    #     self.defense = 5
    #     return super().defend()
    
    # def stats(self):
    #     super().stats()
    #     if self.weapon_equipped:
    #         print(f"Weapon Equipped: {self.weapon_equipped.item_name}")

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
        if self.weapon_equipped and self.weapon_equipped.char_type == "Jedi":
            self.defense += self.weapon.defense_additional
            print(f"{self.name} defends with {self.weapon.item_name} and increases defense by {self.weapon.defense_additional}. New defense: {self.defense}.")
        elif not self.weapon_equipped:
            print(f"{self.name} cannot perform an armed defend because no weapon is equipped.")
        else:
            print(f"{self.name} is untrained in using {self.weapon.item_name} because it is a Sith weapon. The weapon is treated as Neutral type.")
            self.weapon_equipped.char_type = "Neutral"

class Char_Type_Sith(Character):
    def __init__(self, name, weapon_equipped=None):
        super().__init__(name)
        self.health = 20
        self.strength = 7
        self.defense = 3
        self.weapon_equipped = weapon_equipped
        self.weapon_name = weapon_equipped.item_name if weapon_equipped else "No weapon equipped"
        self.char_type = "Sith"

    # def defend(self):
    #     self.defense = 3
    #     return super().defend()
    
    # def stats(self):
    #     super().stats()
    #     if self.weapon_equipped:
    #         print(f"Weapon Equipped: {self.weapon_equipped.item_name}")

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
                    heal_amount = random.randint(1, 3)
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
                    counter_damage_determination = random.randint(1, 6)
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
                    counter_damage_determination = random.randint(1, 6)
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
                weapon_gain_chance = random.randint(1, 6)
                if weapon_gain_chance > 4:
                    print(f"\n***BONUS***\n{active_player.name} gained a weapon!")
                    weapon_selection = random.randint(1, 6)
                    weapon_name = "Basic Knife"
                    if weapon_selection <= 4:
                        print(f"Weapon gained is {weapon_name}.")
                        equip_choice = input(f"\n{active_player.name} received {weapon_name}. Do you want to equip this weapon? (yes/no)\n>>>")
                        if equip_choice == "yes":
                            if active_player.weapon_equipped:
                                print(f"\n{active_player.name} already has a weapon equipped. Replacing it with {weapon_name}.")
                                active_player.strength -= active_player.weapon_equipped.attack_power_additional
                                active_player.defense -= active_player.weapon_equipped.defense_additional
                            active_player.weapon_equipped = Weapon()
                            active_player.strength += active_player.weapon_equipped.attack_power_additional
                            active_player.defense += active_player.weapon_equipped.defense_additional
                            print(f"\n{active_player.name} equipped {weapon_name}. {active_player.name}'s new total strength is {active_player.strength} and new total defense is {active_player.defense}.")
                        else:
                            print(f"\n{active_player.name} chose not to equip the weapon.")
                        weapon_gain_chance = random.randint(1, 6)
                    elif weapon_selection == 5:
                        weapon_name = "Jedi Lightsaber"
                        equip_choice = input(f"\n{active_player.name} received {weapon_name}. Do you want to equip this weapon? (yes/no)\n>>>")
                        if equip_choice == "yes":
                            if active_player.weapon_equipped:
                                print(f"\n{active_player.name} already has a weapon equipped. Replacing it with {weapon_name}.")
                                active_player.strength -= active_player.weapon_equipped.attack_power_additional
                                active_player.defense -= active_player.weapon_equipped.defense_additional
                            active_player.weapon_equipped = Weapon_Type_Jedi()
                            if active_player.char_type != "Jedi":
                                print(f"\n{active_player.name} is untrained in using {weapon_name}. The weapon is treated as Neutral type.")
                                active_player.weapon_equipped.char_type = "Neutral"
                                active_player.strength += 1
                                active_player.defense += 0
                            else:
                                active_player.strength += active_player.weapon_equipped.attack_power_additional
                                active_player.defense += active_player.weapon_equipped.defense_additional
                                print(f"\n{active_player.name} equipped {weapon_name}. {active_player.name}'s new total strength is {active_player.strength} and new total defense is {active_player.defense}.")
                        else:
                            print(f"\n{active_player.name} chose not to equip the weapon.")
                        weapon_gain_chance = random.randint(1, 6)
                    else:
                        weapon_name = "Sith Lightsaber"
                        equip_choice = input(f"\n{active_player.name} received {weapon_name}. Do you want to equip this weapon? (yes/no)\n>>>")
                        if equip_choice == "yes":
                            if active_player.weapon_equipped:
                                print(f"\n{active_player.name} already has a weapon equipped. Replacing it with {weapon_name}.")
                                active_player.strength -= active_player.weapon_equipped.attack_power_additional
                                active_player.defense -= active_player.weapon_equipped.defense_additional
                            active_player.weapon_equipped = Weapon_Type_Sith()
                            if active_player.char_type != "Sith":
                                print(f"\n{active_player.name} is untrained in using {weapon_name}. The weapon is treated as Neutral type.")
                                active_player.weapon_equipped.char_type = "Neutral"
                                active_player.strength += 1
                                active_player.defense += 0
                            else:
                                active_player.strength += active_player.weapon_equipped.attack_power_additional
                                active_player.defense += active_player.weapon_equipped.defense_additional
                                print(f"\n{active_player.name} equipped {weapon_name}. {active_player.name}'s new total strength is {active_player.strength}.")
                        else:
                            print(f"\n{active_player.name} chose not to equip the weapon.")
                        weapon_gain_chance = random.randint(1, 6)
                else:
                    print(f"\n***NO BONUS***\n{active_player.name} did not gain a weapon this round.")
                    weapon_gain_chance = random.randint(1, 6)
        
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
