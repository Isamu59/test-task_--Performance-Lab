import math


def check_point_gpt(x, y):
    gpt = math.sqrt((x - cord_oval[0]) ** 2 + (y - cord_oval[1]) ** 2)

    if gpt < radius_oval:
        print(1)
    elif gpt == radius_oval:
        print(0)
    else:
        print(2)


f1 = open("file1.txt")
cord_oval = [float(n) for n in (f1.readline()).split()]
radius_oval = float(f1.readline())
f1.close()

f2 = open("file2.txt")
for i in f2:
    temp = [float(j) for j in (i.split())]
    check_point_gpt(temp[0], temp[1])
f2.close()
