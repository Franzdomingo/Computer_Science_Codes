class Undead:
    undead_list = []
    
    def __init__(self, name, hp ):
        self.name = name
        self.hp = hp
        self.__class__.undead_list.append(self)

    def attack(self, target):
        if self.hp > 50:
            target.hp -= self.hp * 0.5
            print(f"{self.name} attacked {target.name} for {self.hp * 0.5} damage!")
        else:
            print(f"{self.name} cannot attack. Its HP is too low.")

    def display_info(self):
        print(f"{self.name} ({type(self).__name__}) - HP: {self.hp}")

    def command_undead(self, command, target=None):
        print(f"{self.name} is trying to {command} {target.name}...")
        if command == "attack":
            self.attack(target)
        elif command == "bite":
            self.bite(target)
        elif command == "haunt":
            self.haunt(target)
        elif command == "cast spell":
            self.cast_spell(target)
            
    @classmethod
    def display_all(cls):
        print("All undead:")
        for undead in cls.undead_list:
            undead.display_info()
 

class Zombie(Undead):
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self, target):
        if self.hp > 50:
            target.hp -= self.hp * 0.5
            print(f"{self.name} attacked {target.name} for {self.hp * 0.5} damage!")
        else:
            print(f"{self.name} cannot attack. Its HP is too low.")

    def eat(self, target):
        self.hp += target.hp * 0.5
        print(f"{self.name} ate {target.name} and restored {target.hp * 0.5} HP!")
        target.hp = 0

    def command_undead(self, command, target=None):
        if command == "attack":
            self.attack(target)
        elif command == "eat":
            self.eat(target)
        else:
            super().command_undead(command, target)

class Vampire(Undead):
    def __init__(self, name):
        super().__init__(name, 120)

    def attack(self, target):
        target.hp -= self.hp
        print(f"{self.name} attacked {target.name} for {self.hp} damage!")

    def bite(self, target):
        self.hp += target.hp * 0.8
        print(f"{self.name} bit {target.name} and restored {target.hp * 0.8} HP!")
        target.hp *= 0.2

    def command_undead(self, command, target=None):
        if command == "attack":
            self.attack(target)
        elif command == "bite":
            self.bite(target)
        else:
            super().command_undead(command, target)

class Skeleton(Undead):
    def __init__(self, name):
        super().__init__(name, 80)

    def attack(self, target):
        target.hp -= self.hp * 0.7
        print(f"{self.name} attacked {target.name} for {self.hp * 0.7} damage!")

    def command_undead(self, command, target=None):
        if command == "attack":
            self.attack(target)
        else:
            super().command_undead(command, target)

class Ghost(Undead):
    def __init__(self, name):
        super().__init__(name, 40) # initial HP is half of the default HP of undead
    
    def attack(self, target):
        damage = self.hp * 0.2 # attack damage is only 20% of its HP
        target.receive_damage(damage)
        print(f"{self.name} attacked {target.name} for {damage:.2f} damage.")
    
    def haunt(self, target):
        hp_gain = target.hp * 0.1 # gain 10% of the target's HP
        self.hp += hp_gain
        print(f"{self.name} haunted {target.name} and gained {hp_gain:.2f} HP.")

def create_undead():
    type = input("Enter type of undead (zombie, vampire, skeleton, ghost): ")
    name = input("Enter name of undead: ")
    if type == "zombie":
        return Zombie(name)
    elif type == "vampire":
        return Vampire(name)
    elif type == "skeleton":
        return Skeleton(name)
    elif type == "ghost":
        return Ghost(name)
    else:
        print("Invalid type of undead!")
        return None

def command_undead():
    name = input("Enter name of undead to command: ")
    command = input("Enter command (attack, bite, eat, haunt, cast spell): ")
    target_name = input("Enter name of target: ")
    undead = None
    for u in Undead.undead_list:
        if u.name == name:
            undead = u
            break
    if undead is None:
        print("Undead not found!")
        return
    target = None
    for u in Undead.undead_list:
        if u.name == target_name:
            target = u
            break
    if target is None:
        print("Target not found!")
        return
    undead.command_undead(command, target)

def display_undead():
    Undead.display_all()

def menu():
    while True:
        print("\n1. Create Undead")
        print("2. Command Undead")
        print("3. Display all Undead")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_undead()
        elif choice == "2":
            command_undead()
        elif choice == "3":
            display_undead()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


menu()
