def dem_so_lan_xuat_hien(lst):
    count_dict = {}  
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1  # Nếu từ đã tồn tại, tăng số lần xuất hiện
        else:
            count_dict[item] = 1  # Nếu từ chưa có, gán giá trị ban đầu là 1
    return count_dict

# Nhập danh sách từ người dùng
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")

# Tách các từ thành danh sách
word_list = input_string.split()

# Sử dụng hàm và in kết quả
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử:", so_lan_xuat_hien)
