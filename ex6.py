import math

# 1. Khởi tạo dữ liệu (Dạng danh sách các từ điển)
dataset = [
    {'id': 1, 'a1': 'T', 'a2': 'T', 'a3': 1.0, 'class': '+'},
    {'id': 2, 'a1': 'T', 'a2': 'T', 'a3': 6.0, 'class': '+'},
    {'id': 3, 'a1': 'T', 'a2': 'F', 'a3': 5.0, 'class': '-'},
    {'id': 4, 'a1': 'F', 'a2': 'F', 'a3': 4.0, 'class': '+'},
    {'id': 5, 'a1': 'F', 'a2': 'T', 'a3': 7.0, 'class': '-'},
    {'id': 6, 'a1': 'F', 'a2': 'T', 'a3': 3.0, 'class': '-'},
    {'id': 7, 'a1': 'F', 'a2': 'F', 'a3': 8.0, 'class': '-'},
    {'id': 8, 'a1': 'T', 'a2': 'F', 'a3': 7.0, 'class': '+'},
    {'id': 9, 'a1': 'F', 'a2': 'T', 'a3': 5.0, 'class': '-'},
]

# Hàm tính Entropy
def calculate_entropy(data):
    if not data:
        return 0
    
    total = len(data)
    # Đếm số lượng mỗi lớp (+ và -)
    counts = {}
    for row in data:
        label = row['class']
        counts[label] = counts.get(label, 0) + 1
        
    entropy = 0
    for label in counts:
        prob = counts[label] / total
        entropy -= prob * math.log2(prob)
        
    return entropy

# Hàm chia dữ liệu theo giá trị thuộc tính
def split_data(data, attribute):
    splits = {}
    for row in data:
        value = row[attribute]
        if value not in splits:
            splits[value] = []
        splits[value].append(row)
    return splits

# Hàm tính Information Gain
def calculate_info_gain(data, attribute):
    # Entropy toàn bộ tập S
    total_entropy = calculate_entropy(data)
    
    # Chia dữ liệu
    splits = split_data(data, attribute)
    total_samples = len(data)
    
    weighted_entropy = 0
    print(f"\n--- Chi tiết Entropy thuộc tính {attribute} ---")
    for value, subset in splits.items():
        subset_entropy = calculate_entropy(subset)
        weight = len(subset) / total_samples
        weighted_entropy += weight * subset_entropy
        print(f"  Giá trị '{value}': {len(subset)} mẫu, Entropy = {subset_entropy:.4f}")
        
    gain = total_entropy - weighted_entropy
    return gain

# Hàm tính Gini Index
def calculate_gini(data):
    if not data:
        return 0
    total = len(data)
    counts = {}
    for row in data:
        label = row['class']
        counts[label] = counts.get(label, 0) + 1
        
    impurity = 1
    for label in counts:
        prob = counts[label] / total
        impurity -= prob ** 2
    return impurity

# Hàm tính Gini Split (Weighted)
def calculate_gini_split(data, attribute):
    splits = split_data(data, attribute)
    total_samples = len(data)
    
    weighted_gini = 0
    print(f"\n--- Chi tiết Gini thuộc tính {attribute} ---")
    for value, subset in splits.items():
        subset_gini = calculate_gini(subset)
        weight = len(subset) / total_samples
        weighted_gini += weight * subset_gini
        print(f"  Giá trị '{value}': {len(subset)} mẫu, Gini = {subset_gini:.4f}")
        
    return weighted_gini

# --- CHẠY CHƯƠNG TRÌNH ---
print("=== CÂU A: TÍNH ENTROPY ===")
entropy_s = calculate_entropy(dataset)
print(f"Entropy(S) = {entropy_s:.4f}")

print("\n=== CÂU B: TÍNH INFORMATION GAIN ===")
gain_a1 = calculate_info_gain(dataset, 'a1')
print(f"-> Gain(S, a1) = {gain_a1:.4f}")

gain_a2 = calculate_info_gain(dataset, 'a2')
print(f"-> Gain(S, a2) = {gain_a2:.4f}")

print("\n=== CÂU F: TÍNH GINI INDEX SPLIT ===")
gini_a1 = calculate_gini_split(dataset, 'a1')
print(f"-> Weighted Gini(a1) = {gini_a1:.4f}")

gini_a2 = calculate_gini_split(dataset, 'a2')
print(f"-> Weighted Gini(a2) = {gini_a2:.4f}")

print("\n=== KẾT LUẬN CHO CÂU F ===")
if gini_a1 < gini_a2:
    print(f"Chọn thuộc tính a1 (Vì {gini_a1:.4f} < {gini_a2:.4f})")
else:
    print(f"Chọn thuộc tính a2 (Vì {gini_a2:.4f} < {gini_a1:.4f})")
