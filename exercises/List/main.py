# Import

# Function

# Main
if __name__ == "__main__":
    print("Main component") 

## Khai bao
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

## Truy cap List
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

## Cap nhat gia tri
print("Gia tri tai vi tri 2 chuoi list2 : ")
print(list2[2])

print("Cap nhat gia tri list2 : ")
list2[2] = 2001
print(list2[2])

## Xoa phan list
print("Xoa phan tu list1 : ")
print(list1)
del list1[2]
print(list1)

## Lay do dai list
print("Do dai list1 : ",len(list1))

## Them phan tu vao list
print("Them phan tu list1 : ")
print(list1)
list1.append("Capnhat1")
print(list1)

##
