def list_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        min_id = i
        for j in range(i+1,len(list_to_sort)):
            if list_to_sort[min_id] > list_to_sort[j]:
                min_id = j
        list_to_sort[i], list_to_sort[min_id] = list_to_sort[min_id], list_to_sort[i]

if __name__ == "__main__":
    list_raw=[]
i = 0
n = input("Nhap so luong: ")
n = int(n)
while i < n:
    temp = input("Nhap n[{0}]: ".format(i))
    list_raw.append(temp)
    i=i+1
list_sort(list_raw)
print(list_raw)
