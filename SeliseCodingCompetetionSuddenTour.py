from random import randint
import operator

space = 0
count = 0
neon = 0
T = int(input("Number of Test Cases(<11) = "))
if T > 11:
    print("Number of cases should not exceed 11")

for i in range(0, T):
    Si_Fi = {}
    N = int(input("Number of items(0<=100) = "))
    if N > 101:
        print("number of items should not be more than 100")
    C = int(input("Total Capacity(0<=100000) = "))
    if C > 100001:
        print("Capacity should not exceed 100000")
    for j in range(0, N):
        Si = randint(0, 10000)
        Fi = randint(0, 10000)
        Si_Fi.update({Si: Fi})
        sorted_Si_Fi = dict(sorted(Si_Fi.items(), key=operator.itemgetter(1), reverse=True))

    for x in sorted_Si_Fi:
        if space < C:
            space += x
            count +=1
        elif space > C:
            break

    fun_Max = max(sorted_Si_Fi.values())
    print("Case:", i + 1,",Max Fun Value:" ,fun_Max,",Number of Carried Items:",count)

    del Si_Fi
