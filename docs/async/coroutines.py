def coro():
    hello = yield "Hello"
    yield hello

c = coro()
print(next(c))
print(c.send("World"))