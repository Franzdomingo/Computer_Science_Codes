import random

class Undead:
    
    def __init__(self, name=None, hp=None):
        if name != None and hp != None:
            self.__hp = hp
            self.__name = name + " - Undead"
        else:
            self.__hp = 100
            self.__name = "Undead"
        self.__isDead = False
    
    # dead is a boolean
    def isDead(self, dead = None):
        if dead == None:
            return self.__isDead
        else:
            self.__isDead = dead
        
    def getName(self):
        return self.__name
    
    def getHP(self):
        return self.__hp
    
    def setName(self, name):
        self.__name = name
    
    def setHP(self, hp=None, multiplier=None):
        if multiplier == None:
            self.__hp = hp
        else:
            self.__hp = self.__hp * multiplier
            
    def attack(self, undead):
        if isinstance(undead, Undead):
            damage = self.getHP() * 0.5
            undead.setHP(undead.getHP() - damage)
            print(self.getName() + " attacked " + undead.getName() + " for " + str(damage) + " damage!")
        else:
            print("Invalid target!")
    
    def getStanding(self):
        return self.getName() + " HP: " + str(self.getHP()) + " State: " + ("alive" if not self.isDead() else "dead")
    
class Zombie(Undead):
    
    def __init__(self, name=None):
        super().__init__(name=name, hp=100)
    
    def attack(self, undead):
        if self.getHP() > 50:
            super().attack(undead)
        else:
            print(self.getName() + " cannot attack as its HP is less than or equal to 50!")
    
    def eat(self, undead):
        if isinstance(undead, Undead):
            hp_gain = undead.getHP() * 0.5
            self.setHP(self.getHP() + hp_gain)
            print(self.getName() + " ate " + undead.getName() + " and gained " + str(hp_gain) + " HP!")
        else:
            print("Invalid target!")
    
class Vampire(Undead):
    
    def __init__(self, name=None):
        super().__init__(name=name, hp=120)
    
    def attack(self, undead):
        if self.getHP() > 0:
            damage = self.getHP()
            undead.setHP(undead.getHP() - damage)
            print(self.getName() + " attacked " + undead.getName() + " for " + str(damage) + " damage!")
        else:
            print(self.getName() + " cannot attack as its HP is 0!")
    
    def bite(self, undead):
        if isinstance(undead, Undead):
            hp_gain = undead.getHP() * 0.8
            self.setHP(self.getHP() + hp_gain)
            print(self.getName() + " bit " + undead.getName() + " and gained " + str(hp_gain) + " HP!")
        else:
            print("Invalid target!")


class Skeleton(Undead):
    
    def __init__(self, name = None):
        super().__init__(name, 80)
    
    def attack(self, undead):
        damage = self.getHP() * 0.7
        undead.setHP(undead.getHP() - damage)
        
        if undead.getHP() <= 0:
            undead.isDead(True)
            print(f"{undead.getName()} has died.")

class Ghost(Undead):

    def __init__(self, name=None):
        super().__init__(name=name, hp=40)
        self.__initial_hp = self.getHP()
        self.__isHaunting = False

    def haunt(self, target):
        if target != self:
            hp_gain = target.getHP() * 0.1
            self.setHP(self.getHP() + hp_gain)
            self.__isHaunting = True
            print(self.getName(), "has haunted", target.getName(), "and gained", hp_gain, "HP")
        else:
            print("Cannot haunt itself")

    def getInitialHP(self):
        return self.__initial_hp

    def getIsHaunting(self):
        return self.__isHaunting

    def setIsHaunting(self, value):
        self.__isHaunting = value

    def attack(self, target):
        if self.getIsHaunting():
            damage = self.getHP() * 0.2
            target_damage = damage * 0.1
        else:
            damage = self.getHP() * 0.2
            target_damage = damage
        self.setIsHaunting(False)
        target.setHP(target.getHP() - target_damage)
        print(self.getName(), "has attacked", target.getName(), "and dealt", target_damage, "damage")

    def getStatus(self):
        state = "alive" if not self.isDead() else "dead"
        print(self.getName())
        print("HP:", self.getHP())
        print("State:", state)
        if self.getIsHaunting():
            print("Is haunting")

class Lich:
    def __init__(self, hp):
        self.hp = hp
        self.max_hp = hp
        self.alive = True
    
    def attack(self):
        if self.alive:
            attack_damage = int(self.hp * 0.7)
            return attack_damage
        else:
            return 0
    
    def absorb_hp(self, undead):
        if self.alive and isinstance(undead, Undead):
            hp_to_absorb = int(undead.hp * 0.1)
            self.hp += hp_to_absorb
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            undead.hp -= hp_to_absorb
    
    def take_damage(self, damage):
        if self.alive:
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                self.alive = False
