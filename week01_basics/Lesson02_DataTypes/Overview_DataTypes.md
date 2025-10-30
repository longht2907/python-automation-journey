# Tổng quan về Kiểu Dữ Liệu trong Python

## I. Khái niệm
- **Kiểu dữ liệu (Data Type)** là cách Python phân loại giá trị để xác định cách **lưu trữ và xử lý** chúng.
- Python là ngôn ngữ **động (dynamic typing)** → không cần khai báo kiểu khi tạo biến.

```python
a = 10          # int
b = 3.14        # float
c = "Python"    # str
d = True        # bool
```
---

## II. Phân loại kiểu dữ liệu trong Python

| Nhóm | Kiểu dữ liệu | Mô tả |
|------|---------------|-------|
| **Cơ bản** | `int`, `float`, `complex`, `bool`, `str` | Kiểu dữ liệu nguyên thủy |
| **Chuỗi (Text)** | `str` | Đại diện cho chuỗi ký tự |
| **Dãy (Sequence)** | `list`, `tuple`, `range` | Tập hợp có thứ tự |
| **Tập hợp (Set)** | `set`, `frozenset` | Tập hợp **không trùng lặp, không thứ tự** |
| **Ánh xạ (Mapping)** | `dict` | Cặp **khóa – giá trị** |
| **Nhị phân (Binary)** | `bytes`, `bytearray`, `memoryview` | Dữ liệu nhị phân |
| **Đặc biệt** | `NoneType` | Giá trị rỗng (None) |
---

## III. Kiểm tra kiểu dữ liệu

```python
x = [1, 2, 3]
print(type(x))          # <class 'list'>
print(isinstance(x, list))  # True
```
## IV. Nhóm kiểu dữ liệu cơ bản

### 1. Numeric types (Số học)

- **int** : số nguyên, là một số nguyên dương hoặc âm, không có phần thập phân, có độ dài không giới hạn.
- **float** : Số thực,là một số, dương hoặc âm, chứa một hoặc nhiều số thập phân.
             Khi chia hai số nguyên, kết quả luôn là float || print(5 / 2)  # 2.5
             Muốn lấy phần nguyên khi chia || print(5 // 2)  # 2
- **complex** : Kiểu số phức
```python
a = 10          # int: số nguyên
b = 3.14        # float: số thực
c = 2 + 3j      # complex: số phức
```

### 2. Boolean (True / False)
```python
is_python_fun = True
print(is_python_fun)  # True
```

### 3. String (Chuỗi ký tự)
```python
s = "Hello Python"
print(s[0])       # H
print(len(s))     # 12
print(s.lower())  # hello python
```
---

## V. Kiểu dữ liệu có cấu trúc (Collections)

| Kiểu | Có thứ tự | Thay đổi được | Trùng lặp | Cú pháp |
|------|------------|----------------|------------|----------|
| `list` | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| `tuple` | ✅ | ❌ | ✅ | `(1, 2, 3)` |
| `set` | ❌ | ✅ | ❌ | `{1, 2, 3}` |
| `dict` | ✅ | ✅ | ❌ (key) | `{"a": 1, "b": 2}` |
---

## VI. Mutable vs Immutable

| Loại | Kiểu dữ liệu | Đặc điểm |
|------|---------------|-----------|
| **Immutable** | `int`, `float`, `str`, `tuple`, `bool` | Không thể thay đổi giá trị sau khi tạo |
| **Mutable** | `list`, `set`, `dict` | Có thể thay đổi nội dung |

**Ví dụ:**
```python
x = [1, 2, 3]      # list: mutable
x.append(4)
print(x)           # [1, 2, 3, 4]

y = "Python"       # str: immutable
y.replace("P", "C")
print(y)           # Python (không thay đổi)
```
---

## VII. Chuyển đổi kiểu dữ liệu (Type Casting)
```python
a = 5
print(float(a))    # 5.0

b = "10"
print(int(b))      # 10

c = [1, 2, 3]
print(tuple(c))    # (1, 2, 3)
```
---

## VIII. Tổng kết

| Nhóm | Kiểu dữ liệu | Ghi nhớ nhanh |
|------|---------------|----------------|
| Cơ bản | `int`, `float`, `bool`, `str` | Dữ liệu nguyên thủy |
| Cấu trúc | `list`, `tuple`, `set`, `dict` | Rất quan trọng cho lập trình thực tế |
| Đặc biệt | `NoneType`, `bytes` | Dùng trong API, file, nhị phân |
---

## IX. Bài tập thực hành
1. Tạo biến và kiểm tra kiểu dữ liệu của chúng bằng `type()`.
2. Chuyển đổi giữa `int`, `float`, `str`.
3. Tạo danh sách (`list`) các số, chuyển sang `tuple`, và ngược lại.
4. So sánh sự khác nhau giữa `set` và `list` khi thêm phần tử trùng.
---

## X. Hướng học tiếp theo
- **Buổi 1-2:** Ôn kiểu cơ bản (`int`, `float`, `str`, `bool`)
- **Buổi 3-4:** Học sâu **List, Tuple**
- **Buổi 5-6:** Tìm hiểu **Set, Dictionary**
- **Buổi 7:** Bài tập tổng hợp
