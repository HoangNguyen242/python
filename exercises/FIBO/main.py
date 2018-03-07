def FIBO(n):
    a=b=1
    i=0
    while i<n:
        temp=b
        b=a+b
        a=temp
        print('{0} {1}'.format(a,b))
        i=i+1
    return 'done'

if __name__ == "__main__":
    list_raw=[]
i = 0
n = input("Nhap N: ")
n = int(n)
print(FIBO(n))
