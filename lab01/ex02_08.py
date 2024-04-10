def chia_het_cho_5(value):
    if(int(value, 2) % 5 == 0):
        return True
    return False

numbers = []

input_str = input("Nhap bon so nhi phan cach nhau boi dau , ");
binary_list = input_str.split(', ')
print(binary_list)
numbers = [number for number in binary_list if chia_het_cho_5(number)]

if len(numbers) > 0:
    print("Cac so chia het cho 5 la: ")
    print(numbers)
else:
    print("Khong co so nao chia het cho nam !")

