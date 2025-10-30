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

def change():
    y = 20  # đây là biến cục bộ mới, không thay đổi x toàn cục
    print("Trong hàm:", y)

change()
print("Ngoài hàm:", y)

'''Dùng từ khóa global để thay đổi biến toàn cục'''
z = 10

def change():
    global z
    z = 20 # change giá trị của Z
    print(f"Đây là giá trị của z trong hàm {z}")

change()
print(f'Đây là giá trị của z ngoài hàm {z}')

count = 0

def sum():
    global count
    count += 1
    print(f"Gía trị hiện tại {count}")
sum()
sum()
sum()

