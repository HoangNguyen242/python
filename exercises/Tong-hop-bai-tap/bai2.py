# Import

# Function
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
# Main
if __name__ == "__main__":
    print "Main component"

x=int(input("Nhap so N: "))
