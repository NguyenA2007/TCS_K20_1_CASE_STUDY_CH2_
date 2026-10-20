# Nguyên trạng đoạn mã ban đầu gặp lỗi:
ma_may = input("Nhập mã máy: ")
cong_suat_w = input("Nhập công suất W: ")
so_phut = int(input("Nhập số phút: "))

# LỖI XẢY RA Ở DÒNG DƯỚI ĐÂY:
# cong_suat_w đang có kiểu 'str', không thể thực hiện phép nhân với số thực/
# nguyên trong công thức tính toán.
# Traceback: TypeError: unsupported operand type(s) for /: 'str' and 'int'
dien_nang_kwh = float(cong_suat_w) * so_phut / 60 / 1000  # Đã sửa lại float(cong_suat_w)

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# COMMENT GIẢI THÍCH LỖI THEO YÊU CẦU BÀI TẬP:
# Lỗi 1: Do chưa ép kiểu biến cong_suat_w từ str sang float/
# int nên phép tính toán số học bị hỏng (TypeError).
# Khắc phục: Đã sửa thành float(cong_suat_w) để đưa dữ liệu về đúng kiểu
#  số thực trước khi tính toán.