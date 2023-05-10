import os
display_on = True
class Undead:
    Undead.undead_list = []
    
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
        self.__class__.Undead.undead_list.append(self)
    
    def isDead(self):
        return self.__hp <= 0

    def attack(self, tgt):
        if self.__hp > 50:
            tgt.hp -= self.__hp * 0.5
            print(f"{self.__name} attacked {tgt.name} for {self.__hp * 0.5} damage!")
        else:
            print(f"{self.__name} cannot attack. Its HP is too low.")
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getHP(self):
        return self.__hp

    def setHP(self, hp):
        self.__hp = hp

    @classmethod
    def display_all(cls):
        if len(cls.Undead.undead_list) == 0:
            print("No current undead characters available.")
        else:
            print("Current Undead Characters Details:")
            for undead in cls.Undead.undead_list:
                undead.display_info()

class Zombie(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self, tgt):
        if self.hp > 50:
            tgt.hp -= self.hp * 0.5
            os.system('cls')
            print(f"{self.name} attacked {tgt.name} for {self.hp * 0.5} damage!")
        else:
            os.system('cls')
            print(f"{self.name} cannot attack. Its HP is too low.")

    def eat(self, tgt):
        self.hp += tgt.hp * 0.5
        os.system('cls')
        print(f"{self.name} ate {tgt.name} and restored {tgt.hp * 0.5} HP!")
        tgt.hp = 0

    def command_undead(self, command, tgt=None):
        if self.isDead():
            os.system('cls')
            print(f"{self.name} is dead and cannot be commanded!")
            return
        elif tgt.isDead():
            os.system('cls')
            print(f"{tgt.name} is dead and cannot be commanded!")
            return      
        if command == "attack":
            self.attack(tgt)
        elif command == "eat":
            self.eat(tgt)
        else:
            super().command_undead(command, tgt)

    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")   

