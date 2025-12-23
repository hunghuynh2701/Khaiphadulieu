import math

# 1. Dữ liệu đầu vào
# Tọa độ A1 đến A8
data = [
    (2, 10), # A1
    (2, 5),  # A2
    (8, 4),  # A3
    (5, 8),  # A4
    (7, 5),  # A5
    (6, 4),  # A6
    (1, 2),  # A7
    (4, 9)   # A8
]
names = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]

# Khởi tạo 3 tâm cụm ban đầu là A1, A2, A3
centroids = [list(data[0]), list(data[1]), list(data[2])]

def calc_distance(p1, p2):
    """Hàm tính khoảng cách Euclidean"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print("--- BẮT ĐẦU TÍNH TOÁN K-MEANS ---\n")

# Lặp 3 lần (đủ để thuật toán hội tụ với dữ liệu nhỏ này)
for iteration in range(1, 4):
    print(f"=== LẦN LẶP THỨ {iteration} ===")
    
    # Tạo 3 cụm rỗng
    clusters = [[], [], []] # Cụm 0 (tương ứng C1), Cụm 1 (C2), Cụm 2 (C3)
    clusters_names = [[], [], []]

    # BƯỚC 1: Gán điểm vào cụm
    for i in range(len(data)):
        point = data[i]
        # Tính khoảng cách từ điểm hiện tại tới 3 tâm
        d0 = calc_distance(point, centroids[0])
        d1 = calc_distance(point, centroids[1])
        d2 = calc_distance(point, centroids[2])
        
        # Tìm khoảng cách nhỏ nhất
        min_dist = min(d0, d1, d2)
        
        # Gán vào cụm tương ứng
        if min_dist == d0:
            clusters[0].append(point)
            clusters_names[0].append(names[i])
        elif min_dist == d1:
            clusters[1].append(point)
            clusters_names[1].append(names[i])
        else:
            clusters[2].append(point)
            clusters_names[2].append(names[i])

    # In kết quả phân nhóm của lần lặp này
    print(f"Cụm 1: {clusters_names[0]}")
    print(f"Cụm 2: {clusters_names[1]}")
    print(f"Cụm 3: {clusters_names[2]}")

    # BƯỚC 2: Cập nhật tâm cụm mới (Trung bình cộng)
    new_centroids = []
    converged = True # Giả sử đã hội tụ
    
    for k in range(3):
        group = clusters[k]
        if len(group) > 0:
            # Tính trung bình cộng X và Y
            avg_x = sum([p[0] for p in group]) / len(group)
            avg_y = sum([p[1] for p in group]) / len(group)
            new_centroid = [avg_x, avg_y]
        else:
            new_centroid = centroids[k] # Giữ nguyên nếu cụm rỗng

        # Kiểm tra xem tâm có thay đổi không
        if new_centroid != centroids[k]:
            converged = False
        
        new_centroids.append(new_centroid)
    
    print(f"Tâm cụm mới: {[[round(c[0], 2), round(c[1], 2)] for c in new_centroids]}")
    print("-" * 30)

    # Cập nhật lại tâm cụm cho vòng lặp sau
    centroids = new_centroids
    
    if converged:
        print("\n=> Thuật toán đã dừng (Hội tụ) vì tâm cụm không đổi.")
        break

print("\n--- KẾT QUẢ CUỐI CÙNG ---")
print(f"Cluster 1 (Tâm { [round(centroids[0][0],2), round(centroids[0][1],2)] }): {clusters_names[0]}")
print(f"Cluster 2 (Tâm { [round(centroids[1][0],2), round(centroids[1][1],2)] }): {clusters_names[1]}")
print(f"Cluster 3 (Tâm { [round(centroids[2][0],2), round(centroids[2][1],2)] }): {clusters_names[2]}")
