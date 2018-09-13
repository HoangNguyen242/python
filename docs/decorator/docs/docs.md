https://realpython.com/primer-on-python-decorators/


Mẫu thiết kế decorator chuẩn

```
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

@decorator
def func_abc(....):
    return ...
```

Lưu ý
- function có thể chứa function
- Bản chất function cũng là các object (Là 1 dạng class)
- Có thể truyển function như 1 đối số
