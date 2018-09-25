# property 
```py
class Foo:
    @property
    def foo(self):
        return self._foo
    @foo.setter
    def foo(self, value):
        self._foo = value

test = Foo() 
test.foo
test.foo = test
```
> Thực hiện như biến
---
# Don't Repeat Yourself (DRY) 
- Ko lặp lại code hay copy lại 1 đoạn code có chức năng giống nhau