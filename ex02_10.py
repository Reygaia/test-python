def dao_nguoc_chuoi(str):
    return str[::-1]

str = input("Nhap chuoi: ")
print("Chuoi sau khi dao nguoc la: ", dao_nguoc_chuoi(str))