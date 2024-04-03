def la_so_nguyen_to(value):
    cnt = 0
    for i in range(1, value + 1):
        if(value % i == 0):
            cnt+=1
    return cnt == 2


number = int(input("Nhập số cần kiểm tra: "))
print(la_so_nguyen_to())