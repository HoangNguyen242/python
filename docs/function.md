# Hàm trong python
---
## Định nghĩa một hàm trong Python
Khi định nghĩa các hàm để cung cấp một tính năng nào đó, bạn cần theo các qui tắc sau:
- Từ khóa def được sử dụng để bắt đầu phần định nghĩa hàm. Def xác định phần bắt đầu của khối hàm.
- def được theo sau bởi ten_ham được theo sau bởi các dấu ngoặc đơn ().
- Các tham số được truyền vào bên trong các dấu ngoặc đơn. Ở cuối là dấu hai chấm.
- Trước khi viết một code, một độ thụt dòng được cung cấp trước mỗi lệnh. Độ thụt dòng này nên giống nhau cho tất cả các lệnh bên trong hàm đó.
- Lệnh đầu tiên của hàm là tùy ý, và nó là Documentation String của một hàm đó.
- Sau đó là lệnh để được thực thi.

## Cú pháp
```python
def ten_ham( cac_tham_so ):
   "function_docstring"
   function_suite
   return [bieu_thuc]
```
VD:
```python
# Phan dinh nghia ham o day
def printme( str ):
   "Chuoi nay duoc truyen vao trong ham"
   print str
   return;

# Bay gio ban co the goi ham printme
printme("Loi goi dau tien toi custom func!")
printme("Loi goi thu hai toi custom func")
```
