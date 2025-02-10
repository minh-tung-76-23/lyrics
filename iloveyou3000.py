import curses
import time
from animation import *

line1 = "But I want"
line1a = "\tnt it to"
line1b = "\t\t be out"
line1c = " of the blue"
line2 = "So make"
line2a = "\tsure"
line2b = " I have no clues"
line3 = "\tWhen you ask       "
line4 = "Baby"
line4a = ", take my hand"
line5 = "I want"
line5a = "you to be my husband"
line6 = "Cause you’re my Iron Man"
line7 = "And"
line7a = "\tI love you"
line7b = " three thousand🩶"
line8 = "Baby"
line8a = ", take a chance"
line9 = "‘Cause I want"
line9a = "this to be something’"
line10 = "Straight out of a Hollywood"
line10a = " movie..."

time.sleep(1)
show_fade_in_and_each_letter(line1, .04)
time.sleep(0.3)
fade_in_text(line1a, .09)
time.sleep(0.3)
fade_in_text(line1b, .09)
time.sleep(0.3)
show_each_letter(line1c, .07)

print()
time.sleep(0.5)
fade_in_words_non_del(line2, .01, 2)
time.sleep(.3)
fade_in_text(line2a, .09)
time.sleep(.3)
show_each_letter(line2b, .07)

print()
time.sleep(0.5)
fade_out_from_sides_left(line3, .15, 10)
time.sleep(.3)
fade_in_text(line4, .06)
time.sleep(0.2)
show_each_letter(line4a, .05)
print()
time.sleep(0.3)
fade_in_words_non_del(line5, .01, 2)
time.sleep(0.3)
show_each_letter(line5a, .06)

print()
time.sleep(0.8)
fade_in_from_sides(line6, .07, 20)
print()
time.sleep(0.2)
fade_in_text(line7, .02)
time.sleep(0.2)
fade_in_from_sides(line7a, .07, 20)
time.sleep(0.2)
show_each_letter(line7b, .05)

print()
time.sleep(0.5)
fade_in_text(line8, .06)
time.sleep(0.2)
show_each_letter(line8a, .05)

print()
time.sleep(0.3)
fade_in_words_non_del(line9, .01, 2)
time.sleep(0.2)
show_each_letter(line9a, .05)

print()
time.sleep(0.5)
fade_in_from_sides(line10, .09, 20)
time.sleep(0.5)
if line10a.endswith("..."):
    main_text = line10a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()







