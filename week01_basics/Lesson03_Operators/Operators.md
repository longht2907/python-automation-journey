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

