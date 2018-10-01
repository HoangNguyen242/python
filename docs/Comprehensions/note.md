the iterable is an object with elements that can be looped over. 

The iterator, on the other hand, represents a specific location in that iterable;

Two different iterators might be at different places in the list of words, but any one iterator can mark only one place.

# List comprehensions

Trong bài viết này, tôi sẽ giới thiệu một kỹ thuật rất hay được dùng trong python để tạo ra các cấu trúc dữ liệu như list, set, dict, đó là comprehensions. Sử dụng comprehension, ta có thể dễ dàng tạo ra các cấu trúc dữ liệu phức tạp theo cách rất tự nhiên chỉ với ít dòng code.

# Cú pháp
```
|| f(x) for x in iterable if condition ||
```

f(x) là hàm bất kỳ, và điều kiện if là tùy chọn. Khi sử dụng comprehensions để tạo ra một list ta gọi là list-comprehension, lúc đó cặp ký hiệu || || được thay bằng []. Còn khi thay || || bằng {} ta có set-comprehension hoặc dictionary-comprehension.

VD:
- Tạo List
```
[ f(x) for x in iterable if condition ]
```
- Tại dict
```
{ f(x) for x in iterable if condition }
```

VD:
```py
lst = []
for i in range(1,11):
	lst.append(i)
---
lst = [i for i in range(1, 11)]

```

```py
s = set()
for i in range(1,21):
	if i % 3 == 0:
    	s.add(i)

print(s)
{3, 6, 9, 12, 15, 18}

---

s = {i for i in range(1, 21) if i % 3 == 0}

print(s)
{3, 6, 9, 12, 15, 18}
```

```py
d = {}
for k in range(1, 21):
	if k % 3 == 0:
    	d[k] = k**2

print(d)
{18: 324, 3: 9, 6: 36, 9: 81, 12: 144, 15: 225}

---

d = {k: k**2 for k in range(1, 21) if k % 3 == 0}

print(d)
{18: 324, 3: 9, 6: 36, 9: 81, 12: 144, 15: 225}

```

# Nguồn

https://viblo.asia/p/su-dung-comprehensions-trong-python-pVYRPjJEG4ng