from datetime import datetime

# Nhập dữ liệu
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = float(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

# Tính toán
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60  # Giá trị Boolean không dùng if

# Lấy thời điểm hiện tại
thoi_diem_hien_tai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Xuất kết quả sử dụng f-string
print("\n--- BÁO CÁO SỬ DỤNG PHÒNG LAB ---")
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_hien_tai}")