# Execution of Coroutine

Execution of coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next() and send() method. This can be seen clearly in above example, as only after calling __next__() method, out coroutine starts executing. After this call, execution advances to the first yield expression, now execution pauses and wait for value to be sent to corou object. When first value is sent to it, it checks for prefix and print name if prefix present. After printing name it goes through loop until it encounters name = (yield) expression again.

# Closing a Coroutine

Coroutine might run indefinitely, to close coroutine close() method is used. When coroutine is closed it generates GeneratorExit exception which can be catched in usual way. After closing coroutine, if we try to send values, it will raise StopIteration exception. Following is a simple example :


# 

https://www.geeksforgeeks.org/coroutine-in-python/

