import itertools

def main():
    # Dữ liệu đầu vào: Tập phổ biến 3-itemsets (F3)
    # Lưu ý: Các phần tử bên trong mỗi tập con phải được sắp xếp tăng dần
    F3 = [
        [1, 2, 3], [1, 2, 4], [1, 2, 5],
        [1, 3, 4], [1, 3, 5],
        [2, 3, 4], [2, 3, 5],
        [3, 4, 5]
    ]
    
    # Tập hợp các item duy nhất (F1)
    items = {1, 2, 3, 4, 5}
    
    print("--- DỮ LIỆU ĐẦU VÀO (F3) ---")
    print(F3)
    print("\n")

    # ==========================================
    # CÂU A: Chiến lược F(k-1) x F1
    # ==========================================
    candidates_a = set()
    for itemset in F3:
        for item in items:
            if item not in itemset:
                # Tạo tập mới, sắp xếp và chuyển thành tuple để có thể add vào set (tránh trùng lặp)
                new_candidate = sorted(itemset + [item])
                candidates_a.add(tuple(new_candidate))
    
    print(f"--- CÂU (a): Ứng viên từ chiến lược F(k-1) x F1 ({len(candidates_a)} tập) ---")
    sorted_candidates_a = sorted([list(c) for c in candidates_a])
    print(sorted_candidates_a)
    print("\n")

    # ==========================================
    # CÂU B: Chiến lược Apriori (Join step) F(k-1) x F(k-1)
    # ==========================================
    candidates_b = []
    k = 4
    n = len(F3)
    
    # Duyệt qua từng cặp itemset trong F3
    for i in range(n):
        for j in range(i + 1, n):
            list1 = F3[i]
            list2 = F3[j]
            
            # Kiểm tra k-2 phần tử đầu tiên (ở đây là 2 phần tử đầu)
            # Nếu prefix giống nhau, ta ghép lại
            if list1[:k-2] == list2[:k-2]:
                # Ghép list1 với phần tử cuối của list2
                new_candidate = sorted(list(set(list1) | set(list2)))
                candidates_b.append(new_candidate)
                
    print(f"--- CÂU (b): Ứng viên từ Apriori Join ({len(candidates_b)} tập) ---")
    print(candidates_b)
    print("\n")

    # ==========================================
    # CÂU C: Bước Cắt tỉa (Pruning step)
    # ==========================================
    survived_candidates = []
    
    # Chuyển F3 thành set các tuple để việc tìm kiếm (lookup) nhanh hơn
    F3_set = set(tuple(x) for x in F3)
    
    print("--- CÂU (c): Chi tiết bước Cắt tỉa (Pruning) ---")
    
    for cand in candidates_b:
        is_valid = True
        print(f"Kiểm tra ứng viên: {cand}")
        
        # Sinh tất cả các tập con kích thước k-1 (tức là 3)
        subsets = list(itertools.combinations(cand, 3))
        
        for subset in subsets:
            # combination trả về tuple, cần convert list -> tuple để so sánh
            if subset not in F3_set:
                print(f"  -> Loại bỏ vì tập con {list(subset)} không nằm trong F3")
                is_valid = False
                break # Nếu 1 tập con thiếu thì loại luôn, không cần check tiếp
        
        if is_valid:
            print("  -> GIỮ LẠI (Tất cả tập con đều hợp lệ)")
            survived_candidates.append(cand)
            
    print("\n--- KẾT QUẢ CUỐI CÙNG (CÂU C) ---")
    print(survived_candidates)

if __name__ == "__main__":
    main()
