class agent:
    secondary_weapon = "classic"
    def __init__(self, name, role):
            self.name = name
            self.role = role
            
    def walk(self, direction):
        print("walking", direction)
    
    def crouch(self):
        print("crouching")
    
killjoy = agent("Killjoy", "Sentinel")
omen = agent("Omen", "Controller")

print(killjoy.name, killjoy.role, killjoy.secondary_weapon)
print(omen.name, omen.role, omen.__class__.secondary_weapon)

killjoy.secondary_weapon = "ghost"

print(killjoy.name, killjoy.role, killjoy.secondary_weapon)
killjoy.crouch()
omen.walk("left")

