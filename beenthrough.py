import time
from animation import *     

line1 = "\tI'm dedicated"
line2 = "I'm dedicated to you  "
line3 = "I've seen so many faces"
line4 = "But you're the best"
line4a = "\t\tthat I've been through"
line5 = "I've been so many places"
line6 = "But you're the one"
line6a = "\t     I run home"
line6b = "\t\t\tto"
line7 = "    You shine"
line7a = " like the stars"
line8 = "      You light"
line8a = "\t\tup my heart"
line9 = "I've seen so many faces"

fade_in_text(line1, .06)
time.sleep(.5)
show_fade_in_and_each_letter(line2, .06)
time.sleep(.7)
print()

fade_in_from_sides(line3, .09, 20)
print()
time.sleep(2.)
show_each_letter(line4, .05)
print()
time.sleep(.5)
show_each_letter(line4a, .05)

print()
time.sleep(.2)
fade_in_from_sides(line5, .06, 15)
time.sleep(2.5)
print()
show_fade_in_and_each_letter(line6, .06)
time.sleep(.2)
print()
show_each_letter(line6a, .05)
time.sleep(.5)
fade_in_text(line6b, .09)
print()

time.sleep(.5)
fade_in_text(line7, .09)
time.sleep(.5)
show_each_letter(line7a, .05)
print()

time.sleep(.5)
show_each_letter(line8, .09)
time.sleep(.5)
fade_in_text(line8a, .09)
print()
fade_in_from_sides(line3, .09, 20)
time.sleep(2)
print()
time.sleep(.5)
show_each_letter(line4, .05)
print()
time.sleep(.5)
show_each_letter(line4a, .05)

