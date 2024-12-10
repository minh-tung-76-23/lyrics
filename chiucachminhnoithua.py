import time
import sys
from animation import show_each_letter, show_fade_in_and_each_letter, fade_in_text, fade_in_and_move_from_right

line1 = "▶ I told you that never leave me alone"
line2 = "♪ Trái tim anh giờ đau thế"
line3 = "♪ Nói buông nhưng mà đâu dễ"
line4 = "♪ Không còn cơ hội đâu bé, "
line4a = "\t\t\té, oh yeah"
line5 = "\t♫ Baby are you so bad?"
line6 = "\t♫ Kết cục vẫn vậy, đâu khác"
line7 = "\t♫ Thêm một bài nhạc so sad"
line8 = "𓏢 How I feel about love"
line8a = "\t\t\t, no cap"
line9 = "𝄞 Chứng kiến anh ra nông nỗi này liệu có phải"
line9a = "\t\t\t là điều em muốn thấy?"
line10 = "♮ Oh baby no no no"
line11 = "♮ Vứt hết kỷ niệm đằng sau"
line12 = "♮ Nếu như ta chẳng cần nhau"
line13 = "\t\t\tOh bae 🩶  ~"
line14 = "⏯ Lần này thì anh chịu thua em rồi"
line15 = "♩ Em bỏ anh đi ngay giữa đêm tối"
line16 = "𝄢 Từng giọt nước mắt anh chợt tuôn"
line17 = "𝄢 Một người nắm, một người buông"
line18 = "▶ I told you that never leave me alone"
line19 = "⏯ Lần này thì anh chịu thua em rồi"
line20 = "♪ Chẳng có cơ hội nào nữa em ơi"
line21 = "♫ Giá mà..."
line21a = "\t\t em cũng yêu"
line21b = "\t\t\t yêu anh nhiều"
line22 = "♫ I told you that never leave me alone..."

# Thực thi
time.sleep(.5)  
show_fade_in_and_each_letter(line1, delay=0.04)     
time.sleep(.2)  

fade_in_text(line2, 0.15)  
time.sleep(.3)  
fade_in_text(line3, 0.1)  
time.sleep(.7)  
fade_in_text(line4, 0.15)
time.sleep(.4)  
fade_in_text(line4a, 0.1)  
print()
time.sleep(.7) 

show_each_letter(line5, delay=0.06)
print()
time.sleep(.5)  
show_each_letter(line6, delay=0.06)
print()
time.sleep(.5)  
show_each_letter(line7, delay=0.06)
print()
time.sleep(.5)  
show_each_letter(line8, delay=0.06)
time.sleep(.5)  
fade_in_text(line8a, delay=0.08)
print()

time.sleep(1.5)  
show_fade_in_and_each_letter(line9, delay=0.06)  
time.sleep(.5)  
fade_in_text(line9a, delay=0.2)  
print()

time.sleep(.8) 
fade_in_text(line10, delay=0.09)   
time.sleep(.9)  
fade_in_text(line11, delay=0.09)  
time.sleep(.9)  
fade_in_text(line12, delay=0.15)
print() 
time.sleep(.9)  
show_fade_in_and_each_letter(line13, delay=0.09)  

time.sleep(1.5)  
fade_in_and_move_from_right(35,line14, 0.1, 20)      
time.sleep(1.5)  
fade_in_and_move_from_right(35,line15, 0.1, 20)   
time.sleep(2)  
fade_in_and_move_from_right(35,line16, 0.1, 20)   
time.sleep(.6)  
fade_in_and_move_from_right(35,line17, 0.08, 20)   
time.sleep(.6)  
fade_in_text(line18, delay=0.08)      
time.sleep(1.5)  
print() 

fade_in_and_move_from_right(35,line19, 0.1, 20)   
time.sleep(2)  
fade_in_and_move_from_right(35,line20, 0.2, 20)   
time.sleep(1)  
show_fade_in_and_each_letter(line21, delay=0.1)    
time.sleep(.6) 
show_each_letter(line21a, delay=0.09) 
time.sleep(.6) 
fade_in_text(line21b, delay=0.08)      
time.sleep(1) 
print()

if line22.endswith("..."):
    main_text = line22[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 
