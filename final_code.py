book = []

class Animal:
  satiety_state = "hungry"
  
  def make_sound(self):
    print(self.sound)

  def feed(self):
    self.satiety_state = "well-fed"




class Bird(Animal):

  def collect_eggs(self):
    print("You have collected", self.eggs_produced, "eggs from", self.name)
    self.eggs_produced = 0
    


class Chicken(Bird):
  def __init__(self, mass, name, sound = "кукареку", eggs_produced = 12):
    self.name = name
    self.sound = sound
    self.mass_in_kg = mass
    self.eggs_produced = eggs_produced


class Duck(Bird):
  def __init__(self, mass, name, sound = "кря кря", eggs_produced = 8):
    self.name = name
    self.sound = sound
    self.mass_in_kg = mass
    self.eggs_produced = eggs_produced



class Goose(Bird):
  def __init__(self, mass, name, sound = "га га", eggs_produced = 6):
    self.name = name
    self.sound = sound
    self.mass_in_kg = mass
    self.eggs_produced = eggs_produced





class Even_toed(Animal):
  pass


class Cow(Even_toed):
  def __init__(self, mass, name, sound = "муууу", milk = 40):
    self.name = name
    self.mass_in_kg = mass
    self.sound = sound
    self.milk_produced = milk
  def milking(self):
    print("you have milked", self.milk_produced, "litres from", self.name)



class Goat(Even_toed):
  def __init__(self, mass, name, sound = "мяяяя", milk = 20):
    self.name = name
    self.mass_in_kg = mass
    self.sound = sound
    self.milk_produced = milk
  
  def milking(self):
    print("you have milked", self.milk_produced, "litres from", self.name)




class Sheep(Even_toed):
  def __init__(self, mass, name, sound = "беееее", wool = 100):
    self.name = name
    self.mass_in_kg = mass
    self.sound = sound
    self.wool_produced = wool
  
  def shave(self):
    print("you have shaved", self.wool_produced, "kg of wool from", self.name)
    



white_goose = Goose(5, "Белый")
book.append(white_goose)


gray_goose = Goose(4, "Серый")
book.append(gray_goose)

manka_cow = Cow(25, "Манька")
book.append(manka_cow)

sheepy = Sheep(15, "Барашек")
book.append(sheepy)

curly_sheep = Sheep(17, "Кудрявый")
book.append(curly_sheep)

co_co_chicken = Chicken(4, "Ко-Ко")
book.append(co_co_chicken)

kukareku_chicken = Chicken(5, "Кукареку")
book.append(kukareku_chicken)



horns_goat = Goat(14, "Рога")
book.append(horns_goat)


hooves_goat = Goat(16, "Копыта")
book.append(hooves_goat)


kryakwa_duck = Duck(14, "Кряква")
book.append(kryakwa_duck)




heaviest_animal = ""
biggest_weight = 0
weight = 0
for animal in book:
  weight += animal.mass_in_kg
  if animal.mass_in_kg > biggest_weight:
    biggest_weight = animal.mass_in_kg
    heaviest_animal = animal.name




print("Total weight of all animals here is ", weight)
print("Heaviest animal here is ", heaviest_animal," and it's mass is ", biggest_weight)
