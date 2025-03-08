def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num  
    return tong

# Nhập danh sách các số từ người dùng
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# Gọi hàm và in kết quả
print("Tổng số chẵn trong danh sách là:", tinh_tong_so_chan(numbers))
