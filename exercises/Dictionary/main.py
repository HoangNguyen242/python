# Import

# Function

# Main
if __name__ == "__main__":
    print "Main component"

## Khai bao
data1={'Id':100, 'Ten':'Thanh', 'Nghenghiep':'Developer'}
data2={'Id':101, 'Ten':'Chinh', 'Nghenghiep':'Trainer'}

## Truy cap
print "Id cua nhan vien dau tien la",data1['Id']
print "Id cua nhan vien thu hai la",data2['Id']
print "Ten cua nhan vien dau tien la:",data1['Ten']
print "Nghe nghiep cua nhan vien thu hai la:",data2['Nghenghiep']

## Cap nhat
data1['Nghenghiep']='Manager'
data2['Mucluong']=17000000
data1['Mucluong']=12000000

print data1
print data2

## Xoa
del data1['Nghenghiep']
print data1
