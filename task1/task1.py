mass = []
accumulated_mass = []
input_date = []
tmp = 0


for i in input().split():
    input_date.append(int(i))

for i in range(1, input_date[0] + 1):
    mass.append(i)

if input_date[0] > 1:
    while True:
        tmp_lst = []
        for i in range(input_date[1]):
            tmp_lst.append(mass[tmp])
            if mass[tmp] == mass[-1]:
                tmp = 0
            else:
                tmp += 1
        accumulated_mass.append(tmp_lst)
        tmp -= 1
        if tmp == 0:
            break

    for i in accumulated_mass:
        print(i[0], end="")
else:
    print("Длина массива должна составлять более 1 элемента")


