# --- DỮ LIỆU ĐẦU VÀO (Mô phỏng bảng dữ liệu) ---
# Cấu trúc: [ID, Gender, Car Type, Shirt Size, Class]
dataset = [
    [1,  'M', 'Family', 'Small',       'C0'],
    [2,  'M', 'Sports', 'Medium',      'C0'],
    [3,  'M', 'Sports', 'Medium',      'C0'],
    [4,  'M', 'Sports', 'Large',       'C0'],
    [5,  'M', 'Sports', 'Extra Large', 'C0'],
    [6,  'M', 'Sports', 'Extra Large', 'C0'],
    [7,  'F', 'Sports', 'Small',       'C0'],
    [8,  'F', 'Sports', 'Small',       'C0'],
    [9,  'F', 'Sports', 'Medium',      'C0'],
    [10, 'F', 'Luxury', 'Large',       'C0'],
    [11, 'M', 'Family', 'Large',       'C1'],
    [12, 'M', 'Family', 'Extra Large', 'C1'],
    [13, 'M', 'Family', 'Medium',      'C1'],
    [14, 'M', 'Luxury', 'Extra Large', 'C1'],
    [15, 'F', 'Luxury', 'Small',       'C1'],
    [16, 'F', 'Luxury', 'Small',       'C1'],
    [17, 'F', 'Luxury', 'Medium',      'C1'],
    [18, 'F', 'Luxury', 'Medium',      'C1'],
    [19, 'F', 'Luxury', 'Medium',      'C1'],
    [20, 'F', 'Luxury', 'Large',       'C1']
]

# Chỉ số cột (để dễ gọi)
IDX_ID = 0
IDX_GENDER = 1
IDX_CAR = 2
IDX_SHIRT = 3
IDX_CLASS = 4

# --- HÀM TÍNH TOÁN ---

def get_gini_impurity(data_subset):
    """Tính Gini cho một nhóm dữ liệu cụ thể"""
    total_samples = len(data_subset)
    if total_samples == 0:
        return 0.0
    
    # Đếm số lượng C0 và C1
    count_c0 = 0
    count_c1 = 0
    for row in data_subset:
        if row[IDX_CLASS] == 'C0':
            count_c0 += 1
        elif row[IDX_CLASS] == 'C1':
            count_c1 += 1
            
    prob_c0 = count_c0 / total_samples
    prob_c1 = count_c1 / total_samples
    
    # Công thức: 1 - sum(p^2)
    gini = 1 - (prob_c0**2 + prob_c1**2)
    return gini

def get_weighted_gini(dataset, attribute_index):
    """Tính Gini có trọng số cho một thuộc tính (Multiway split)"""
    total_rows = len(dataset)
    
    # Tìm các giá trị duy nhất của thuộc tính (ví dụ: Family, Sports, Luxury)
    unique_values = set([row[attribute_index] for row in dataset])
    
    weighted_gini = 0.0
    print(f"\n--- Tính chi tiết cho cột số {attribute_index} ---")
    
    for val in unique_values:
        # Lọc ra các dòng có giá trị này
        subset = [row for row in dataset if row[attribute_index] == val]
        
        # Tính Gini của nhóm con
        gini_sub = get_gini_impurity(subset)
        
        # Tính trọng số
        weight = len(subset) / total_rows
        weighted_gini += weight * gini_sub
        
        print(f"   Giá trị '{val}': {len(subset)} mẫu -> Gini nhóm = {gini_sub:.4f}")
        
    return weighted_gini

# --- CHẠY CHƯƠNG TRÌNH ---

print("=== BẮT ĐẦU TÍNH TOÁN GINI ===")

# a) Overall Gini
gini_overall = get_gini_impurity(dataset)
print(f"\na) Gini index toàn bộ tập dữ liệu: {gini_overall:.4f}")

# b) Customer ID (Cột 0)
# Lưu ý: ID là unique nên Gini luôn = 0
gini_id = get_weighted_gini(dataset, IDX_ID)
print(f"b) Weighted Gini cho Customer ID: {gini_id:.4f}")

# c) Gender (Cột 1)
gini_gender = get_weighted_gini(dataset, IDX_GENDER)
print(f"c) Weighted Gini cho Gender: {gini_gender:.4f}")

# d) Car Type (Cột 2)
gini_car = get_weighted_gini(dataset, IDX_CAR)
print(f"d) Weighted Gini cho Car Type: {gini_car:.6f}") # Lấy 6 số lẻ để so sánh chính xác

# e) Shirt Size (Cột 3)
gini_shirt = get_weighted_gini(dataset, IDX_SHIRT)
print(f"e) Weighted Gini cho Shirt Size: {gini_shirt:.4f}")

# f) So sánh và kết luận
print("\n=== KẾT LUẬN (CÂU F) ===")
results = {
    'Gender': gini_gender,
    'Car Type': gini_car,
    'Shirt Size': gini_shirt
}

print("Kết quả so sánh:")
for name, score in results.items():
    print(f" - {name}: {score:.6f}")

best_attr = min(results, key=results.get)
print(f"\n-> Thuộc tính tốt nhất để phân lớp là: '{best_attr}' (vì có chỉ số Gini thấp nhất).")

# Dòng này để giữ màn hình không bị tắt ngay nếu chạy trực tiếp file .py
input("\nẤn Enter để thoát chương trình...")
