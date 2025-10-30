# **Tổng quan về Toán tử trong Python**

Toán tử (Operators) trong Python là **những ký hiệu đặc biệt dùng để thực hiện các phép tính hoặc thao tác trên biến và giá trị**.  
Mỗi toán tử đều có **ý nghĩa và độ ưu tiên riêng**, ảnh hưởng đến cách biểu thức được đánh giá.

## 🔹 1. Toán tử số học (Arithmetic Operators)

Toán tử số học dùng để thực hiện các phép tính cơ bản trên số học (bao gồm số nguyên int và số thực float).
Python hỗ trợ đầy đủ các phép toán phổ biến như cộng, trừ, nhân, chia, chia lấy dư, chia lấy nguyên và lũy thừa.

| Toán tử | Ý nghĩa | Ví dụ | Kết quả |
|----------|----------|--------|----------|
| `+` | Cộng | `5 + 2` | `7` |
| `-` | Trừ | `5 - 2` | `3` |
| `*` | Nhân | `5 * 2` | `10` |
| `/` | Chia (kết quả float) | `5 / 2` | `2.5` |
| `//` | Chia lấy phần nguyên | `5 // 2` | `2` |
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
---
