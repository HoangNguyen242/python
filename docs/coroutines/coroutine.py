# Python3 program for demonstrating  
# coroutine execution 
  
def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    while True: 
        name = (yield) 
        if prefix in name: 
            print(name) 
  
# calling coroutine, nothing will happen 
corou = print_name("Dear") 
  
# This will start execution of coroutine and  
# Prints first line "Searchig prefix..." 
# and advance execution to the first yield expression 
corou.__next__() 
  
# sending inputs 
corou.send("Atul") 
corou.send("Dear Atul")