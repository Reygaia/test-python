def chia_het_cho_5(value):
    if(int(value, 2) % 5 == 0):
        return True
    return False

numbers = []

input_str = input("Nhập 4 số nhị phân cách nhau bởi dấu , ");
binary_list = input_str.split(', ')
print(binary_list)
numbers = [number for number in binary_list if chia_het_cho_5(number)]

if len(numbers) > 0:
    print("Các số chia hết cho 5 là: ")
    print(numbers)
else:
    print("Không có số nào chia hết cho 5 !")

