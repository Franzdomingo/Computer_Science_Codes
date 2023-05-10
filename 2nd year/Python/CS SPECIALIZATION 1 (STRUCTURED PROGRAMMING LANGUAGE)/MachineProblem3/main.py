import os
display_on = True

undead_list = []

class Undead:
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
        undead_list.append(self)
    
    def isDead(self):
        return self.__hp <= 0
   
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
        if len(undead_list) == 0:
            print("------------------------------------------------------------------------------")
            print("No current undead characters available.")
            print("------------------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------------------")
            print("----------------------Current Undead Characters Details-----------------------")
            print("------------------------------------------------------------------------------")
            for undead in undead_list:
                undead.display_info()
            print("------------------------------------------------------------------------------")
    
    def display_info(self):
        status = 'Alive' if (self.hp > 0 or isinstance(self, Lich)) else 'Perished' if isinstance(self, Ghost) else 'Dead'
        print(f"{self.name} - {type(self).__name__} - HP: {self.hp if self.hp > 0 else '0'} - Status: {status}")       

class Zombie(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self, target):
        if self.hp > 50:
            if isinstance(target, Ghost):
                target.hp -= (self.hp * 0.5)*0.1
                os.system('cls')
                print("------------------------------------------------------------------------------")
                print(f"{self.name} attacked {target.name} for {(self.hp * 0.5)*0.1:.2f} damage!")
                print("------------------------------------------------------------------------------")
            else:
                target.hp -= self.hp * 0.5
                os.system('cls')
                print("------------------------------------------------------------------------------")
                print(f"{self.name} attacked {target.name} for {self.hp * 0.5:.2f} damage!")
                print("------------------------------------------------------------------------------")
        else:
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} cannot attack. Its HP is too low.")
            print("------------------------------------------------------------------------------")

    def eat(self, target):
        self.hp += target.hp * 0.5
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} ate {target.name} and restored {target.hp * 0.5:.2f} HP!")
        print("------------------------------------------------------------------------------")
        target.hp = 0

    def command_undead(self, command, target=None):
        if self.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        elif target.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{target.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return      
        if command == "attack":
            self.attack(target)
        elif command == "eat":
            self.eat(target)
        else:
            super().command_undead(command, target)

class Vampire(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
       
    def __init__(self, name):
        super().__init__(name, 120)

    def attack(self, target):
        if isinstance(target, Ghost):
            target.hp -= self.hp * 0.1
        else:
            target.hp -= self.hp
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} attacked {target.name} for {self.hp * 0.1 if isinstance(target, Ghost) else self.hp} damage!")
        print("------------------------------------------------------------------------------")
    def bite(self, target):
            self.hp += target.hp * 0.8
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} bit {target.name} and gained {target.hp * 0.8:.2f} HP!")
            print("------------------------------------------------------------------------------")

    def command_undead(self, command, target=None):
        if self.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        elif target.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{target.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        if command == "attack":
            self.attack(target)
        elif command == "bite":
            self.bite(target)
        else:
            super().command_undead(command, target)
            
class Skeleton(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 80)

    def attack(self, target):
        if isinstance(target, Ghost):
            target.hp -= (self.hp * 0.7)*0.1
        else:
            target.hp -= self.hp * 0.7
        os.system('cls')
        if isinstance(target, Ghost):
            print("------------------------------------------------------------------------------")
            print(f"{self.name} attacked {target.name} for {(self.hp * 0.7)*0.1:.2f} damage!")
            print("------------------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------------------")
            print(f"{self.name} attacked {target.name} for {self.hp * 0.7:.2f} damage!")
            print("------------------------------------------------------------------------------")

    def command_undead(self, command, target=None):
        if self.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        elif target.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{target.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        if command == "attack":
            self.attack(target)
        else:
            super().command_undead(command, target)
            
class Ghost(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 100) # initial HP is half of the default HP of undead
    
    def attack(self, target):
        if isinstance(target, Ghost):
            target.hp -= (self.hp * 0.2)*0.1
        else:
            target.hp -= self.hp * 0.2
        os.system('cls')
        if isinstance(target, Ghost):
            print("------------------------------------------------------------------------------")
            print(f"{self.name} attacked {target.name} for {self.hp * 0.02:.2f} damage!")
            print("------------------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------------------")
            print(f"{self.name} attacked {target.name} for {self.hp * 0.2:.2f} damage!")
            print("------------------------------------------------------------------------------")
    
    def haunt(self, target):
        hp_gain = target.hp * 0.1
        self.hp += hp_gain
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} haunted {target.name} and gained {hp_gain:.2f} HP.")
        print("------------------------------------------------------------------------------")
        
    def command_undead(self, command, target=None):
        if self.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        elif target.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{target.name} is dead and cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        if command == "attack":
            self.attack(target)
        elif command == "haunt":
            self.haunt(target)
        else:
            super().command_undead(command, target)

class Lich(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 80)
    
    def attack(self, target):
        if isinstance(target, Ghost):
            damage = (self.hp * 0.7)*0.1
            target.hp -= damage
        else:
            damage = self.hp * 0.7
            target.hp -= damage
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} attacked {target.name} for {damage:.2f} damage!")
        print("------------------------------------------------------------------------------")

    def cast_spell(self, target):
        if isinstance(target, Ghost):
            hp_loss = (target.hp * 0.1)*0.1
        else:
            hp_loss = target.hp * 0.1
        target.hp -= hp_loss
        self.hp += hp_loss
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} cast a spell on {target.name} and gained {hp_loss:.2f} HP.")
        print("------------------------------------------------------------------------------")
    
    def command_undead(self, command, target=None):
        if self.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{self.name} is alive but cannot be commanded!")
            print("------------------------------------------------------------------------------")
            return
        elif target.isDead():
            os.system('cls')
            print("------------------------------------------------------------------------------")
            print(f"{target.name} is dead!")
            print("------------------------------------------------------------------------------")
            return       
        if command == "attack":
            self.attack(target)
        elif command == "cast spell":
            self.cast_spell(target)
        else:
            super().command_undead(command, target)
            
