import time
import sys
from animation import *

# Các dòng cần hiển thị
line1 = "▶ Tiếng "
line1a = "▶ Tiếng vỡ "
line1b = "▶ Tiếng vỡ tan "
line1c = "▶ Tiếng vỡ tan cơn "
line1d = "▶ Tiếng vỡ tan cơn mê "
line1e = "▶ Tiếng vỡ tan cơn mê màng"
line2 = " ♪ Đánh thức nơi thiên đàng anh mơ "
line2a = "\t\t\t\tmơ"
line2b = "\t\t\t\t    mơ"
line2c = "\t\t\t\t       mơ"
line2e = "\t\t\t\tmơ           "
line3 = "♬ Nơi thiên đàng anh mơ"
line3a = "\t\t\t mơ"
line3b = "\t\t\t mơ mơ"
line3c = "\t\t\t mơ mơ mơ"
line3d = "\t\t\t mơ mơ mơ mơ"
line3e = "\t\t\t            "
line4 = "\t♬ Nơi có em là yên bình,"
line4a = "\t\t\t\t anh mãi như thằng si tình"
line5 = "▶ Dù đôi chân anh đi mòn lối "
line5a = "vẫn mãi không về nơi em..."

# Thực thi
time.sleep(.5)
print()  
print()  
print()  
fade_in_text(line1, 0.015)
fade_in_text(line1a, 0.015)
fade_in_text(line1b, 0.015)
fade_in_text(line1c, 0.015)
fade_in_text(line1d, 0.015)
fade_in_text(line1e, 0.001)
print()

time.sleep(.2)  
show_each_letter(line2, delay=0.05)
fade_in_text(line2a, 0.06)
fade_in_text(line2b, 0.06)
fade_in_text(line2c, 0.06)
fade_in_text(line2e, 0.06)
print()

show_each_letter(line3, delay=0.04)
fade_in_text(line3a, 0.05)
fade_in_text(line3b, 0.05)
fade_in_text(line3c, 0.05)
fade_in_text(line3d, 0.05)
fade_in_text(line3e, 0.001)
print()

time.sleep(.4)
show_each_letter(line4, 0.05)
time.sleep(.4)
fade_in_text(line4a, 0.09)
print()

time.sleep(.6)
fade_in_text(line5, 0.15)
time.sleep(.5)

if line5a.endswith("..."):
    main_text = line5a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 