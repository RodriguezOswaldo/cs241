class Fish:

    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print(f"The {self.last_name} is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Trout(Fish):
    pass


class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")


print('First Fish')
print('-------------')
terry = Trout('Terry')
print(f'{terry.first_name} - {terry.last_name}')
print(f'{terry.skeleton} - {terry.eyelids}')
terry.swim()
terry.swim_backwards()

print('\nSecond Fish')
print('-------------')
casey = Clownfish('Casey')
print(f'{casey.first_name} - {casey.last_name}')
print(f'{casey.skeleton} - {casey.eyelids}')
casey.swim()
casey.live_with_anemone()

print('\nThird Fish')
print('-------------')
sharky = Shark('Sharky')
print(f'{sharky.first_name} - {sharky.last_name}')
print(f'{sharky.skeleton} - {sharky.eyelids}')
sharky.swim()
sharky.swim_backwards()
