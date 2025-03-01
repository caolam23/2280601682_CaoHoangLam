# Tạo danh sách rỗng
danh_sach = []

# Duyệt qua các số trong đoạn từ 2000 đến 3200
for i in range(2000, 3201):  # 3201 để bao gồm 3200
    if i % 7 == 0 and i % 5 != 0:  # Kiểm tra chia hết cho 7 và không phải bội số của 5
        danh_sach.append(i)

# In danh sách kết quả
print(danh_sach)
