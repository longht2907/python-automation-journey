city = "Hồ Chí Minh"
year = 2025
is_learning_python = True

print(f"Tôi đang sống ở {city}" )
print("Tôi đang sống ở", city)
print(f"Năm nay là {year} ")
print(f"Tôi đang học python: {is_learning_python}")

'''Global Variable
'''
x = 10
def display():
    print("Gía trị trong hàm:", x)

display()
print("Gía trị ngoài hàm", x)


'''Sự khác biệt khi thay đổi biến toàn cục trong hàm
Nếu bạn chỉ đọc giá trị của biến toàn cục trong hàm → Python cho phép.
Nhưng nếu bạn thay đổi giá trị của nó → Python sẽ tạo ra một biến cục bộ mới trùng tên, trừ khi bạn dùng từ khóa global.'''

y = 10

# def change():
#     y = 20 đây là biến cục bộ mới, không thay đổi y toàn cục
#     print(f"Trong hàm {y}")
# change()