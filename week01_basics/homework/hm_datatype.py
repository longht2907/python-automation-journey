"""Khai báo 3 biến a, b, c lần lượt là int, float, complex. In kiểu dữ liệu của chúng"""
# a = 5
# b = 20.3
# c = 1 + 2j
# print(type(a))
# print(type(b))
# print(type(c))

"""Tính toán biểu thức: (5 + 3) * 2 / 3 và hiển thị kết quả dạng float """
# d = (5 + 3) * 2 / 3
# print(float(d))

"""Viết chương trình nhập chiều cao (m) và cân nặng (kg) → tính chỉ số BMI: bmi = weight / (height ** 2) """
try:
    # Nhập dữ liệu từ người dùng
    weight = float(input("Nhập cân nặng của bạn (kg): "))
    height = float(input("Nhập chiều cao của bạn (m): "))

    # Kiểm tra giá trị hợp lệ
    if weight <= 0 or height <= 0:
        print("⚠️ Cân nặng và chiều cao phải lớn hơn 0.")
    else:
        # Tính chỉ số BMI
        bmi = weight / (height ** 2)

        # In kết quả làm tròn 2 chữ số
        print(f"\n🔹 Chỉ số BMI của bạn là: {bmi:.2f}")

        # Phân loại theo tiêu chuẩn WHO
        if bmi < 18.5:
            print("➡️ Tình trạng: Gầy")
        elif bmi < 25:
            print("➡️ Tình trạng: Bình thường")
        elif bmi < 30:
            print("➡️ Tình trạng: Thừa cân")
        else:
            print("➡️ Tình trạng: Béo phì")

except ValueError:
    print("⚠️ Vui lòng nhập số hợp lệ cho cân nặng và chiều cao.")
