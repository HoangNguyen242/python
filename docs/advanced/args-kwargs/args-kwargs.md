# Truyền tham số dạng *args, **kwargs trong python.
---

## 1. *args và **kwargs dùng để làm gì?

Khi khai báo 1 hàm, sử dụng *args và **kwargs cho phép bạn truyền vào bao nhiêu tham số cũng được mà không cần biết trước số lượng.

```python 
def sum(*args):
  	total = 0
  	for number in args:
    	total += number
    return total

// gọi hàm
sum(1, 2, 3,19)
sum( 1, 100)
```

## 2. *args và **kwargs khác gì nhau?

Khi gọi hàm trong Python, có 2 kiểu truyền tham số:
- Truyền tham số theo tên.
- Truyền tham số bình thường theo thứ tự khai báo đối số.

```python
def register(name, password):
	....

#Truyền tham số theo kiểu thông thường, phải theo đúng thứ tự
register( 'Coulson', 'hail_Hydra')
#Truyền tham số theo tên, Không cần phải theo thứ tự khai báo thao số
register( password='cookHim', name='Skye')
```

Lưu ý:
- *args nhận các tham số truyền bình thường. Sử dụng args như một list.
- **kwargs nhận tham số truyền theo tên. Sử dụng kwargs như một dictionary


```python
def test_args(*args):
	for item in args:
		print item
	
>>test_args('Hello', 'world!')
Hello
world!

def test_kwargs(*kwargs):
	for key, value in kwargs.iteritems():
		print '{0} = {1}'.format(key, value)
	
>>test_kwargs(name='Dzung', age=10)
age = 10
name = Dzung
```

## 3. Thứ tự sử dụng và truyền tham số *args, **kwargs và tham số bình thường
Thứ tự
```
đối số xác đinh --> *args --> **kwargs
```

> Đây là thứ tự bắt buộc. Và khi truyền tham số bạn cũng phải truyền theo đúng thứ tự này. Không thể truyền lẫn lộn giữa 2 loại.

Lưu ý
```
Khi sử dụng đồng thời *args **kwargs thì không thể truyền tham số bình thường theo tên
```

```python
def show_detail(name, *args, **kwargs):
.....

show_detail(name='Coulson', 'agent', age='40', level='A')
>>Error

def show_detail_2(name, **kwargs):
....

show_detail_2(name='Coulson', age='40', level='A')
```

# Nguồn

https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

https://daynhauhoc.com/t/cach-truyen-tham-so-dang-args-va-kwargs-trong-python/7115
