import random

names = ["dristhuth","gurtheos","kriurphax","rikrun","koskrain","tushkoc","raskejux", "tesgiujeks", "kabotre", "muduktith"]

index = random.randint(0, len(names) - 1)
greeting = f"Hello {names[index]}, it is good to see you again!"

print(greeting)

