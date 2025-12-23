# --- 1. KHỞI TẠO DỮ LIỆU (DATASET) ---
# Biểu diễn dữ liệu dưới dạng danh sách các từ điển để dễ hiểu
dataset = [
    {'A': 0, 'B': 0, 'C': 0, 'Class': '+'}, # 1
    {'A': 0, 'B': 0, 'C': 1, 'Class': '-'}, # 2
    {'A': 0, 'B': 1, 'C': 1, 'Class': '-'}, # 3
    {'A': 0, 'B': 1, 'C': 1, 'Class': '-'}, # 4
    {'A': 0, 'B': 0, 'C': 1, 'Class': '+'}, # 5
    {'A': 1, 'B': 0, 'C': 1, 'Class': '+'}, # 6
    {'A': 1, 'B': 0, 'C': 1, 'Class': '-'}, # 7
    {'A': 1, 'B': 0, 'C': 1, 'Class': '-'}, # 8
    {'A': 1, 'B': 1, 'C': 1, 'Class': '+'}, # 9
    {'A': 1, 'B': 0, 'C': 1, 'Class': '+'}  # 10
]

print(f"Tổng số mẫu dữ liệu: {len(dataset)}")

# --- CÂU A: TÍNH TOÁN XÁC SUẤT ---

# Hàm phụ trợ để đếm số lượng
def calculate_prob(feature_name, feature_val, class_label):
    count_feature_in_class = 0
    count_class = 0
    
    for row in dataset:
        if row['Class'] == class_label:
            count_class += 1
            if row[feature_name] == feature_val:
                count_feature_in_class += 1
                
    if count_class == 0: return 0
    return count_feature_in_class / count_class

# 1. Tính xác suất tiên nghiệm P(+) và P(-)
total = len(dataset)
count_plus = sum(1 for row in dataset if row['Class'] == '+')
count_minus = sum(1 for row in dataset if row['Class'] == '-')

p_plus = count_plus / total
p_minus = count_minus / total

# 2. Tính các xác suất có điều kiện cần thiết cho câu b
# Cần tính cho mẫu: A=0, B=1, C=0

# Với lớp (+)
p_a0_plus = calculate_prob('A', 0, '+')
p_b1_plus = calculate_prob('B', 1, '+')
p_c0_plus = calculate_prob('C', 0, '+')

# Với lớp (-)
p_a0_minus = calculate_prob('A', 0, '-')
p_b1_minus = calculate_prob('B', 1, '-')
p_c0_minus = calculate_prob('C', 0, '-')

print("\n--- KẾT QUẢ CÂU (A) ---")
print(f"P(+) = {p_plus}")
print(f"P(-) = {p_minus}")
print("-" * 20)
print(f"P(A=0 | +) = {p_a0_plus}")
print(f"P(B=1 | +) = {p_b1_plus}")
print(f"P(C=0 | +) = {p_c0_plus}")
print("-" * 20)
print(f"P(A=0 | -) = {p_a0_minus}")
print(f"P(B=1 | -) = {p_b1_minus}")
print(f"P(C=0 | -) = {p_c0_minus}")


# --- CÂU B: DỰ ĐOÁN MẪU MỚI ---
print("\n--- KẾT QUẢ CÂU (B) ---")
print("Dự đoán cho mẫu X: (A=0, B=1, C=0)")

# Công thức Naïve Bayes: P(Class) * P(A|Class) * P(B|Class) * P(C|Class)

# Tính điểm số cho lớp (+)
score_plus = p_plus * p_a0_plus * p_b1_plus * p_c0_plus
print(f"Score(+) = {p_plus} * {p_a0_plus} * {p_b1_plus} * {p_c0_plus} = {score_plus}")

# Tính điểm số cho lớp (-)
score_minus = p_minus * p_a0_minus * p_b1_minus * p_c0_minus
print(f"Score(-) = {p_minus} * {p_a0_minus} * {p_b1_minus} * {p_c0_minus} = {score_minus}")

# Kết luận
print("\n=> KẾT LUẬN:")
if score_plus > score_minus:
    print(f"Vì {score_plus} > {score_minus} nên nhãn dự đoán là: LỚP (+)")
else:
    print(f"Vì {score_minus} > {score_plus} nên nhãn dự đoán là: LỚP (-)")
