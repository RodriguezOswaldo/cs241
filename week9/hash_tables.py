# class HashTable:
#     def __init__(self):
#         self.size = 11
#         self.slots = [None] * self.size
#         self.data = [None] * self.size
#
#
#     def put(self, key, data):
#         hashvalue = self.hashfunction(key, len(self.slots))
#
#         if self.slots[hashvalue] == None:
#             self.slots[hashvalue] = key
#             self.data[hashvalue] = data
#         else:
#             if self.slots[hashvalue] == key:
#                 self.data[hashvalue] = data
#             else:
#                 nextslot = self.rehash(hashvalue, len(self.slots))
#                 while self.slots[nextslot] != None and self.slots[nextslot] != key:
#                     nextslot = self.rehash(nextslot, len(self.slots))
#
#                 if self.slots[nextslot] == None:
#                     self.slots[nextslot] = key
#                     self.data[nextslot] = data
#                 else:
#                     self.data[nextslot] = data
#
#     def hashfunction(self, key, size):
#         return key % size
#
#     def rehash(self, oldhash, size):
#         return (oldhash + 1) % size
#


mine = set('Oswaldo Rodriguez')
print(mine)

phone_numbers = {}
phone_numbers["Helena"] = "(234)233-4324"
print(phone_numbers["Helena"])

capitals = {}
capitals['Idaho'] = "Boise"
capitals['Utah'] = "Salt Lake City"
capitals['California'] = "Sacramento"

state = input("Enter a state name: ")
capital = capitals[state]

print(f"The capital of {state} is {capital}")

print("Dictionary: ")
tel = {'jack' : 4353, 'sape' : 2341}
tel['guido'] = 4124

print(tel)

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])