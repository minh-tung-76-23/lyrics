import time
import sys
from animation import * 

line01 = "🎤 Là vì ai?"
line02 = " Nỗi cô đơn này"
line02a = "\t\tlà vì ai?"
line03 = "Em nói anh nghe "
line03a = "anh làm gì sai?"
line04 = "Quá khứ kia   "
line04a = "\t\t  giờ nhạt phai"
line1 = "🎧 Một thằng ngu"
line2 = "Cuối cùng chỉ là một thằng ngu"
line3 = "Em đưa anh lên rồi đạp anh xuống"
line4 = "🎤 Đó có phải điều em mong muốn ?..."
line4a = "Đó"
line5 = "\t\t là anh phải đi khỏi đây          "
line6 = "Anh cũng chẳng thể giữ nữa"
line6a = " khi anh đã mỏi tay"
line6b = "              yeah                                 "
line7 = "Con tim giờ trống rỗng"
line7a = ", cố tỏ ra thờ ơ"
line8 = "Em bây giờ không giống ngày xưa nên"
line8a = "♭ I can't feel a love                "
line9 = "Cứ bước tiếp đi anh không níu đâu"
line9a = "Anh biết đau mà you know          "
line10 = "Sống như khi anh chưa gặp em "
line10a = "Như 2 ta chưa từng thiếu nhau"
line11 = "Chưa bao giờ anh chán em       "
line11a = "Đây đâu phải là ván game"
line12 = "   ♫ Câu yêu thương này quá quen"
line12a = "\t\t\t\t, em đoán xem?"
line13 = "Giờ lại ngồi ở trong phòng thu                  "
line13a = "♪ Và anh lại uống                                 "
line14 = "Dặn lòng phải giữ tỉnh táo"
line14a = "♪ Nhưng anh phải uống          "
line15 = "Bật bài nhạc em thích ngày xưa"
line15a = "♪ Cảm xúc lại tuôn                "
line16 = "Tự hỏi bản thân sao ngày đó"
line16a = "♯ Tay em lại buông 🩶           "

flash_line_fade_in_out_once(line01, 1.5)
show_each_letter(line02, 0.08)
fade_in_text(line02a, 0.08)
time.sleep(.5)

print()
fade_in_text(line03, 0.08)
show_each_letter(line03a, .08)
time.sleep(.5)
print()
show_fade_in_and_each_letter(line04, .08)
fade_in_text(line04a, 0.09)
flash_line_fade_in_out_once(line01, 1.8)
time.sleep(1)
print()
#thục thi
fade_in_text(line1, 0.08)
print()
time.sleep(.5)
show_each_letter(line2, 0.08)
time.sleep(.5)
flash_line_fade_in_out_once(line3, 3)
flash_line_fade_in_out_once(line4, 3)

fade_in_words(line4a, .01, 10)
show_fade_in_and_each_letter(line4, .06)
fade_in_and_move_from_right(50, line5, .02, 20)
time.sleep(.8)
fade_in_text(line6, 0.09) 
time.sleep(.3)
show_each_letter(line6a, 0.08)
flash_line_fade_in_out_once(line6b, .3)

time.sleep(.1)
fade_in_text(line7, 0.08)
time.sleep(.2)
show_each_letter(line7a, 0.05)
print()
show_each_letter(line8, .05)
fade_in_text(line8a, 0.08)
print()

time.sleep(.2)
fade_in_text(line9, 0.1)
time.sleep(.5)
flash_line_fade_in_out_once(line9a, 2)
print()

show_each_letter(line10, 0.02)
show_fade_in_and_each_letter(line10a, .04)
time.sleep(.4)

flash_line_fade_in_out_once(line11, 1.2)
flash_line_fade_in_out_once(line11a, 1.2)
show_fade_in_and_each_letter(line12, .05)
fade_in_text(line12a, 0.08)
time.sleep(.4)

show_fade_in_and_each_letter(line13, .04)
fade_in_text(line13a, 0.08)
time.sleep(.4)
print()
show_fade_in_and_each_letter(line14, .04)
time.sleep(.4)
fade_in_text(line14a, 0.08)
time.sleep(.4)

print()
show_fade_in_and_each_letter(line15, .04)
time.sleep(.4)
fade_in_text(line15a, 0.08)
time.sleep(.4)

print()
show_fade_in_and_each_letter(line16, .04)
time.sleep(.4)
flash_line_fade_in_out_once(line16a, 2)






