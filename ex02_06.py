input_str = input("Nhập X: ")

dimension = [int(x) for x in input_str.split(',')]

rowNum = dimension[0]
columnNum = dimension[1]

multilist = [[0 for col in range(columnNum)] for row in range(rowNum)]
for row in range (rowNum): 
    for col in range (columnNum):
        multilist[row][col] = row * col

print(multilist) 
        