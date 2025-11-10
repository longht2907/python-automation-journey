# **Tổng quan về Toán tử trong Python**

Toán tử (Operators) trong Python là **những ký hiệu đặc biệt dùng để thực hiện các phép tính hoặc thao tác trên biến và giá trị**.  
Mỗi toán tử đều có **ý nghĩa và độ ưu tiên riêng**, ảnh hưởng đến cách biểu thức được đánh giá.

## 1. Toán tử số học (Arithmetic Operators)

Toán tử số học dùng để thực hiện các phép tính cơ bản trên số học (bao gồm số nguyên int và số thực float).
Python hỗ trợ đầy đủ các phép toán phổ biến như cộng, trừ, nhân, chia, chia lấy dư, chia lấy nguyên và lũy thừa.

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|----------|----------|--------|----------|
| `+` | Cộng | `5 + 2` | `7` |
| `-` | Trừ | `5 - 2` | `3` |
| `*` | Nhân | `5 * 2` | `10` |
| `/` | Chia (kết quả float) | `5 / 2` | `2.5` |
| `//` | Chia lấy phần nguyên | `5 // 2` | `2` | N = D * (N // D) + (N % D)
| `%` | Chia lấy dư | `5 % 2` | `1` |
| `**` | Lũy thừa | `5 ** 2` | `25` |

```python
a = 10
b = 3

print(a + b)   # 13
print(a / b)   # 3.3333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```
## 2. Toán tử gán (Assignment Operators)

Toán tử **gán** dùng để **lưu giá trị vào biến**.  
Ngoài phép gán cơ bản `=`, Python còn hỗ trợ **toán tử gán kết hợp**, giúp viết code **ngắn gọn và dễ hiểu hơn**.

| Toán tử | Mô tả | Tương đương với | Ví dụ | Kết quả |
|----------|--------|----------------|--------|----------|
| `=` | Gán giá trị | `x = 5` | `x = 5` | `x = 5` |
| `+=` | Cộng rồi gán | `x = x + 3` | `x += 3` | `x = 8` |
| `-=` | Trừ rồi gán | `x = x - 3` | `x -= 3` | `x = 2` |
| `*=` | Nhân rồi gán | `x = x * 3` | `x *= 3` | `x = 15` |
| `/=` | Chia rồi gán (float) | `x = x / 3` | `x /= 3` | `x = 1.666...` |
| `//=` | Chia nguyên rồi gán | `x = x // 3` | `x //= 3` | `x = 1` |
| `%=` | Lấy dư rồi gán | `x = x % 3` | `x %= 3` | `x = 2` |
| `**=` | Lũy thừa rồi gán | `x = x ** 3` | `x **= 3` | `x = 125` |
| `&=` | AND bit rồi gán | `x = x & 2` | `x &= 2` | - |
| `|=` | OR bit rồi gán | `x = x | 2` | `x |= 2` | - |
| `^=` | XOR bit rồi gán | `x = x ^ 2` | `x ^= 2` | - |
| `>>=` | Dịch phải rồi gán | `x = x >> 1` | `x >>= 1` | - |
| `<<=` | Dịch trái rồi gán | `x = x << 1` | `x <<= 1` | - |

-- Toán tử gán chuỗi (String Assignment) : Toán tử gán cũng áp dụng được với **chuỗi (string)**:

```python
name = "Python"
name += " 3.12"
print(name)  # Python 3.12
```
Gán nhiều giá trị cùng lúc

-- Python cho phép **gán nhiều biến cùng lúc** (đa gán – multiple assignment):

```python
a, b, c = 1, 2, 3
print(a, b, c)
```
-- Hoặc gán **cùng một giá trị** cho nhiều biến:

```python
x = y = z = 10
print(x, y, z)
```
-- Hoán đổi giá trị giữa hai biến : Python có cú pháp hoán đổi cực kỳ ngắn gọn — **không cần biến tạm**:

```python
a = 5
b = 10
a, b = b, a
print(a, b)
```
- `=` **luôn thực hiện gán từ phải sang trái**.  
  👉 Nghĩa là giá trị bên phải được tính trước rồi gán cho biến bên trái.  
- Các toán tử như `+=`, `-=`... **làm thay đổi giá trị của biến ban đầu**.


## 3. Toán tử So sánh trong Python

**Toán tử so sánh (Comparison Operators)** trong Python được dùng để **so sánh hai giá trị hoặc hai đối tượng**.  
Kết quả của phép so sánh **luôn là giá trị Boolean (`True` hoặc `False`)**.

**Danh sách các toán tử so sánh trong Python**

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|----------|----------|--------|----------|
| `==` | Bằng nhau | `3 == 3` | `True` |
| `!=` | Khác nhau | `3 != 2` | `True` |
| `>` | Lớn hơn | `5 > 2` | `True` |
| `<` | Nhỏ hơn | `3 < 1` | `False` |
| `>=` | Lớn hơn hoặc bằng | `3 >= 3` | `True` |
| `<=` | Nhỏ hơn hoặc bằng | `2 <= 5` | `True` |

### 3.1. So sánh chuỗi (String)

Python so sánh **theo thứ tự bảng mã Unicode (lexicographical order)**.

```python
'a' < 'b'    # True
'abc' < 'abd' # True
'abc' > 'Abc' # True
```
Dùng `.lower()` hoặc `.casefold()` để so sánh không phân biệt hoa thường.

### 3.2. So sánh số (int, float, complex)

```python
5 == 5.0     # True
5 < 5.1      # True
```
Không thể so sánh với số phức (`complex`) trừ khi bằng nhau.

### 3. So sánh chuỗi điều kiện (Chaining)

```python
x = 10
print(5 < x < 20)  # True
```
Tương đương với `(5 < x) and (x < 20)`.

### 4. So sánh đối tượng (Object)
Mặc định so sánh theo **vùng nhớ**, muốn so theo giá trị thì định nghĩa `__eq__`:
```python
class Server:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
```
### 5. So sánh List, Tuple, Dict
- List/Tuple so sánh từng phần tử.
```python
[1, 2, 3] < [1, 2, 4]  # True
```
- Dict chỉ hỗ trợ `==` và `!=`.

### 6. So sánh với None
Dùng `is` hoặc `is not`:
```python
if data is None:
    print("Chưa có dữ liệu")
```
### 7. So sánh Boolean và số
```python
True == 1   # True
False < 1   # True
```

### 8. Thứ tự ưu tiên toán tử
```
() → ** → * / // % → + - → < > <= >= == != → not → and → or
```
**Các lưu ý quan trọng**

### 1. So sánh kiểu khác nhau
```python
5 < "10"  # ❌ TypeError
5 < int("10")  # ✅
```

### 2. So sánh NaN
```python
import math
math.nan == math.nan   # False
```
Dùng `math.isnan(x)` để kiểm tra.

## Toán tử Logic trong Python

**Toán tử logic (Logical Operators)** trong Python được dùng để **kết hợp nhiều điều kiện boolean**.  
Kết quả trả về của mỗi biểu thức logic là **`True` hoặc `False`**.

***Các loại toán tử logic***

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|----------|----------|--------|----------|
| `and` | Cả hai điều kiện đều đúng | `True and True` | `True` |
| `or` | Một trong hai điều kiện đúng | `True or False` | `True` |
| `not` | Đảo ngược giá trị logic | `not True` | `False` |

***Cách hoạt động chi tiết***

### 1️⃣ Toán tử `and`
```python
cpu = 75
ram = 85
if cpu > 70 and ram > 80:
    print("⚠️ Tài nguyên cao!")
```
➡️ Cả hai điều kiện đúng → `True`.

**Short-circuit:** nếu vế trái `False`, Python không kiểm tra vế phải.
```python
print(0 and 5)   # 0
print(1 and 5)   # 5
```

### 2️⃣ Toán tử `or`
```python
disk_space = 10
network_ok = False
if disk_space < 20 or not network_ok:
    print("⚠️ Cảnh báo hệ thống.")
```
➡️ Chỉ cần **một điều kiện đúng** là đủ.

**Short-circuit:** nếu vế trái `True`, Python bỏ qua vế phải.
```python
print(0 or 5)   # 5
print(1 or 5)   # 1
```
### 3️⃣ Toán tử `not`
```python
server_active = False
if not server_active:
    print("🚫 Server đang tắt.")
```
➡️ `not False → True`.

**Kết hợp toán tử logic & so sánh**

```python
user_role = "admin"
login_status = True
if login_status and (user_role == "admin" or user_role == "root"):
    print("✅ Truy cập được cấp phép.")
```
**Thứ tự ưu tiên:**
```
1. not
2. and
3. or
```
```python
print(True or False and False)  # True
```
**Mẹo và kỹ thuật nâng cao**

### Dùng `or` để gán giá trị mặc định
```python
username = input("Tên: ") or "Guest"
```
### Dùng `and` để kiểm tra an toàn
```python
user = {"name": "Long", "age": 25}
print(user and user.get("name"))  # "Long"
```
### Lưu ý khi dùng `not`
`not` luôn trả về **Boolean**, không giống `and/or`.
```python
not "abc"  # False
```
### Kết hợp inline condition
```python
status = "OK" if cpu < 70 and ram < 80 else "WARNING"
```
**Lỗi và lưu ý thường gặp**

| Lỗi | Nguyên nhân | Cách xử lý |
|------|---------------|-------------|
| `TypeError` với object đặc biệt | Object không có giá trị boolean | Dùng `bool(obj)` |
| Hiểu sai thứ tự ưu tiên | `and` được xử lý trước `or` | Dùng ngoặc `()` |
| Biểu thức phức tạp | Dễ sai logic | Tách nhỏ điều kiện |


## Mức độ ưu tiên toán tử (Operator Precedence) trong Python

**Mức độ ưu tiên (Precedence)** xác định **thứ tự mà Python thực hiện các toán tử** trong một biểu thức.  
Khi có nhiều phép toán, Python sẽ xử lý theo **thứ tự ưu tiên từ cao đến thấp**.

Ví dụ:
```python
x = 10 + 3 * 2
print(x)  # 16, vì * thực hiện trước +
```
**Quy tắc thực thi**
1. Toán tử có **độ ưu tiên cao hơn** được thực hiện trước.
2. Nếu có **cùng độ ưu tiên**, thực hiện **từ trái sang phải** (trừ `**`).
3. **Dấu ngoặc `()`** luôn được ưu tiên cao nhất.

**Bảng thứ tự ưu tiên (cao → thấp)**

| Thứ tự | Toán tử | Ví dụ | Ghi chú |
|--------|----------|--------|----------|
| 1️⃣ | `()` | `(a + b) * c` | Dấu ngoặc – luôn xử lý đầu tiên |
| 2️⃣ | `**` | `2 ** 3` | Lũy thừa, thực hiện **phải sang trái** |
| 3️⃣ | `+x`, `-x`, `~x` | `-5`, `~x` | Toán tử đơn ngôi |
| 4️⃣ | `*`, `/`, `//`, `%` | `a * b / c` | Nhân, chia, chia nguyên, chia dư |
| 5️⃣ | `+`, `-` | `a + b - c` | Cộng, trừ |
| 6️⃣ | `<<`, `>>` | `a << 1` | Dịch bit trái/phải |
| 7️⃣ | `&` | `a & b` | Bitwise AND |
| 8️⃣ | `^`, `|` | `a ^ b`, `a | b` | XOR, OR |
| 9️⃣ | `<`, `<=`, `>`, `>=`, `==`, `!=` | `a > b`, `x == y` | So sánh |
| 🔟 | `is`, `is not`, `in`, `not in` | `x in list`, `a is b` | Thành viên, định danh |
| 11️⃣ | `not` | `not x` | Logic NOT |
| 12️⃣ | `and` | `x and y` | Logic AND |
| 13️⃣ | `or` | `x or y` | Logic OR |
| 14️⃣ | `=`, `+=`, `-=` ... | `x += 1` | Toán tử gán – thực hiện sau cùng |

```python
a = True
b = False
c = True

print(a or b and c)     # True (vì b and c được thực hiện trước)
print((a or b) and c)   # True
print(a or (b and c))   # True
```
`not` có độ ưu tiên cao hơn `and`
```python
a = True
b = False
print(not a and b)  # False → (not a) → False → False and b → False
```
`**` ưu tiên hơn `*` và `/`
```python
print(2 * 3 ** 2)   # 18 → (3**2)=9 → 2*9=18
print((2 * 3) ** 2) # 36 → ép ưu tiên bằng ngoặc
```
Toán tử gán có độ ưu tiên thấp nhất
```python
x = 5
y = 10
z = x + y * 2  # Nhân trước, cộng sau → 25
```
**Mẹo ghi nhớ**

> **“Ngoặc – Lũy thừa – Dấu – Nhân chia – Cộng trừ – So sánh – Logic – Gán”**

Tóm gọn:
```
() → ** → * / // % → + - → < > <= >= == != → not → and → or → =
```
**Kỹ thuật Pythonic tránh lỗi logic**

### Dùng ngoặc khi có nghi ngờ
```python
result = (a > b) and (b < c)
```

### Tránh biểu thức quá dài
Thay vì:
```python
if not a and b or c:
```
Nên:
```python
if (not a and b) or c:
```

### Dùng module `operator` cho rõ ràng
```python
import operator
print(operator.add(3, 5))  # 8
print(operator.and_(True, False))  # False
```

