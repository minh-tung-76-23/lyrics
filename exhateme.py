import time
import sys
from animation import * 

line1 = "🎙️   And it’s all because of me🩶"
line2 = "🎧 Cô ta nói là anh can đảm"
line3 = "Thì đến nơi đây chỉ tay     "
line4 = "\t Vào những vết thương mà anh than vãn"
line5 = "Có mỗi cô người yêu cũ"
line6 = "Mà hết năm này năm nọ kể hoài"
line7 = "Nhưng không bao giờ tôi nghe anh kể"
line8 = "\tVề đống đổ nát mà anh để lại        "
line9 = "Anh ngoài kia ánh đèn sân khấu"
line10 = "Đuổi theo một giấc mơ nung nấu"
line11 = "Từ khi còn bé thì tôi tự hỏi"
line12 = "Trong tâm trí anh tôi sẽ đựng đâu?"
line13 = "Dày vò thêm bao lâu"
line14 = "𝄫     Cho một con người thì nó sẽ đáng"
line15 = "Ước mơ của tôi là anh"
line16 = "\t♭ Nhưng anh đang mơ về một điều khác..."

show_fade_in_and_each_letter(line1, .05)
print()
time.sleep(0.5)
show_each_letter(line2, 0.04)
time.sleep(0.5)
fade_in_text(line3, 0.06)
print()
time.sleep(0.5)
show_each_letter(line4, 0.03)
print()
time.sleep(0.5)
show_each_letter(line5, 0.04)
time.sleep(0.2)
fade_in_text(line6, 0.07)
time.sleep(0.5)
print()
flash_line_fade_in_out_once(line7, 1)
flash_line_fade_in_out_once(line8, 1)

time.sleep(0.3)
show_each_letter(line9, 0.03)
time.sleep(0.5)
fade_in_text(line10, 0.07)
print()

time.sleep(0.5)
show_fade_in_and_each_letter(line11, .03)
print()
fade_in_and_move_from_right(40, line12, .05, 30)
time.sleep(0.5)

fade_in_text(line13, 0.07)
show_fade_in_and_each_letter(line14, .05)
print()

fade_in_text(line15, 0.07)
print()
if line16.endswith("..."):
    main_text = line16[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print() 










