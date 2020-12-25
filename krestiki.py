znah = [[" ", "|", "0", "1", "2"],
        ["-", "+", "-", "-", "-"],
        ["0", "|", ".", ".", "."],
        ["1", "|", ".", ".", "."],
        ["2", "|", ".", ".", "."]]

hod = "Y"

c = "Играем"

b = 0

yz = 0

def pobeda():
    global b, c
    if znah[2][2] == znah[2][3] == znah[2][4] == hod:
        b, c = 1, "Победа"
    elif znah[3][2] == znah[3][3] == znah[3][4] == hod:
        b, c = 1, "Победа"
    elif znah[4][2] == znah[4][3] == znah[4][4] == hod:
        b, c = 1, "Победа"
    elif znah[2][2] == znah[3][2] == znah[4][2] == hod:
        b, c = 1, "Победа"
    elif znah[2][3] == znah[3][3] == znah[4][3] == hod:
        b, c = 1, "Победа"
    elif znah[2][4] == znah[3][4] == znah[4][4] == hod:
        b, c = 1, "Победа"
    elif znah[2][2] == znah[3][3] == znah[4][4] == hod:
        b, c = 1, "Победа"
    elif znah[4][2] == znah[3][3] == znah[2][4] == hod:
        b, c = 1, "Победа"

def pusto ():
    global c, yz
    yz = 0
    for y in range(2, 5):
        for z in range(2, 5):
            if znah[y][z] == ".":
                yz += 1
                c = "Играем дальше"

def pole ():
    for x in znah:
        print(x[0], x[1], x[2], x[3], x[4])

def vvod ():
    i = int(input("Введите строку: "))
    j = int(input("Введите столбец: "))
    if znah[i+2][j+2] == ".":
        znah[i+2][j+2] = hod
    else:
        pole()
        print()
        print("Клетка занята!")
        print(c)
        print("Ход ", hod)
        vvod()

pole()

while b == 0:
    if hod == "X":
        hod = "Y"
    else:
        hod = "X"
    print()
    print(c)
    print("Ход ", hod)
    vvod()
    pole()
    pusto()
    pobeda()
    if yz == 0:
        b, c, hod = 1, "Ничья ", " "

print()
print(c, hod)