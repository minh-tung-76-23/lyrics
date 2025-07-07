import time
import sys
from animation import *

line1 = "Don’t wanna know"  
line2 = "What kind of dress you’re wearing tonight"  
line3 = "   If he’s holding onto you so tight      "  
line4 = "The way I did before 💔"  
line5 = "I overdosed"  
line6 = "Should’ve known your love was a game"  
line7 = "Now I can’t get you out of"  
line7a = "my brain"  
line8 = "Oh, it’s such a shame"  
line9 = "That"  
line9a = "We don’t talk anymore"  
line10 = "Like"  
line10a = "we used to do"  
line11 = "We don’t laugh anymore"  
line12 = "What was all "  
line12a = "of it for?"  
line13 = "     Oh🩶  "  
line14 = "..."  

# Create a new animation object
fade_in_text(line1, .055, 10)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line2, .045)
time.sleep(1)
fade_out_from_sides_left(line3, .09, 30)
time.sleep(.5)
fade_in_from_sides(line4, .05, 10)
print()
time.sleep(.5)

fade_out_by_char(line5, .08, 20)
time.sleep(.5)
show_fade_in_and_each_letter(line6, .06)
print()
time.sleep(.5)
fade_in_words_non_del(line7, .01, 1)
time.sleep(.2)
show_each_letter(line7a, .05)
print()
time.sleep(.5)

flash_line_fade_in_out_once(line8, 1)
time.sleep(.5)
fade_in_words_non_del(line9, .01, 1)
fade_in_words_non_del(line9a, .05, 2)
print()
time.sleep(1)
fade_out_with_color(line9a, .05, 25)
time.sleep(1.5 )
fade_out_from_sides_left(line9a, .05, 20)
time.sleep(.2)
fade_in_words_non_del(line10, .05, 1)
time.sleep(.5)
show_each_letter(line10a, .08)
print()
time.sleep(1.5)

fade_in_text(line11, .08, 10)
time.sleep(1.5)
print()
fade_in_words_non_del(line12, .02, 1)
show_each_letter(line12a, .05)
print()
flash_line_fade_in_out_once(line13, .5)
time.sleep(.5)
show_fade_in_and_each_letter(line9a, .06)
print()
time.sleep(.2)
fade_in_words_non_del(line10, .05, 1)
time.sleep(.5)
show_each_letter(line10a, .06)
if line14.endswith("..."):
    main_text = line14[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)














