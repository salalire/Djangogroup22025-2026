class animal:
    def make_sound(self):
        print("All animals can make sound!")
        
class cat(animal):
    def make_sound(self):
        print("Cats makee the sound meww")
a=animal()
a.make_sound()
c=cat()
c.make_sound()
        
        
    
