def dao_nguoc_chuoi(str):
    return str[::-1]

str = input("Nhập chuỗi: ")
print("Chuỗi sau khi đảo ngược là: ", dao_nguoc_chuoi(str))