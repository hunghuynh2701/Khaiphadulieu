# CHƯƠNG TRÌNH PHÂN LOẠI KNN 1 CHIỀU
# -----------------------------------

def knn_manual_code():
    # 1. KHỞI TẠO DỮ LIỆU
    # Dữ liệu X và nhãn Y tương ứng từ đề bài
    X = [0.5, 3.0, 4.5, 4.6, 4.9, 5.2, 5.3, 5.5, 7.0, 9.5]
    Y = ['-', '-', '+', '+', '+', '-', '-', '+', '-', '-']
    
    # Điểm cần dự đoán
    z = 5.0
    
    # Các giá trị K cần xét
    k_list = [1, 3, 5, 9]

    print(f"Dữ liệu đầu vào X: {X}")
    print(f"Nhãn tương ứng Y : {Y}")
    print(f"Điểm cần phân loại z: {z}")
    print("=" * 60)

    # 2. TÍNH KHOẢNG CÁCH
    # Tạo danh sách chứa các bộ (khoảng cách, nhãn, giá trị x)
    distances = []
    for i in range(len(X)):
        # Công thức khoảng cách Euclidean 1 chiều: |x - z|
        d = abs(X[i] - z) 
        distances.append((d, Y[i], X[i]))

    # 3. SẮP XẾP TĂNG DẦN THEO KHOẢNG CÁCH
    # Sắp xếp dựa trên phần tử đầu tiên của bộ (là khoảng cách d)
    distances.sort(key=lambda x: x[0])
    
    # In bảng khoảng cách đã sắp xếp để kiểm tra
    print("Bảng khoảng cách sau khi sắp xếp:")
    print(f"{'Khoảng cách':<12} | {'Giá trị x':<10} | {'Nhãn':<5}")
    print("-" * 35)
    for d, label, x_val in distances:
        print(f"{d:<12.1f} | {x_val:<10} | {label:<5}")
    print("=" * 60)

    # 4. XÉT CÁC TRƯỜNG HỢP K VÀ RA QUYẾT ĐỊNH
    for k in k_list:
        print(f"--- Với K = {k} ---")
        
        # Lấy k láng giềng gần nhất (cắt k phần tử đầu tiên của list đã sắp xếp)
        neighbors = distances[:k]
        
        # Đếm phiếu bầu
        count_plus = 0
        count_minus = 0
        
        # Danh sách chi tiết để in ra màn hình
        neighbors_info = []
        
        for d, label, x_val in neighbors:
            neighbors_info.append(f"x={x_val}({label})")
            if label == '+':
                count_plus += 1
            else:
                count_minus += 1
        
        # In thông tin thống kê
        print(f"  + Láng giềng: {', '.join(neighbors_info)}")
        print(f"  + Số phiếu: (+) = {count_plus}, (-) = {count_minus}")
        
        # Kết luận dựa trên đa số phiếu (Majority Vote)
        result = ""
        if count_plus > count_minus:
            result = "+"
        else:
            result = "-"
            
        print(f"  -> KẾT QUẢ PHÂN LOẠI: Lớp {result}")
        print("")

# Điểm bắt đầu chạy chương trình
if __name__ == "__main__":
    knn_manual_code()
