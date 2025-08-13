STARTING NOTE
- It might be helpful to view this by pressing ctl+shft+v to see it in preview mode. 
- Also if you are having a hard time remember the git commands, feel free to make a file and populate it with the common commands.

<!-- --------------- REF A --------------- -->
```py
# Your current code
def __init__(self, name, weapon_equipped=None, limited_weapon_equipped=None):
    self.name = name
    self.health = 30
    self.strength = 0
    self.defense = 0
    self.is_alive = True
    self.weapon_equipped = weapon_equipped
    self.limited_weapon_equipped = limited_weapon_equipped

# Improved Code
def __init__(self, name, health=30, strength=0, defense=0, is_alive=True, weapon_equipped=None, limited_weapon_equipped=None):
    self.name = name
    self.health = health
    self.strength = strength
    self.defense = defense
    self.is_alive = True # CRH: Why did you leave this as a boolean value rather than assigning the variable like you did with all the others?
    self.weapon_equipped = weapon_equipped
    self.limited_weapon_equipped = limited_weapon_equipped
```

When doing it your current way we would only be able to create a base character class with those exact attribute values. however when we do it the improved way we can initialize a base character instance like `A` or like `B`

```py
# A
p1 = Character("Tommy")

# B
p2 = Character("Tommy", 80, 10, is_alive=False)
```

in `B` tommy is starting with greater health and strength and is not alive because he is a zombie. However we don't have to write any additional code because they are using the same base class.

<!-- --------------- REF B --------------- -->

```py
# ... your previous code
def change_health(self, amount):
    if amount < 0:
        print(f"{self.name}'s health decreased by {abs(amount)}.")
        # Exhibit A
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
        # Exhibit B
        self.health += amount
        print(f"{self.name}'s health is now {self.health}.")
        return self
    else:
        print(f"{self.name}'s health remains unchanged.")
        return self
# ...
```
Here you are rewriting how you change your health. while this is just a single line it is better to only have one place where you are determaning how you go about changing your health. That way in the future if you want to change how things work you just need to change it in a single location. Great work on using the abs() functionality

```py
def change_health(self, amount):
    # we can write an if statement on a single line. 
    health_direction = 'decreased' if amount < 0 else 'increased'
    
    self.health += amount
    print(f"{self.name}'s health has {health_direction} by {abs(amount).}")
    print(f"{self.name}'s health is now {self.health}")

    if self.health <= 0:
        self.is_alive = False
        print(f"{self.name} has been defeated!")
        return self
    
    if amount == 0:
        print(f"{self.name}'s health remains unchanged.")
        return self

    return self
```

A couple of things to remember here...no lines inside the function run after the `return` statement. so we can check to see if the health is <= 0 and if it is we will switch is_alive and do the print statement and then return and the function will be done. it will never get to line 79. 

<!-- --------------- REF C --------------- -->

Here you are creating a weapons class and then inheriting different types of weapons based off that base weapons class. This is great! I would like you to think deeper though. It could look like this

```
Weapons
├─ melee 
│  └─ Lightsabers
│     ├─ Jedi
│     └─ Sith
└─ Range
   ├─ Ninja Stars
   └─ Guns
```
You each layer you make builds off of each other.

```py
class Weapon:
    def __init__(self, name, attack_pwr, def_pwr, char_type, limited_use=False):
        self.name = name
        self.attack_pwr = attack_pwr
        self.def_pwr = def_pwr
        self.char_type = char_type
        self.limited_use = limited_use

    def attack(self):
        # basic code for attacking with the weapon (could be different than base character attack). Although if you code it so that your fists are a weapon then maybe removing the attack and block function from the character class and have them here instead.
        pass

    def block(self):
        # same as above
        pass

class Melee(Weapon):
    def __init__(self, name, attack_pwr, char_type, swing_speed, impact_type="slash", def_pwr=3, limited_use=False):
        super().__init__(name, attack_pwr, def_pwr, char_type, limited_use)
        self.swing_speed = swing_speed 
        self.impact_type = impact_type 

    def swing(self):
        # Code what to do for a swing...
        # Are they close enough...too close...etc.
        pass

    def parry(self):
        # code for a parry
        pass


class Range(Weapon):
    def __init__(self, name, attack_pwr, char_type, effective_range, noise_level, reload_time=5, def_pwr=0, limited_use=True):
        super().__init__(name, attack_pwr, def_pwr, char_type, limited_use)
        self.reload_time = reload_time
        self.effective_range = effective_range 
        self.noise_level = noise_level 

    def reload(self):
        # code for reloading
        pass

    def aim(self):
        # code for aiming
        pass

class Lightsaber(Melee):
    def __init__(self, name, attack_pwr, char_type, swing_speed=10, impact_type="slash", def_pwr=3, limited_use=False):
        super(name, attack_pwr, char_type, swing_speed, impact_type, def_pwr, limited_use)

    # lightsaber doesn't need attack or block because it inherits it from the super() (ie:Melee class) which inherits it from its super() (ie: weapons class). UNLESS the attack is different...for instance maybe the lightsaber class has a throw attack. 

    def throw_attack(self):
        # Some code for the throw aspect of the attack. like some kind of increase/temporary range attibute given 
        
        # this will call on the base weapon's attack. 
        super().attack()

        # maybe a option to potentially lose the lightsaber. 


# now if we want to make an instance of a Jedi lightsaber it might look like this ... (multiple instances)
jedi_saber_1 = Lightsaber("Dawnshard", attack_pwr=1, def_pwr=2, char_type="jedi")
jedi_saber_2 = Lightsaber("Starflare", attack_pwr=1, def_pwr=2, char_type="jedi")
jedi_saber_3 = Lightsaber("Echo Blade", attack_pwr=1, def_pwr=2, char_type="jedi")

# a sith lightsaber (multiple instances)
sith_saber_1 = Lightsaber("Bloodreign", attack_pwr=3, def_pwr=0, char_type="sith")
sith_saber_2 = Lightsaber("Nightscar", attack_pwr=3, def_pwr=0, char_type="sith")
sith_saber_3 = Lightsaber("Voidfang", attack_pwr=3, def_pwr=0, char_type="sith")

```

This way we are using the power of inheritance to reduce the amount of code we need to write. we can change the attributes between the jedi/sith lightsabers without creating a new class. unless, we want the sith saber to do [method/action] something that the jedi saber can't do. then we would make a class `class SithSaber(Lightsaber)` and give it methods that the normal `Lightsaber` class doesn't have. 


I think you can take these concepts and apply them to your character classes as well. We will cover this more on thursday. 

<!-- --------------- REF D --------------- -->
This will be the last thing just something to think about...
in this battle function you have a total of 134 lines of code. For sure this function is doing more than 1 or 2 things, that means we can break it up. maybe make a `turn` function that handles the turn and a `choice` function (using a dictionary instead of if statements) to handle program-user interaction. Maybe a `end_game` function to handle the closing of the game and a `start_game` function to handle the beginning introduction of the game. These are some idea's without diving deep into this code block. I would recomend that you look through it and see how you can improve it. It always helped me to remind myself to think of the game function like it is going to be used in an arcade of games and therefore there could be multiple instances running at the same time, it really is no different than your `Character` class or your `Weapon` class. 