class Mummy(Undead):
    
    name = property(Undead.getName, Undead.setName)
    hp = property(Undead.getHP, Undead.setHP)
    
    def __init__(self, name):
        super().__init__(name, 100)
        self.revive_hp = 100
        
    def attack(self, target):
        if isinstance(target, Ghost):
            damage = (self.hp * 0.5 + target.hp * 0.1)*0.1
            target.hp -= damage
        else:
            damage = self.hp * 0.5 + target.hp * 0.1
            target.hp -= damage
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} attacked {target.name} for {damage:.2f} damage!")
        print("------------------------------------------------------------------------------")

    def die(self):
        self.hp = 0
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} died!")
        print("------------------------------------------------------------------------------")

    def revive(self):
        self.hp = self.revive_hp
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print(f"{self.name} is revived and has {self.revive_hp} HP!")
        print("------------------------------------------------------------------------------")

    def command_undead(self, command, target=None):       
        if command == "attack":
            self.attack(target)
        elif command == "die":
            self.die()
        elif command == "revive":
            self.revive()
        else:
            super().command_undead(command, target)
            
def create_undead():
    print("\n")
    print("------------------------------------------------------------------------------")
    print("---------------------------------Create Undead--------------------------------")
    print("------------------------------------------------------------------------------")
    type = input("- zombie\n- vampire\n- skeleton\n- ghost\n- lich\n- mummy\nEnter type of undead: ")
    print("------------------------------------------------------------------------------")
    name = input("Enter name of undead: ")
    if (name == None or name == ""):
        print("No name provided. Please enter a name")
        return None    
    while any(undead.name == name for undead in undead_list):
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
    print("------------------------------------------------------------------------------")
    name = input("Enter name of undead to command: ")
    print("------------------------------------------------------------------------------")
    command = input("Commands:\n- attack (Available for Every Undead)\n- bite (Vampire only)\n- eat (Zombie Only)\n- haunt (Ghost Only)\n- cast spell (Lich Only)\n- die (Mummy Only)\n- revive (Mummy Only)\n\nEnter command:")
    
    if command not in ["attack", "bite", "eat", "haunt", "cast spell", "die", "revive"]:
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print("Invalid command!")
        print("------------------------------------------------------------------------------")
        return
    
    targetName = None
    if command not in ["die", "revive"]:
        print("------------------------------------------------------------------------------")
        targetName = input("Enter name of target: ")
        print("------------------------------------------------------------------------------")
        
    try:
        undead = None
        for u in undead_list:
            if u.name == name:
                undead = u
                break

        if undead is None:
            os.system('cls')  
            print("------------------------------------------------------------------------------")     
            print("Undead not found!")
            print("------------------------------------------------------------------------------")
            return

        target = None
        if targetName:
            for u in undead_list:
                if u.name == targetName:
                    target = u
                    break
            if target is None:
                os.system('cls')
                print("------------------------------------------------------------------------------")
                print("Target not found!")
                print("------------------------------------------------------------------------------")
                return
            
        undead.command_undead(command, target)
        
    except AttributeError:
        os.system('cls')
        print("------------------------------------------------------------------------------")
        print("Command not available for this undead subclass!")
        print("------------------------------------------------------------------------------")

def display_undead():
    Undead.display_all()

def menu():
    global display_on
    while True:
        print("\n")
        print("------------------------------------------------------------------------------")
        print("-----------------------------------Game Menu----------------------------------")
        print("------------------------------------------------------------------------------")
        print("1. Create an undead")
        print("2. Command an undead")
        print("3. Toggle display of undead characters")
        print("4. Exit game\n")
        print("------------------------------------------------------------------------------")
        choice = input("Enter your choice: ")
        print("------------------------------------------------------------------------------")
        
        if choice == "1":
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
            print("------------------------------------------------------------------------------")
            print("---------------------CREATED BY FRANZ PHILLIP G. DOMINGO----------------------")     
            print("------------------------------------------------------------------------------")       
            break
        else:
            print("------------------------------------------------------------------------------")
            print("Invalid choice. Please try again.")
            print("------------------------------------------------------------------------------")
        if display_on:
            display_undead()

menu()
