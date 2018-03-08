# function define
## Sum
def sum( arg1, arg2 ):
   # Cong hai tham so va tra ve ket qua."
   total = arg1 + arg2
   print(total)
   return total
##
def msg(Id,Name,Age=21):
    "In gia tri da truyen"
    print(Id)
    print(Name)
    print(Age)
    return
##
def msg_key(id,name):
    print(id)
    print(name)
    return

# Main
# if __name__ == "__main__":
print("Ben ngoai ham : {0}".format(sum( 10, 20 )))
msg(Id=100,Name='Hoang',Age=20)
msg(Id=101,Name='Thanh')

msg_key(id=100,name='Hoang')
msg_key(name='Thanh',id=101)

##
square=lambda x1: x1*x1
print("Binh phuong cua so la",square(10))
