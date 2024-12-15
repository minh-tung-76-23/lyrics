import time
import sys
# import threading  # Import thêm threading
from animation import *  # Giả sử bạn có các hiệu ứng như fade_in_text, show_each_letter, v.v.

# Danh sách các dòng để hiển thị
# line0 = "\t 🎼 Hanee "
line1 = "▶ Người con gái bất ngờ đến"
line2 = "\t♪ Với cuộc đời anh ba tháng rồi"
line3 = "♬ Không phải quá ngắn nhưng đủ thôi"
line4 = "\t♬ Để anh cảm nhận tim rộn ràng"
line5 = "Anh muốn tiến xa hơn trong"
line6 = "\t♪ Mối quan hệ này em biết không   "
line7 = "♬ Anh biết ơn em thật nhiều"
line8 = "\t♬ Vì cơ hội này ta yêu "
line9 = "\t▶ Với anh mỗi khoảnh khắc "
line9a = "\t\t\t\tc bên em thật quý giá"
line10 = "\t♪ Em là người đặc biệt"
line10a = "\t\t\t\t anh không muốn đánh mất đâu"
line11 = "\t♬ Phần còn lại cứ để anh     "
line12 = "\t♬ Anh sẽ lo lắng"
line12a = "\t\t\t và chăm chuốt"
line13 = "▶ Làm tất cả để bảo vệ"
line13a = "\t\t\ttình cảm"
line13b = "\t\t\t\t của chúng ta.."

# # Khởi động luồng riêng để nhấp nháy line0
# flashing_thread = threading.Thread(target=flash_line_fade_in_out_forever, args=(line0, 0.5))
# flashing_thread.daemon = True  # Dừng luồng khi chương trình kết thúc
# flashing_thread.start()

# Tạo khoảng trống cho các dòng khác để tránh bị đè lên bởi line0
# print("\n" * 2)  # Dòng trống giúp các dòng bên dưới không bị ghi đè

# Các dòng bài hát khác (không ảnh hưởng đến line0)
show_each_letter(line1, 0.09)
time.sleep(1.5)
print()

fade_in_text(line2, 0.3)
time.sleep(.5)
print()

show_each_letter(line3, 0.06)
time.sleep(1.5)
print()

fade_in_text(line4, 0.3)
time.sleep(1.)
print()

fade_in_text(line5, 0.3)
time.sleep(.5)
print()

fade_in_and_move_from_right(40, line6, .08, 30)
time.sleep(.5)

show_fade_in_and_each_letter(line7, .09)
time.sleep(1.4)
print()  

flash_line_fade_in_out_once(line8, 2)
time.sleep(.5)
print()

show_each_letter(line9, 0.08)
time.sleep(.2)
fade_in_text(line9a, 0.09)
time.sleep(.5)
print()

show_each_letter(line10, 0.05)
time.sleep(.7)
fade_in_text(line10a, 0.09)
time.sleep(.5)
print()

fade_in_and_move_from_right(35, line11, .05, 20)
time.sleep(.4)
show_fade_in_and_each_letter(line12, .09)
time.sleep(.4)
print()  
fade_in_text(line12a, 0.09)
print()
fade_in_and_move_from_right(35, line13, .05, 20)
show_each_letter(line13a, 0.07)
fade_in_text(line13b, 0.09)



