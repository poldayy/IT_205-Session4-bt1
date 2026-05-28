cost = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

if cost >= 500000:
    money_desc = cost * 0.1
else:
    money_desc = 0
int(money_desc)
total_cost = cost - money_desc

print("--- Hóa đơn thanh toán Rikkei Store ---")
print(f"Số tiền được giảm giá: {money_desc} VND")
print(f"Tổng tiền khách phải trả: {total_cost} VND")
