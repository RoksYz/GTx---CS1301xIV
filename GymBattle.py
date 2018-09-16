class Pokemon:
    
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def would_defeat(self,_different_):
        if self.power > _different_.power:
            return True
        else:
            return False
        
#If your code works correctly, this will originally run
#error-free and print:
#Pikachu
#500
#False
#True
new_pokemon_1 = Pokemon("Pikachu", 500)
print(new_pokemon_1.name)
print(new_pokemon_1.power)

new_pokemon_2 = Pokemon("Charizard", 2412)
new_pokemon_3 = Pokemon("Squirtle", 312)
print(new_pokemon_1.would_defeat(new_pokemon_2))
print(new_pokemon_1.would_defeat(new_pokemon_3))

