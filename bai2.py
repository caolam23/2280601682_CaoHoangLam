def dao_nguoc_danh_sach(lst):
    lst.reverse()  # Phương thức reverse() sẽ đảo ngược danh sách tại chỗ
    return lst

# Nhập danh sách các số
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

# In kết quả
print("Danh sách sau khi đảo ngược là:", dao_nguoc_danh_sach(numbers))
