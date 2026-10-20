tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print("Số giờ:", so_gio, "giờ")
print("Số phút còn lại:", so_phut_du, "phút")

# 10. Tạo biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print("Sử dụng lâu (>60 phút):", su_dung_lau)

# 11. Tạo biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# 12. Kiểm chứng hai biểu thức toán học
bt1 = 100 + 20 * 3
bt2 = (100 + 20) * 3
print("Giá trị 100 + 20 * 3:", bt1)  
print("Giá trị (100 + 20) * 3:", bt2)  

# Du doan ket qua truoc khi chay:
# 100 + 20 * 3 = 160
# (100 + 20) * 3 = 360