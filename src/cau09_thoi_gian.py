from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Phần bổ sung
bat_cau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_cau

print(thoi_luong)
print(type(thoi_luong))

# 24 & 25 (Giải thích trong comment):
# 24. Dự đoán kết quả phép trừ: 2 giờ 5 phút -> '1:50:00'.


# 25. Khác nhau giữa datetime, str và timedelta:
# - datetime: Đối tượng lưu trữ mốc thời gian cụ thể 
# (năm, tháng, ngày, giờ, phút, giây).
# - str: Chuỗi văn bản thuần túy được định dạng từ datetime để hiển thị hoặc lưu trữ.
# - timedelta: Đối tượng thể hiện khoảng thời gian (hiệu của 2 mốc datetime),
#  có thể dùng để cộng/trừ với datetime.