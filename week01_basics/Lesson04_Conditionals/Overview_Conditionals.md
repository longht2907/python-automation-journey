# Tổng Quan Kiến Thức Về Câu Điều Kiện Trong Python

## 1. Giới Thiệu Về Câu Điều Kiện

Câu điều kiện (conditional statements) cho phép chương trình của bạn đưa ra quyết định dựa trên các điều kiện khác nhau. Nó giúp bạn thực thi các khối mã khác nhau tùy theo điều kiện là đúng hay sai.

Câu điều kiện trong Python chủ yếu được xây dựng từ các từ khóa:
- **if** – kiểm tra một điều kiện.
elif – thêm các nhánh kiểm tra khác khi điều kiện trước đó không thỏa.
else – xử lý trường hợp “còn lại”, khi tất cả điều kiện đều không đúng.

---

## 2. Các Toán Tử So Sánh (Comparison Operators)

Trước khi học câu điều kiện, bạn cần hiểu các toán tử so sánh:

| Toán Tử | Ý Nghĩa | Ví Dụ |
|---------|---------|-------|
| `==` | Bằng | `5 == 5` → True |
| `!=` | Không bằng | `5 != 3` → True |
| `>` | Lớn hơn | `5 > 3` → True |
| `<` | Nhỏ hơn | `3 < 5` → True |
| `>=` | Lớn hơn hoặc bằng | `5 >= 5` → True |
| `<=` | Nhỏ hơn hoặc bằng | `3 <= 5` → True |

---

## 3. Câu Lệnh IF (If Statement)

### 3.1 Cấu Trúc Cơ Bản

```python
if điều_kiện:
    # Thực thi khối mã này nếu điều kiện đúng (True)
    print("Điều kiện đúng")
```

### 3.2 Ví Dụ Thực Tế

```python
tuoi = 18

if tuoi >= 18:
    print("Bạn đủ tuổi để lái xe")
```

**Kết quả:** `Bạn đủ tuổi để lái xe`

### 3.3 Lưu Ý Quan Trọng

- Dòng `if` phải kết thúc bằng dấu `:` (hai chấm)
- Khối mã bên trong `if` phải được **thụt đầu dòng** (indent) 4 khoảng trắng hoặc 1 tab
- Python sử dụng thụt đầu dòng để xác định khối mã, không phải dấu ngoặc nhọn `{}`

---

## 4. Câu Lệnh IF-ELSE

Dùng để thực thi một khối mã khi điều kiện đúng, và khối mã khác khi điều kiện sai.

### 4.1 Cấu Trúc

```python
if điều_kiện:
    # Thực thi nếu đúng
else:
    # Thực thi nếu sai
```

### 4.2 Ví Dụ

```python
tuoi = 15

if tuoi >= 18:
    print("Bạn đủ tuổi để lái xe")
else:
    print("Bạn chưa đủ tuổi để lái xe")
```

**Kết quả:** `Bạn chưa đủ tuổi để lái xe`

---

## 5. Câu Lệnh IF-ELIF-ELSE

Dùng khi bạn cần kiểm tra nhiều điều kiện.

### 5.1 Cấu Trúc

```python
if điều_kiện_1:
    # Thực thi nếu điều_kiện_1 đúng
elif điều_kiện_2:
    # Thực thi nếu điều_kiện_2 đúng
elif điều_kiện_3:
    # Thực thi nếu điều_kiện_3 đúng
else:
    # Thực thi nếu tất cả điều kiện trên đều sai
```

### 5.2 Ví Dụ

```python
diem = 75

if diem >= 90:
    print("Bạn nhận được A")
elif diem >= 80:
    print("Bạn nhận được B")
elif diem >= 70:
    print("Bạn nhận được C")
else:
    print("Bạn nhận được F")
```

**Kết quả:** `Bạn nhận được C`

### 5.3 Lưu Ý

- Bạn có thể có nhiều `elif` tùy thích
- Python dừng lại khi gặp điều kiện đầu tiên đúng (không kiểm tra các điều kiện sau)

---

## 6. Toán Tử Logic (Logical Operators)

Dùng để kết hợp nhiều điều kiện.

### 6.1 Toán Tử AND

```python
if điều_kiện_1 and điều_kiện_2:
    # Thực thi nếu CẢ HAI điều kiện đều đúng
```

**Ví dụ:**
```python
tuoi = 20
giay_phep = True

if tuoi >= 18 and giay_phep:
    print("Bạn có thể lái xe")
else:
    print("Bạn không thể lái xe")
```

**Kết quả:** `Bạn có thể lái xe`

### 6.2 Toán Tử OR

```python
if điều_kiện_1 or điều_kiện_2:
    # Thực thi nếu ÍT NHẤT MỘT trong hai điều kiện đúng
```

**Ví dụ:**
```python
nguon_sang = "den" 
gio = 18

if gio >= 18 or nguon_sang == "den":
    print("Bạn nên bật đèn")
```

**Kết quả:** `Bạn nên bật đèn`

### 6.3 Toán Tử NOT

```python
if not điều_kiện:
    # Thực thi nếu điều kiện SAI
```

