# Coroutines
---
## Cở bản
Thread cho phép Python programmer thực hiện nhiều hoạt động cùng 1 thời điểm. Nhưng nó tồn tại 3 vấn đề lớn:
- Yêu cầu công cụ để phối hợp các thread, khiên code trở nên phức tạp so với lập trình luồng (thủ tục).
- Thread yêu cầu nhiều bộ nhớ, cơ bản 8mb/thread. Với số lượng ít, nó ko phải là vấn đề, nhưng nếu với hàng nghìn thread xảy ra đồng thời nó sẽ trở thành vấn đề, đặc biệt đối với các dòng máy chủ khi phục vụ hàng ngàn người ... Các thread chạy độc lập sẽ không đáp ứng được.
- Thread tồn nhiều tài nguyên để bắt đầu, nếu tạo liên lục các hàm chạy đồng thời sẽ khiến máy tính trở nên chậm chạp.

Python có thể giải quyết vấn đề trên bằng khái niệm `coroutines`. Coroutines cho phép thực hiện nhiều tiến trình đồng thời trong chương trình Python. Chúng được thực hiện trên khái niệm mở rộng của generators. Tài nguyên được sử dụng khi generator coroutine. Sẽ tốn khoảng 1KB cho chúng nó.

Coroutines hoạt động bằng code genetator, gửi giá trị bằng hàm `send` vào biểu thức `yield`. Generator function nhận giá trị truyền từ `send function`

Giông thread có thể chạy mãi mãi, coroutines sẽ xử lý giá trị mỗi khi nhận được giá tị từ `send`. Giống thread, coroutines là hàm độc lập, có thể xử lý đầu vào từ môi trường, trả lại kết quả. Điều khác biệt là coroutines dừng lại tại mỗi yield expression và chạy khi nhận được hàm send từ bên ngoài. Đây là điều kỳ diệu của coroutines. 