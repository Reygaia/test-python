print("Nhập các dòng văn bản (Nhập 'done' để thoát): ")
lines = []

while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Các dòng văn bản sau khi in hoa")
for line in lines:
    print(line.upper())