import math

# ==========================================
# 1. KHỞI TẠO DỮ LIỆU (Giống hệt hình ảnh)
# ==========================================
# Dữ liệu đầy đủ (20 dòng)
# Index dùng để đối chiếu: 0 đến 19
full_data = [
    # Class + (Indices 0-7)
    [4,3,'+'], [3,7,'+'], [7,4,'+'], [4,1,'+'], [6,5,'+'], [5,6,'+'], [3,7,'+'], [6,2,'+'],
    # Class - (Indices 8-19)
    [4,6,'-'], [4,4,'-'], [5,8,'-'], [7,8,'-'], [7,6,'-'], [4,10,'-'], [9,7,'-'], [5,4,'-'], [8,5,'-'], [6,6,'-'], [7,4,'-'], [8,8,'-']
]

# ==========================================
# 2. CHIA DATASET (HARD-CODE ĐỂ KHỚP BÁO CÁO)
# ==========================================
# Trong báo cáo tính tay, ta đã chọn 4 điểm sau làm Test:
# P7 (3,7,+), P8 (6,2,+), P19 (7,4,-), P20 (8,8,-)
# Tương ứng với index trong list trên là: 6, 7, 18, 19

test_indices = [6, 7, 18, 19]

train_set = []
test_set = []

for i in range(len(full_data)):
    if i in test_indices:
        test_set.append(full_data[i])
    else:
        train_set.append(full_data[i])

print(f"Tổng số mẫu: {len(full_data)}")
print(f"Số lượng Train: {len(train_set)} (80%)")
print(f"Số lượng Test: {len(test_set)} (20%)")
print("Các điểm Test (để đối chiếu):", test_set)
print("-" * 50)

# ==========================================
# 3. CÁC HÀM XỬ LÝ KNN
# ==========================================
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def get_prediction(train_data, test_point, k):
    distances = []
    # Tính khoảng cách từ điểm test đến tất cả điểm train
    for row in train_data:
        d = euclidean_dist(test_point, row)
        distances.append((d, row[2])) # Lưu (khoảng cách, nhãn)
    
    # Sắp xếp tăng dần theo khoảng cách
    distances.sort(key=lambda x: x[0])
    
    # Lấy k láng giềng
    k_neighbors = distances[:k]
    
    # Đếm phiếu
    count_plus = 0
    count_minus = 0
    for _, label in k_neighbors:
        if label == '+': count_plus += 1
        else: count_minus += 1
        
    # Quyết định nhãn
    if count_plus > count_minus: return '+'
    elif count_minus > count_plus: return '-'
    else: return k_neighbors[0][1] # Nếu hòa, chọn theo điểm gần nhất

# ==========================================
# 4. CHẠY CÂU A (Query Point 7,5)
# ==========================================
print("\n=== KẾT QUẢ CÂU A: ĐIỂM (7,5) ===")
query = [7, 5]
for k in [1, 3, 5, 9]:
    # Câu A dùng toàn bộ dữ liệu làm tập train
    pred = get_prediction(full_data, query, k)
    print(f"k={k}: Dự đoán Class {pred}")

# ==========================================
# 5. CHẠY CÂU B (ĐÁNH GIÁ 80/20)
# ==========================================
print("\n=== KẾT QUẢ CÂU B: ĐÁNH GIÁ TRÊN TẬP TEST ===")
for k in [1, 3, 5, 7, 9]:
    tp, tn, fp, fn = 0, 0, 0, 0
    correct = 0
    
    for row in test_set:
        point = [row[0], row[1]]
        actual = row[2]
        
        pred = get_prediction(train_set, point, k)
        
        if pred == actual: correct += 1
        
        # Tính Confusion Matrix
        if actual == '+' and pred == '+': tp += 1
        elif actual == '+' and pred == '-': fn += 1
        elif actual == '-' and pred == '+': fp += 1
        elif actual == '-' and pred == '-': tn += 1
            
    acc = (correct / len(test_set)) * 100
    
    print(f"\n[Với k={k}]")
    print(f"Độ chính xác: {acc}% ({correct}/{len(test_set)} đúng)")
    print(f"Confusion Matrix (Thực tế \\ Dự đoán):")
    print(f"      (+)   (-)")
    print(f"(+)   {tp}     {fn}")
    print(f"(-)   {fp}     {tn}")
