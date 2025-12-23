import math

def main():
    # --- 1. KHỞI TẠO DỮ LIỆU ---
    # Dữ liệu mẫu gồm: [Tên, Petal Length, Petal Width, Nhãn]
    dataset = [
        ["A", 1.4, 0.2, "Setosa"],
        ["B", 1.5, 0.2, "Setosa"],
        ["C", 4.5, 1.5, "Versicolor"],
        ["D", 4.7, 1.4, "Versicolor"],
        ["E", 5.1, 1.8, "Virginica"]
    ]

    # Điểm cần dự đoán X
    X = [4.6, 1.5]
    # Số láng giềng K
    K = 3

    print("=== KẾT QUẢ TÍNH TOÁN TỪ CHƯƠNG TRÌNH ===")
    print(f"Điểm cần dự đoán X: {X} | K = {K}")
    print("-" * 50)

    # --- BƯỚC 1: TÍNH KHOẢNG CÁCH ---
    distances = []
    print("BƯỚC 1: TÍNH KHOẢNG CÁCH")
    
    for point in dataset:
        name = point[0]
        val_x1 = point[1]
        val_x2 = point[2]
        label = point[3]
        
        # Công thức khoảng cách Euclidean
        dist_sq = (val_x1 - X[0])**2 + (val_x2 - X[1])**2
        dist = math.sqrt(dist_sq)
        
        # Lưu kết quả
        distances.append({"name": name, "dist": dist, "label": label})
        
        print(f"d(X, {name}) = {dist:.4f}")

    # --- BƯỚC 2: SẮP XẾP ---
    print("\nBƯỚC 2: XẾP HẠNG VÀ CHỌN 3 ĐIỂM GẦN NHẤT")
    distances.sort(key=lambda x: x["dist"]) # Sắp xếp tăng dần
    
    k_neighbors = distances[:K] # Lấy K phần tử đầu
    
    for i, item in enumerate(distances):
        chon = "(CHỌN)" if i < K else ""
        print(f"Hạng {i+1}: Điểm {item['name']} (kc={item['dist']:.4f}) -> {item['label']} {chon}")

    # --- BƯỚC 3: BẦU CHỌN ---
    print("\nBƯỚC 3: BẦU CHỌN")
    votes = {}
    for item in k_neighbors:
        label = item['label']
        votes[label] = votes.get(label, 0) + 1
            
    for label, count in votes.items():
        print(f"- Nhóm {label}: {count} phiếu")

    # --- KẾT LUẬN ---
    final_result = max(votes, key=votes.get)
    print("-" * 50)
    print(f"KẾT QUẢ CUỐI CÙNG: {final_result.upper()}")

if __name__ == "__main__":
    main()
