# --- PHẦN 1: CHUẨN BỊ DỮ LIỆU ---

# Biểu diễn dữ liệu dưới dạng danh sách các tập hợp (List of Sets)
# Mỗi phần tử trong list là một giao dịch (transaction) chứa các item
transactions = [
    {'a', 'd', 'e'},       # Transaction ID: 0001
    {'a', 'b', 'c', 'e'},  # Transaction ID: 0024
    {'a', 'b', 'd', 'e'},  # Transaction ID: 0012
    {'a', 'c', 'd', 'e'},  # Transaction ID: 0031
    {'b', 'c', 'e'},       # Transaction ID: 0015
    {'b', 'd', 'e'},       # Transaction ID: 0022
    {'c', 'd'},            # Transaction ID: 0029
    {'a', 'b', 'c'},       # Transaction ID: 0040
    {'a', 'd', 'e'},       # Transaction ID: 0033
    {'a', 'b', 'e'}        # Transaction ID: 0038
]

# Tổng số lượng giao dịch (N)
total_transactions = len(transactions)

print(f"Tổng số giao dịch (N): {total_transactions}")
print("-" * 40)

# --- PHẦN 2: HÀM HỖ TRỢ TÍNH TOÁN ---

def get_support_count(dataset, itemset):
    """
    Hàm đếm số lần xuất hiện của một itemset trong toàn bộ dữ liệu.
    Input: 
        dataset: danh sách các giao dịch
        itemset: tập các mặt hàng cần đếm (dạng set)
    Output: 
        Số nguyên (count)
    """
    count = 0
    for transaction in dataset:
        # Kiểm tra nếu itemset là tập con (subset) của transaction
        if itemset.issubset(transaction):
            count += 1
    return count

def calculate_support(count, n):
    """Tính độ hỗ trợ (Support)"""
    return count / n

def calculate_confidence(support_union, support_antecedent):
    """Tính độ tin cậy (Confidence) = Support(X U Y) / Support(X)"""
    if support_antecedent == 0:
        return 0
    return support_union / support_antecedent

# --- PHẦN 3: GIẢI QUYẾT YÊU CẦU ĐỀ BÀI ---

# === CÂU A: TÍNH SUPPORT ===
print("a) Tính Support cho {e}, {b, d}, và {b, d, e}:\n")

# Định nghĩa các tập hợp cần tính
itemset_e = {'e'}
itemset_bd = {'b', 'd'}
itemset_bde = {'b', 'd', 'e'}

# 1. Tính cho {e}
count_e = get_support_count(transactions, itemset_e)
support_e = calculate_support(count_e, total_transactions)
print(f"   - Itemset {{e}}: Count = {count_e}, Support = {count_e}/{total_transactions} = {support_e}")

# 2. Tính cho {b, d}
count_bd = get_support_count(transactions, itemset_bd)
support_bd = calculate_support(count_bd, total_transactions)
print(f"   - Itemset {{b, d}}: Count = {count_bd}, Support = {count_bd}/{total_transactions} = {support_bd}")

# 3. Tính cho {b, d, e}
count_bde = get_support_count(transactions, itemset_bde)
support_bde = calculate_support(count_bde, total_transactions)
print(f"   - Itemset {{b, d, e}}: Count = {count_bde}, Support = {count_bde}/{total_transactions} = {support_bde}")

print("-" * 40)

# === CÂU B: TÍNH CONFIDENCE ===
print("b) Tính Confidence cho các luật kết hợp:\n")

# Luật 1: {b, d} -> {e}
# Antecedent (Giả thiết X): {b, d}
# Union (Hợp X U Y): {b, d, e}
conf_bd_to_e = calculate_confidence(support_bde, support_bd)
print(f"   1. Luật {{b, d}} -> {{e}}:")
print(f"      Confidence = Support({{b, d, e}}) / Support({{b, d}})")
print(f"      Confidence = {support_bde} / {support_bd} = {conf_bd_to_e} (hay {conf_bd_to_e * 100}%)")

print("\n")

# Luật 2: {e} -> {b, d}
# Antecedent (Giả thiết X): {e}
# Union (Hợp X U Y): {b, d, e} (tập hợp vẫn là b, d, e)
conf_e_to_bd = calculate_confidence(support_bde, support_e)
print(f"   2. Luật {{e}} -> {{b, d}}:")
print(f"      Confidence = Support({{b, d, e}}) / Support({{e}})")
print(f"      Confidence = {support_bde} / {support_e} = {conf_e_to_bd} (hay {conf_e_to_bd * 100}%)")

print("-" * 40)
