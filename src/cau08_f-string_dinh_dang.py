ma_may = "PC12"
cong_suat_w = 250
dien_nang_kwh = 0.375
chi_phi = 1125

# Sử dụng f-string định dạng đầu ra theo đúng mẫu
output = f"""Máy: {ma_may}
Công suất: {cong_suat_w:.2f} W
Điện năng: {dien_nang_kwh:.3f} kWh
Chi phí: {chi_phi:.2f} VND"""

print(output)