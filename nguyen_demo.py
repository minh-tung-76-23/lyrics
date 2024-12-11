import time
import sys
from animation import show_each_letter, show_fade_in_and_each_letter, fade_in_text, fade_in_and_move_from_right

line1 = "▶  Ngoài trời đã đổ cơn mưa"
line2 = "♪ Trong lòng em có ai chưa?"
line3 = "\t♬ Hay còn vấn vương kỉ niệm"
line4 = "\t♬ Về chuyện của tụi mình ngày xưa"
line5 = "Sao em lại làm như thế"
line6 = "Sao lại bước đi không về"
line7 = "Để mình anh với cơn đau"
line8 = "Phải tập làm quen"
line9 = "Những ngày không em"
line10 = "\tRồi sẽ ra sao..." 

# Thực thi
time.sleep(.5)  
show_fade_in_and_each_letter(line1, delay=0.07)  

time.sleep(.5)  
show_fade_in_and_each_letter(line2, delay=0.09)   
time.sleep(.8)  
fade_in_text(line3, 0.2)
print()  
time.sleep(.7)  
fade_in_text(line4, 0.3)
time.sleep(.8)   
print()  

fade_in_text(line5, delay=0.2)
time.sleep(.8)  
fade_in_text(line6, delay=0.25)
print()
time.sleep(.9)  
show_each_letter(line7, delay=0.06)
print()
time.sleep(.7)  
show_each_letter(line8, delay=0.06)
print()
time.sleep(.7)  
fade_in_and_move_from_right(20,line9, 0.08, 20)   
time.sleep(.8)  


if line10.endswith("..."):
    main_text = line10[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 
