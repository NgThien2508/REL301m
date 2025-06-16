# Chuyển Sang Hàm Tham Số Hóa

## Tổng Quan
Trong học tăng cường, việc sử dụng hàm tham số hóa cho phép chúng ta xử lý các không gian trạng thái lớn và liên tục một cách hiệu quả.

## Lý Do Sử Dụng

### Hạn Chế Của Bảng
- Không gian trạng thái lớn
- Trạng thái liên tục
- Tốn bộ nhớ
- Khó tổng quát hóa

### Ưu Điểm Của Hàm Tham Số
- Biểu diễn gọn gàng
- Tổng quát hóa tốt
- Xử lý được trạng thái mới
- Tiết kiệm bộ nhớ

## Các Loại Hàm Tham Số

### Hàm Tuyến Tính
$$\hat{v}(s,w) = w^T \phi(s)$$
Trong đó:
- $w$: vector trọng số
- $\phi(s)$: vector đặc trưng

### Hàm Phi Tuyến
- Mạng nơ-ron
- Hàm đa thức
- Hàm RBF

## Đặc Trưng Trạng Thái

### Tiền Xử Lý
- Chuẩn hóa
- Mã hóa one-hot
- Tạo đặc trưng tổng hợp

### Lựa Chọn Đặc Trưng
- Phù hợp với bài toán
- Đủ thông tin
- Không dư thừa

## Tối Ưu Hóa

### Hàm Mục Tiêu
$$J(w) = \frac{1}{2} \mathbb{E}[(v_{\pi}(s) - \hat{v}(s,w))^2]$$

### Gradient Descent
$$w_{t+1} = w_t - \alpha \nabla_w J(w_t)$$

## Ứng Dụng

### Ước Lượng Giá Trị
- Học giá trị trạng thái
- Học giá trị hành động
- Tối ưu hóa chính sách

### Kiểm Soát
- Tìm chính sách tối ưu
- Cân bằng khám phá/khai thác
- Học trực tuyến

## Kết Luận
Hàm tham số hóa mở ra khả năng giải quyết các bài toán phức tạp trong học tăng cường, cho phép chúng ta xử lý hiệu quả các không gian trạng thái lớn và liên tục.
