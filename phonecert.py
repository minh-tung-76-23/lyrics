import time
import sys
from animation import *

line1a = "Xin thông báo"
line1a1 = "Sau đây sẽ bắt đầu một đêm diễn"
line1 = "Tuyệt vời"  
line1b = "khi"  
line2 = "Người nghệ sĩ ấy có khách quý"  
line2a = "Là mình em thôi❤️  ..."  
line3 = "Chẳng một ai như anh"  
line3a = "Biết rõ gu nhạc em thích      "  
line3b = "tịch tình tang"  
line4 = "Một bài ca trên tông"  
line4a = "yêu đương"  
line4b = "Nhưng buồn miên man"  
line5 = "Ngày hôm ấy"  
line5a = "nếu em có nhớ"  
line5b = "Hãy vặn volume"  
line5c = "thật vừa tai"  
line6 = "Ngồi ngay ngắn"  
line6a = " lắng nghe anh hát"  
line6b = "Cho em một bài..."  
line7 = "Dù cho anh"  
line7a = "trông hơi nghiêm trọng"  
line8 = "Đừng cười anh"  
line8a = "Đừng có chê       "  
line9 = "Bình thường anh ngân nga rất mượt"  
line10 = "Sao hôm nay lại run như thế?"  
line11 = "Vì khi anh đang đứng trước mặt"  
line11a = "Người yêu thương"  
line11b = "đầy vấn vương"  
line12 = "Anh vẫn sai"  
line12a = "\tsai vẫn quên"  
line12b = "Vẫn vấp váp "  
line12c = "như thường..."  

fade_in_words_non_del(line1a, .01, 1)
print()
time.sleep(.3)
show_each_letter(line1a1, .05)
print()
time.sleep(.5)

fade_in_words_non_del(line1, .01, 5)
time.sleep(.3)
show_each_letter(line1b, .07)

print()
time.sleep(.5)
fade_in_from_sides(line2, .07, 10)
time.sleep(.5)
print()
fade_in_and_move_from_right(30, line2a, .07, 20)
time.sleep(2)
bounce_text(line3, .06, 10)
show_fade_in_and_each_letter(line3a, .04)
time.sleep(.5)
print()
fade_in_words_non_del(line3b, .02, 5)

print()
time.sleep(.5)
fade_in_words_non_del(line4, .01, 1)
time.sleep(.3)
show_each_letter(line4a, .05)
time.sleep(.3)
print()
fade_in_and_move_from_right(30, line4b, .05, 20)

time.sleep(1)
fade_in_words_non_del(line5, .01, 1)
show_each_letter(line5a, .05)
print()
time.sleep(.3)
fade_out_from_sides_left(line5b, .03, 10)
fade_in_words_non_del(line5c, .05, 5)
time.sleep(.5)
fade_in_from_sides(line6, .04, 10)
fade_in_and_move_from_right(30, line6a, .05, 20)
time.sleep(.3)
if line6b.endswith("..."):
    main_text = line6b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.4)
    print()
fade_in_words_non_del(line7, .01, 1)
show_each_letter(line7a, .04)

print()
time.sleep(.3)
bounce_text(line8, .05, 5)
fade_in_from_sides(line8a, .04, 10)
time.sleep(.8)
print()
fade_in_words_non_del(line9, .01, 1)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line10, .07)

print()
time.sleep(1)
fade_in_from_sides(line11, .04, 10)
time.sleep(.5)
print()
fade_in_words_non_del(line11a, .01, 1)
time.sleep(.5)
show_each_letter(line11b, .07)
print()
time.sleep(.5)
fade_in_words_non_del(line12, .01, 1)
time.sleep(.1)
fade_in_text(line12a, .03)
print()
time.sleep(.3)
fade_in_words_non_del(line12b, .01, 1)
time.sleep(.3)
if line12c.endswith("..."):
    main_text = line12c[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)
    print()
