**Ví dụ:**
```python
mua_xe = False

if not mua_xe:
    print("Bạn không mua xe")
```

**Kết quả:** `Bạn không mua xe`

---

## 7. Câu Điều Kiện Lồng Nhau (Nested If)

Bạn có thể đặt câu điều kiện bên trong câu điều kiện khác.

```python
tuoi = 20
co_bang_cap = True

if tuoi >= 18:
    print("Bạn đủ tuổi")
    if co_bang_cap:
        print("Bạn có thể xin việc")
    else:
        print("Bạn cần hoàn thành bằng cấp trước")
else:
    print("Bạn chưa đủ tuổi")
```

**Kết quả:**
```
Bạn đủ tuổi
Bạn có thể xin việc
```

---

## 8. Lệnh Ternary (Biểu Thức Điều Kiện Ngắn)

Cách viết câu điều kiện một dòng.

### 8.1 Cấu Trúc

```python
giá_trị_1 if điều_kiện else giá_trị_2
```

### 8.2 Ví Dụ

```python
tuoi = 20
trang_thai = "đủ tuổi" if tuoi >= 18 else "chưa đủ tuổi"
print(trang_thai)
```

**Kết quả:** `đủ tuổi`

---

## 9. Các Giá Trị Truthy và Falsy

Trong Python, bất kỳ giá trị nào cũng có thể được sử dụng như một điều kiện.

### 9.1 Giá Trị Falsy (được coi là False)

- `False`
- `0`, `0.0`
- Chuỗi rỗng `""`
- Danh sách rỗng `[]`
- Từ điển rỗng `{}`
- `None`

### 9.2 Giá Trị Truthy (được coi là True)

- `True`
- Bất kỳ số nào khác 0 (ví dụ: `1`, `-5`, `3.14`)
- Chuỗi không rỗng (ví dụ: `"hello"`)
- Danh sách không rỗng (ví dụ: `[1, 2, 3]`)

### 9.3 Ví Dụ

```python
# Kiểm tra chuỗi
ten = "Minh"
if ten:
    print(f"Xin chào {ten}")  # In ra: Xin chào Minh

# Kiểm tra số
so = 0
if so:
    print("Số không bằng 0")
else:
    print("Số bằng 0")  # In ra: Số bằng 0
```

---

## 10. Toán Tử IN (Kiểm Tra Phần Tử)

Dùng để kiểm tra xem một phần tử có nằm trong danh sách hay không.

```python
danh_sach = ["táo", "cam", "dâu"]

if "táo" in danh_sach:
    print("Táo có trong danh sách")

if "nho" not in danh_sach:
    print("Nho không có trong danh sách")
```

**Kết quả:**
```
Táo có trong danh sách
Nho không có trong danh sách
```

---

## 11. So Sánh Chuỗi (String Comparison)

```python
ten = "Minh"

if ten == "Minh":
    print("Tên là Minh")

if ten.lower() == "minh":  # Chuyển thành chữ thường
    print("Tên là Minh (không phân biệt hoa thường)")
```

---

## 12. Các Lỗi Thường Gặp

### 12.1 Quên Dấu Hai Chấm

```python
# ❌ SAI
if tuoi >= 18
    print("Đủ tuổi")

# ✓ ĐÚNG
if tuoi >= 18:
    print("Đủ tuổi")
```

### 12.2 Lỗi Thụt Đầu Dòng

```python
# ❌ SAI - không thụt đầu dòng
if tuoi >= 18:
print("Đủ tuổi")

# ✓ ĐÚNG
if tuoi >= 18:
    print("Đủ tuổi")
```

### 12.3 Sử Dụng = Thay Vì ==

```python
# ❌ SAI - = là gán giá trị, không so sánh
if tuoi = 18:
    print("Đủ tuổi")

# ✓ ĐÚNG
if tuoi == 18:
    print("Đủ tuổi")
```

---

## 13. Bài Tập Thực Hành

### Bài 1: Kiểm Tra Số Chẵn Lẻ

```python
so = 10

if so % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
```

### Bài 2: Tính Giá Khách Hàng

```python
so_tien = 1500000

if so_tien >= 1000000:
    giam_gia = so_tien * 0.15
    print(f"Giảm giá: {giam_gia}")
else:
    print("Không giảm giá")
```

### Bài 3: Phân Loại Tam Giác

```python
a, b, c = 3, 4, 5

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
```

---

## 14. Tóm Tắt Quy Trình Làm Việc

1. **Xác định điều kiện** cần kiểm tra
2. **Chọn cấu trúc phù hợp**: `if`, `if-else`, hay `if-elif-else`
3. **Viết điều kiện** sử dụng toán tử so sánh
4. **Viết khối mã** cần thực thi (không quên thụt đầu dòng)
5. **Kiểm tra logic** để đảm bảo chương trình hoạt động đúng

---

## 15. Tài Nguyên Học Tập Thêm

- Thực hành viết nhiều chương trình nhỏ
- Sử dụng debugger để theo dõi luồng chương trình
- Đọc mã của những người khác để học cách viết hiệu quả
- Tham gia các cộng đồng lập trình để hỏi đáp

