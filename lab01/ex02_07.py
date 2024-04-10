print("Nhap cac dong van ban (Nhap 'done' de thoat): ")
lines = []

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Cac dong van ban sau khi in hoa")
for line in lines:
    print(line.upper())