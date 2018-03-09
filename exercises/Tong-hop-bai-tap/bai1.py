# Import

# Function

# Main
if __name__ == "__main__":
    print "Main component"

##

j=[]
for i in range(100, 200):
    if (i%7==0) and (i%5!=0):
       j.append(str(i))
print (','.join(j))
