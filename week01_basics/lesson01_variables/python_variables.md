# Biến trong Python (Python Variables)

## 1. Khái niệm

Biến (variable) là tên dùng để lưu trữ dữ liệu trong bộ nhớ, giúp bạn tái sử dụng giá trị trong chương trình.

``` python
x = 10
name = "Long"
```
-   `x` là biến chứa số nguyên `10`
-   `name` là biến chứa chuỗi `"Long"`

## 2. Quy tắc đặt tên biến

- Gồm chữ cái (a-z, A-Z), số (0-9), dấu gạch dưới `_` 
- Khôngbắt đầu bằng số 
- Phân biệt chữ hoa và chữ thường - Không trùng với từkhóa của Python (`if`, `for`, `class`, ...)

📛 Không hợp lệ:

``` python
2name = "Long"   # ❌ bắt đầu bằng số
for = 10         # ❌ từ khóa
my-name = "abc"  # ❌ chứa dấu gạch ngang
```
Cách đặt tên nên dùng **snake_case**: `student_name`, `total_price`

## 3. Gán giá trị cho biến

``` python
x = 5
y = 3.14
name = "Long"
```


### Gán nhiều biến cùng lúc:

``` python
a, b, c = 1, 2, 3
```

### Gán nhiều biến cùng giá trị:

``` python
x = y = z = 0
```
## 4. Kiểu dữ liệu cơ bản của biến

  Kiểu dữ liệu   Ví dụ                                    Giải thích
  -------------- ---------------------------------------- --------------------
  `int`          `x = 10`                                 Số nguyên
  `float`        `pi = 3.14`                              Số thực
  `str`          `name = "Python"`                        Chuỗi ký tự
  `bool`         `is_active = True`                       Kiểu logic
  `list`         `nums = [1, 2, 3]`                       Danh sách
  `tuple`        `t = (1, 2, 3)`                          Bộ giá trị cố định
  `dict`         `person = {"name": "Long", "age": 25}`   Từ điển
  `set`          `s = {1, 2, 3}`                          Tập hợp

Xem kiểu dữ liệu bằng hàm `type()`:

``` python
x = 5
print(type(x))  # <class 'int'>
```
## 5. Biến động (Dynamic Typing)

Python là ngôn ngữ động, nên kiểu dữ liệu của biến có thể thay đổi trong lúc chạy.

``` python
x = 5
x = "Hello"
print(x)  # Hello
```

## 6. Biến toàn cục và biến cục bộ

Biến toàn cục (Global Variable) là biến được khai báo bên ngoài tất cả các hàm, có phạm vi truy cập toàn chương trình — nghĩa là bạn có thể dùng nó ở bất kỳ đâu (trong hoặc ngoài hàm).

Biến cục bộ (Local Variable) được khai báo bên trong hàm và chỉ tồn tại trong phạm vi hàm đó

``` python
x = 10  # Biến toàn cục

def demo():
    y = 5  # Biến cục bộ
    print("Trong hàm:", x, y)

demo()
print("Ngoài hàm:", x)
```

Dùng từ khóa `global` nếu muốn thay đổi biến toàn cục trong hàm:

``` python
x = 10

def change():
    global x
    x = 20

change()
print(x)  # 20
```
## 7. Tham chiếu và kiểu dữ liệu mutable/immutable

``` python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
```

👉 Cả `a` và `b` cùng trỏ đến một vùng nhớ.

Muốn sao chép độc lập:

``` python
b = a.copy()
```
## 8. So sánh danh tính và giá trị

``` python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (giá trị giống)
print(x is y)  # False (vị trí bộ nhớ khác)
```
## 9. Chuyển đổi kiểu dữ liệu (Type Casting)

``` python
x = "10"
y = int(x)   # "10" -> 10
z = float(x) # "10" -> 10.0
w = str(123) # 123 -> "123"
```

## 10. Một số hàm hữu ích

  Hàm           Mô tả
  ------------- -----------------------------------
  `type(var)`   Trả về kiểu dữ liệu
  `id(var)`     Địa chỉ vùng nhớ
  `globals()`   Tất cả biến toàn cục
  `locals()`    Biến cục bộ trong hàm
  `dir()`       Liệt kê thuộc tính và phương thức

