import time
import sys
from animation import *

line1 = "I know that dress is karma"  
line1a = "      perfume regret      "  
line2 = "You got me thinking about"  
line2a = "When you were mine"  
line1b = "     ●─  💔  ─●"
line3 = "And now I’m all up on ya"  
line3a = "    what you expect      "  
line4 = "But you’re not coming home"  
line4a = "with me tonight"  
line5 = "You just want"  
line5a = "attention"  
line6 = "You don’t want my 🩶"  
line7 = "Baby"  
line7a = " You just hate"  
line7b = " the thought"  
line7c = " of me with"  
line7d = " someone new"  
line8 = "Yeah"  
line8a = "You just want"  
line9 = "I knew from the start"  
line10 = "You’re just"  
line10a = "making sure"  
line10b = "I’m never"  
line10c= "\t getting"  
line10d = " over you💔..."  

time.sleep(.5)
show_fade_in_and_each_letter(line1, .06)
time.sleep(.5)
fade_in_from_sides(line1a, .09, 20)
time.sleep(.5)

fade_in_words_non_del(line2, .01, 2)
time.sleep(.2)
fade_in_and_move_from_right(40, line2a, .05, 20)
time.sleep(.5)
flash_line_fade_in_out_once(line1b, 1)
time.sleep(.5)

show_fade_in_and_each_letter(line3, .06)
time.sleep(.5)
fade_in_from_sides(line3a, .09, 20)
time.sleep(.5)

fade_in_words_non_del(line4, .01, 2)
time.sleep(.2)
print()
fade_in_and_move_from_right(40, line4a, .05, 20)
time.sleep(.5)

fade_in_words_non_del(line5, .01, 2)
time.sleep(.2)
show_each_letter(line5a, .06)
print()
time.sleep(.8)
fade_in_words_non_del(line6, .02, 4)

time.sleep(.5)
color_splash_effect(line7, .04, 10)
time.sleep(.1)
show_each_letter(line7a, .04)
time.sleep(.3)
show_each_letter(line7b, .05)
time.sleep(.3)
show_each_letter(line7c, .04)
time.sleep(.2)
show_each_letter(line7d, .05)

print()
time.sleep(.5)
fade_in_words_non_del(line8, .02, 4)
time.sleep(.2)
fade_in_words_non_del(line8a, .02, 4)
print()
time.sleep(.2)
fade_in_and_move_from_right(40, line5a, .05, 20)

time.sleep(.2)
fade_in_from_sides(line9, .09, 20)
print()
time.sleep(.3)
fade_in_words_non_del(line10, .01, 2)
time.sleep(.1)
show_each_letter(line10a, .04)
print()
time.sleep(.3)
fade_in_text(line10b, .05, 10)
fade_in_text(line10c, .04, 5)
time.sleep(.3)
if line10d.endswith("..."):
    main_text = line10d[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

















