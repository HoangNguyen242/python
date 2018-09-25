# Python iterator & generator
---
# Iterable

Có rất nhiều đối tượng chúng ta có thể sử dụng vòng lặp for. Những đối tượng đó gọi là những đối tượng "iterable". Và thao tác duyệt qua những đối tượng này gọi là iteration.

```
>>> for i in [1, 2, 3, 4]:
...     print(i)
...

>>> for c in "python":
...     print(c)

>>> for k in {"x": 1, "y": 2}:
...     print(k)
...
y
x

>>> for line in open("a.txt"):
...     print(line)
...

```


# Giao thức interation

Những đối tượng "iterable" có thể được duyệt qua các phần tử, bởi vì chúng được cài đặt phương thức __iter__. Phương thức này sẽ trả về một đối tượng iterator. Đối tượng này cần phải hỗ trợ giao thức iteration (sẽ được nói đến sau). Nếu một đối tượng "iterable" có nhiều kiểu duyệt phần tử khác nhau, có thể chúng ta sẽ cần thêm các xử lý để xác định iterator. (Ví dụ một đồ thị có thể duyệt theo chiều rộng và theo chiều sâu.)

Với đối tượng iterator, nó cần phải được cài đặt hai phương thức sau, và bộ hai phương thức này được gọi là giao thức iteration.
- Phương thức __iter__ trả về chính đối tượng iterator. Phương thức này được yêu cầu cài đặt cho cả đối tượng "iterable" và iterator để có thể sử dụng các câu lệnh for và in.
- Phương thức __next__ (ở Python 2 là next) trả về phần tử tiếp theo. Nếu không còn phần tử nào nữa thì StopIteration exception sẽ được raise.

```
class yrange:

    def __init__(self, n):
            self.i = 0
            self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
```

> Phương thức __iter__ sẽ làm đối tượng trở thành đối tượng "iterable". Về bản chất, hàm iter sẽ gọi đến phương thức __iter__ này của mỗi đối tượng.


Một hàm dựng sẵn của Python là iter nhận đầu vào là một đối tượng "iterable" và trả về kết quả là một iterator.

Iterator của Python có một đặc điểm là nó chỉ có thể được duyệt qua 1 lần. Nên nếu đã duyệt qua phần tử nào rồi thì bạn không thể duyệt qua nó thêm lần nào nữa.

```
>>> y = yrange(3)
>>> y.__next__()
0
>>> y.__next__()
1
>>> y.__next__()
2
>>> y.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 14, in next
StopIteration
```

Vì đặc điểm trên, nên nếu iterator và đối tượng "iterable" là một, thì nó cũng chỉ có thể thực hiện iteration một lần. Nhưng nếu chúng không phải là một, thì bạn có thể thực hiện bao nhiêu lần tùy ý.

# Generator
Generator là cách đơn giản để tạo ra iterator. Một generator là một hàm trả kết quả về là một chuỗi kết quả thay vì một giá trị duy nhất.

```
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

Mỗi lần lệnh yield được chạy, nó sẽ sinh ra một giá trị mới. (Vì thế nó mới được gọi là generator)
```
>>> y = yrange(3)
>>> y
<generator object yrange at 0x7f80c2f816d0>
>>> y.__next__()
0
>>> y.__next__()
1
>>> y.__next__()
2
>>> y.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Một generator cũng là một iterator nên bạn không cần phải lo lắng về giao thức iteration.

> Từ generator được sử dụng cho cả hàm (hàm generator là hàm đã nói ở trên) và kết quả mà hàm đó sinh ra (đối tượng được hàm generator sinh ra cũng được gọi là generator). Vì vậy đôi khi việc này gây khó hiểu một chút.

Khi phương thức __next__ được gọi, hàm generator sẽ bắt đầu chạy, cho tới khi nó gặp lệnh yield. Giá trị được yield sẽ được trả về cho hàm __next__.

```
>>> def foo():
...     print("begin")
...     for i in range(3):
...         print("before yield", i)
...         yield i
...         print("after yield", i)
...     print("end")
...
>>> f = foo()
>>> f.__next__()
begin
before yield 0
0
>>> f.__next__()
after yield 0
before yield 1
1
>>> f.__next__()
after yield 1
before yield 2
2
>>> f.__next__()
after yield 2
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

# Tại sao nên sử dụng generator
Việc sử dụng generator sẽ đem lại nhiều tác dụng rất lớn.

## Đơn giản hóa code
Cơ bản
```python
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
```

iterator
```python
class firstn(object):

    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()

sum_of_first_n = sum(firstn(1000000))
```

generator
```py
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
```
## Nâng cao hiệu suất

Việc sử dụng generator có thể nâng cao hiệu suất bởi vì generator chỉ thực sự sinh kết quả khi được gọi. Do đó, nó sẽ sử dụng ít bộ nhớ hơn. Ngoài ra, chúng ta không cần phải chờ tất cả các phần tử của nó được sinh ra hết mới có thể sử dụng. Chúng sẽ được sinh trong quá trình chúng ta gọi generator. Đây là những hiệu quả đạt được khi chúng ta sử dụng iterator, mà generator là cách ngắn gọn để tạo ra một iterator.



# Nguồn 
https://viblo.asia/p/python-iterator-generator-gVQelQJVkZJ
