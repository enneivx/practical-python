# bounce.py
#
# Exercise 1.5

height = 100 # Meters
num_of_drops = 0

while num_of_drops < 10:
    height = round((height * 0.6), 4)
    num_of_drops = num_of_drops + 1
    print(num_of_drops, height)
