cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính điện năng tiêu thụ (kWh) và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In cả giá trị và kiểu dữ liệu của hai kết quả
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

# 15. Du doan ket qua truoc khi chay: 
# cong_suat_w = 250
# so_phut = 90
# don_gia_kwh = 3000
# => 250 * 90/60/1000 = 0.375kwh
# => chi_phi = 0.375 * 3000 = 1125.0VND

# Khi  so_phut = 60
# => 250 * 60/60/1000 = 0.25kwh
# => chi_phi = 0.25 * 3000 = 750.0VND

# 16. Thay so_phut = 60 và tính lại
so_phut = 60
dien_nang_kwh_60 = cong_suat_w * so_phut / 60 / 1000
chi_phi_60 = dien_nang_kwh_60 * don_gia_kwh
print("\n--- Sau khi thay so_phut = 60 ---")
print("Điện năng mới (kWh):", dien_nang_kwh_60)
print("Chi phí mới (VND):", chi_phi_60)