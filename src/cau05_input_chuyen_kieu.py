# 17. Dùng input() để nhận 4 giá trị và in type() ngay sau khi nhập
ma_may_str = input("Nhập mã máy: ")
print("Kiểu của ma_may vừa nhập:", type(ma_may_str))

cong_suat_str = input("Nhập công suất W: ")
print("Kiểu của cong_suat vừa nhập:", type(cong_suat_str))

so_phut_str = input("Nhập số phút sử dụng: ")
print("Kiểu của so_phut vừa nhập:", type(so_phut_str))

don_gia_str = input("Nhập đơn giá điện/kWh: ")
print("Kiểu của don_gia vừa nhập:", type(don_gia_str))

# 18. Chuyển kiểu dữ liệu theo yêu cầu
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# 19. Tính lại điện năng và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- KẾT QUẢ TÍNH TOÁN ---")
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí điện (VND):", chi_phi)