class Vampire(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
       
    def __init__(self, name):
        super().__init__(name, 120)

    def attack(self, tgt):
        tgt.hp -= self.hp
        os.system('cls')
        print(f"{self.name} attacked {tgt.name} for {self.hp} damage!")

    def bite(self, tgt):
        self.hp += tgt.hp * 0.8
        os.system('cls')
        print(f"{self.name} bit {tgt.name} and gained {tgt.hp * 0.8} HP!")
        tgt.hp *= 0.2

    def command_undead(self, command, tgt=None):
        if self.isDead():
            os.system('cls')
            print(f"{self.name} is dead and cannot be commanded!")
            return
        elif tgt.isDead():
            os.system('cls')
            print(f"{tgt.name} is dead and cannot be commanded!")
            return
        if command == "attack":
            self.attack(tgt)
        elif command == "bite":
            self.bite(tgt)
        else:
            super().command_undead(command, tgt)

    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")

class Skeleton(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 80)

    def attack(self, tgt):
        tgt.hp -= self.hp * 0.7
        os.system('cls')
        print(f"{self.name} attacked {tgt.name} for {self.hp * 0.7} damage!")

    def command_undead(self, command, tgt=None):
        if self.isDead():
            os.system('cls')
            print(f"{self.name} is dead and cannot be commanded!")
            return
        elif tgt.isDead():
            os.system('cls')
            print(f"{tgt.name} is dead and cannot be commanded!")
            return
        if command == "attack":
            self.attack(tgt)
        else:
            super().command_undead(command, tgt)
            
    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")

class Ghost(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 40) # initial HP is half of the default HP of undead
    
    def attack(self, tgt):
        tgt.hp -= self.hp * 0.2
        os.system('cls')
        print(f"{self.name} attacked {tgt.name} for {self.hp * 0.2} damage!")
    
    def haunt(self, tgt):
        hp_gain = tgt.hp * 0.1 # gain 10% of the tgt's HP
        self.hp += hp_gain
        os.system('cls')
        print(f"{self.name} haunted {tgt.name} and gained {hp_gain:.2f} HP.")
        
    def command_undead(self, command, tgt=None):
        if self.isDead():
            os.system('cls')
            print(f"{self.name} is dead and cannot be commanded!")
            return
        elif tgt.isDead():
            os.system('cls')
            print(f"{tgt.name} is dead and cannot be commanded!")
            return
        if command == "attack":
            self.attack(tgt)
        elif command == "haunt":
            self.haunt(tgt)
        else:
            super().command_undead(command, tgt)

    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")

class Lich(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 100)
    
    def attack(self, tgt):
        damage = self.hp * 0.7
        tgt.hp -= damage
        os.system('cls')
        print(f"{self.name} attacked {tgt.name} for {damage} damage!")

    def cast_spell(self, tgt):
        hp_loss = tgt.hp * 0.1 # lose 10% of the tgt's HP
        tgt.hp -= hp_loss
        self.hp += hp_loss
        os.system('cls')
        print(f"{self.name} cast a spell on {tgt.name} and gained {hp_loss:.2f} HP.")

    
    def command_undead(self, command, tgt=None):
        if self.isDead():
            os.system('cls')
            print(f"{self.name} is alive but cannot be commanded!")
            return
        elif tgt.isDead():
            os.system('cls')
            print(f"{tgt.name} is dead and cannot be commanded!")
            return       
        if command == "attack":
            self.attack(tgt)
        elif command == "cast spell":
            self.cast_spell(tgt)
        else:
            super().command_undead(command, tgt)
            
    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")

class Mummy(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 150)
        self.revive_hp = 150
        
    def attack(self, tgt):
        damage = self.hp * 0.5 + tgt.hp * 0.1
        tgt.hp -= damage
        os.system('cls')
        print(f"{self.name} attacked {tgt.name} for {damage} damage!")

    def die(self):
        self.hp = 0
        os.system('cls')
        print(f"{self.name} died!")

    def revive(self):
        self.hp = self.revive_hp
        os.system('cls')
        print(f"{self.name} is revived and has {self.revive_hp} HP!")

    def command_undead(self, command, tgt=None):       
        if command == "attack":
            self.attack(tgt)
        elif command == "die":
            self.die()
        elif command == "revive":
            self.revive()
        else:
            super().command_undead(command, tgt)
            
    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")
    
def create_undead():
    print("UNDEAD CREATION:")
    type = input("Enter type of undead(zombie, vampire, skeleton, ghost, lich, mummy): ")
    name = input("Enter name of undead: ")
    while any(undead.name == name for undead in Undead.undead_list):
        print("This name is already taken. Please enter a different name.")
        name = input("Enter name of undead: ")
    if type == "zombie":
        return Zombie(name)
    elif type == "vampire":
        return Vampire(name)
    elif type == "skeleton":
        return Skeleton(name)
    elif type == "ghost":
        return Ghost(name)
    elif type == "lich":
        return Lich(name)
    elif type == "mummy":
        return Mummy(name)
    else:
        print("Invalid type of undead!")
        return None

def command_undead():
    name = input("Enter name of undead to command: ")
    command = input("\nCommands:\n- attack (Available for Every Undead)\n- bite (Vampire only)\n- eat (Zombie Only)\n- haunt (Ghost Only)\n- cast spell (Lich Only)\n- die (Mummy Only)\n- revive (Mummy Only)\n\nEnter command:")
    
    if command not in ["attack", "bite", "eat", "haunt", "cast spell", "die", "revive"]:
        os.system('cls')
        print("Invalid command!")
        return
    
    tgtName = None
    if command not in ["die", "revive"]:
        tgtName = input("Enter name of tgt: ")
        
    try:
        undead = None
        for u in Undead.undead_list:
            if u.name == name:
                undead = u
                break

        if undead is None:
            os.system('cls')        
            print("Undead not found!")
            return

        tgt = None
        if tgtName:
            for u in Undead.undead_list:
                if u.name == tgtName:
                    tgt = u
                    break
            if tgt is None:
                os.system('cls')
                print("tgt not found!")
                return
            
        undead.command_undead(command, tgt)
        
    except AttributeError:
        os.system('cls')
        print("Command not available for this undead subclass!")

def display_undead():
    Undead.display_all()

def menu():
    global display_on
    while True:
        print("\n")
        print("=" * 27)
        print("Welcome to the Undead Game!")
        print("=" * 27)
        print("1. Create an undead")
        print("2. Command an undead")
        print("3. Toggle display of undead characters")
        print("4. Exit game\n")
        
        choice = input("Enter your choice: ")
        print("\n")
        
        if choice == "1":
            os.system('cls')
            create_undead()
            os.system('cls')
        elif choice == "2":
            command_undead()
            print("\n")
        elif choice == "3":
            display_on = not display_on
            if display_on:
                os.system('cls')
                print("Undead display is now on.")
            else:
                os.system('cls')
                print("Undead display is now off.")
        elif choice == "4":
            os.system('cls')
            print("CREATED BY FRANZ PHILLIP G. DOMINGO")            
            break
        else:
            print("Invalid choice. Please try again.")
        if display_on:
            display_undead()

menu()
