from decorators import repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet('ABC')