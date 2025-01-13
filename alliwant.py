import time
import sys
from animation import * 

line1 = "🎙️  And I say"
line1a = "that I'm through"
line1b = "  But"
line1c = " this song's still"
line1d = "\t\t\tfor you🩶"
line2 = "🎧 All I want"
line2a = " is love that lasts"
line3 = "Is all I want"
line3a = " too much to ask?"
line4 = "Is it some"
line4a = "thing wrong with me?"
line51 = "          ●─ 💔  ─●"
line5 = "All I want"
line5a = " is a good guy"
line6 = "Are my expectations far too high?"
line7 = "    Try my best"
line7a = "\t\tbut what can I say?"
line8 = "All I have is myself"
line8a = "\t\tat the end"
line8b = " of the day"
line61 = "     ..."
line9 = "But shouldn't that be enough"
line9a = " for me?..."

time.sleep(0.4)
fade_in_text(line1, .04)
time.sleep(0.4)
show_each_letter(line1a, .06)
print()
time.sleep(0.2)
fade_in_text(line1b, .04)
time.sleep(0.4)
show_each_letter(line1c, .06)
time.sleep(0.4)
fade_in_text(line1d, .15)
print()

time.sleep(0.5)
random_flicker(line2, .2, 6)
time.sleep(0.3)
show_each_letter(line2a, .06)
print()

time.sleep(0.5)
random_flicker(line3, .2, 4)
time.sleep(0.3)
show_each_letter(line3a, .06)
print()

time.sleep(0.5)
color_splash_effect(line4, .15, 10)
time.sleep(0.3)
show_each_letter(line4a, .07)
print()
flash_line_fade_in_out_once(line51, 2)

time.sleep(0.5)
random_flicker(line5, .2, 4)
time.sleep(0.3)
show_each_letter(line5a, .09)
print()
time.sleep(0.5)
fade_in_from_sides(line6, 0.09, 10)
print()

time.sleep(2)
wave_text(line7, .03, 4)
time.sleep(0.3)
fade_in_text(line7a, .04)
print()

time.sleep(0.5)
fade_in_from_sides(line8, 0.07, 10)
print()
time.sleep(0.3)
fade_in_text(line8a, .02)
time.sleep(0.1)
show_each_letter(line8b, .09)
print()

if line61.endswith("..."):
    main_text = line61[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.8)

time.sleep(0.5)
show_fade_in_and_each_letter(line9, .07)
time.sleep(0.5)
if line9a.endswith("..."):
    main_text = line9a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 







