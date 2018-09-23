def simple_gen():
    yield "Hello"
    yield "World"
gen = simple_gen()
print("First: ", next(gen))
print("Second: ", next(gen))