import csv
def Cre_stu(kk):
    f = open('.\course' + str(kk) + '.csv')
    File = csv.reader(f)
    flag = -1
    St = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for row in File:
        if flag == -1:
            flag = flag + 1
            continue
        for j in range(5, 25):
            St[j - 5].append(int(row[j]))
    return St
ans = 0
all = 0
suc = []
f = []
for i in range(0, 10):
    suc.append(0)
    f.append(0)
Stu = []
for i in range(1, 6):
    student = Cre_stu(i)
    for t in range(0, 20):
        if t == 0:
            for j in range(80, 90):
                all = all + 1
                if student[t][j] == 0:
                    suc[j - 80] = suc[j - 80] + 1
                    ans = ans + 1
                    Stu.append(j)
                else:
                    f[j - 80] = f[j - 80] + 1
            continue
        for j in Stu:
            if f[j - 80] >= 4 or suc[j - 80] > 16:
                continue
            all = all + 1
            if student[t][j] == 0:
                ans = ans + 1
                suc[j - 80] = suc[j - 80] + 1
            else:
                f[j - 80] = f[j - 80] + 1
print(ans / all)