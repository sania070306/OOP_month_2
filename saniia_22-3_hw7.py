pos=None
resultOK = False
def binary_search(val, a):
    n=len(a)
    global pos, resultOK

    first=0
    last=n-1
    while first<last:
        middle=(first+last)//2
        if val==a[middle]:
            first=middle
            last=first
            resultOK=True
            pos=middle
        else:
            if val>a[middle]:
                first=middle+1
            else:
                last=middle-1
    return resultOK, pos



a=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
val=int(input('Загадайте число от 15 до 25: '))
ResultOK, Pos = binary_search(val, a)
if resultOK==True:
    print(f"Элемент найден \n {pos}")
else:
    print("Элемент не найден")




def buble_sort(a):
    r = len(a)
    for j in range(r-1):
        for i in range(r-1):
            if a[i] > a[i+1]:
                k = a[i+1]
                a[i+1] = a[i]
                a[i] = k
    print(a)

# print(buble_sort([5,9,7,6,24,1,2,3]))
