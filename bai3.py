def tao_tuple_tu_list(lst):
    return tuple(lst)

# Nhập danh sách các số từ bàn phím, cách nhau bởi dấu phẩy
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

# Chuyển chuỗi nhập vào thành danh sách số nguyên
numbers = list(map(int, input_list.split(',')))

# Chuyển danh sách thành tuple
my_tuple = tao_tuple_tu_list(numbers)

# Hiển thị kết quả
print("Tuple được tạo:", my_tuple)
