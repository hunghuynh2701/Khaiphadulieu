# Dữ liệu huấn luyện (Training Data) từ đề bài
# Mỗi hàng là một mẫu [Outlook, Temp, Humidity, Windy, Play]
dataset = [
    ['Sunny',    'Hot',  'High',   'False', 'No'],  # ID 1
    ['Sunny',    'Hot',  'High',   'True',  'No'],  # ID 2
    ['Overcast', 'Hot',  'High',   'False', 'Yes'], # ID 3
    ['Rainy',    'Mild', 'High',   'False', 'Yes'], # ID 4
    ['Rainy',    'Cool', 'Normal', 'False', 'Yes'], # ID 5
    ['Rainy',    'Cool', 'Normal', 'True',  'No'],  # ID 6
    ['Overcast', 'Cool', 'Normal', 'True',  'Yes'], # ID 7
    ['Sunny',    'Mild', 'High',   'False', 'No'],  # ID 8
    ['Sunny',    'Cool', 'Normal', 'False', 'Yes'], # ID 9
    ['Rainy',    'Mild', 'Normal', 'False', 'Yes'], # ID 10
    ['Sunny',    'Mild', 'Normal', 'True',  'Yes'], # ID 11
    ['Overcast', 'Mild', 'High',   'True',  'Yes'], # ID 12
    ['Overcast', 'Hot',  'Normal', 'False', 'Yes'], # ID 13
    ['Rainy',    'Mild', 'High',   'True',  'No']   # ID 14
]

# Dữ liệu cần dự đoán (ID 15)
# Outlook=Sunny, Temp=Cool, Humidity=High, Windy=True
test_instance = ['Sunny', 'Cool', 'High', 'True']

print("=== BẮT ĐẦU TÍNH TOÁN NAIVE BAYES ===")

# --- BƯỚC 1: TÍNH XÁC SUẤT TIÊN NGHIỆM P(Yes) và P(No) ---
total_samples = len(dataset)
count_yes = sum(1 for row in dataset if row[-1] == 'Yes')
count_no = sum(1 for row in dataset if row[-1] == 'No')

p_yes = count_yes / total_samples
p_no = count_no / total_samples

print(f"\n1. Xác suất tiên nghiệm:")
print(f"   P(Yes) = {count_yes}/{total_samples} = {p_yes:.4f}")
print(f"   P(No)  = {count_no}/{total_samples} = {p_no:.4f}")

# --- BƯỚC 2 & 3: TÍNH XÁC SUẤT THÀNH PHẦN VÀ KẾT QUẢ ---

# Hàm tính xác suất điều kiện: P(Feature = value | Class)
# Ví dụ: P(Outlook=Sunny | Yes)
def calculate_likelihood(feature_index, feature_value, target_class):
    # Đếm số mẫu thuộc target_class (Yes hoặc No)
    subset = [row for row in dataset if row[-1] == target_class]
    total_class_count = len(subset)
    
    # Đếm số mẫu trong tập con đó có giá trị feature trùng khớp
    count_feature = sum(1 for row in subset if row[feature_index] == feature_value)
    
    prob = count_feature / total_class_count
    return prob, count_feature, total_class_count

# Các tên cột để in ra cho đẹp
headers = ['Outlook', 'Temp', 'Humidity', 'Windy']

# Tính cho lớp YES
prob_X_given_Yes = 1.0
print(f"\n2. Tính cho lớp YES:")
for i in range(4):
    prob, count, total = calculate_likelihood(i, test_instance[i], 'Yes')
    print(f"   P({headers[i]}={test_instance[i]} | Yes) = {count}/{total} = {prob:.4f}")
    prob_X_given_Yes *= prob

score_yes = prob_X_given_Yes * p_yes
print(f"   => P(X|Yes) * P(Yes) = {prob_X_given_Yes:.4f} * {p_yes:.4f} = {score_yes:.6f}")

# Tính cho lớp NO
prob_X_given_No = 1.0
print(f"\n3. Tính cho lớp NO:")
for i in range(4):
    prob, count, total = calculate_likelihood(i, test_instance[i], 'No')
    print(f"   P({headers[i]}={test_instance[i]} | No) = {count}/{total} = {prob:.4f}")
    prob_X_given_No *= prob

score_no = prob_X_given_No * p_no
print(f"   => P(X|No) * P(No) = {prob_X_given_No:.4f} * {p_no:.4f} = {score_no:.6f}")

# --- BƯỚC 4: KẾT LUẬN ---
print("\n=== KẾT LUẬN ===")
print(f"Điểm số Yes: {score_yes:.6f}")
print(f"Điểm số No : {score_no:.6f}")

if score_no > score_yes:
    print(">>> DỰ ĐOÁN: Play = No")
else:
    print(">>> DỰ ĐOÁN: Play = Yes")
