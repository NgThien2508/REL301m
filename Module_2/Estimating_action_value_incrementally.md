# Ước tính Giá trị Hành động theo Phương pháp Tăng dần

## Giới thiệu
Trong thực tế, việc lưu trữ và tính toán tất cả dữ liệu quá khứ có thể gặp khó khăn với bộ dữ liệu lớn. Ví dụ: một trang web có hàng triệu lượt truy cập mỗi ngày, việc tính toán giá trị trung bình của các quảng cáo sẽ tốn nhiều tài nguyên. Vì vậy, chúng ta cần một phương pháp hiệu quả hơn.

## Phương pháp Cập nhật Tăng dần (Incremental Update)

### Công thức Tổng quát
$$Q_{n+1} = Q_n + \alpha_n(R_n - Q_n)$$

Trong đó:
- $Q_{n+1}$: Giá trị ước tính mới
- $Q_n$: Giá trị ước tính hiện tại
- $R_n$: Phần thưởng mới nhận được
- $\alpha_n$: Kích thước bước (step size)
- $(R_n - Q_n)$: Sai số của ước tính hiện tại

### Chứng minh từ Phương pháp Trung bình Mẫu
1. Công thức ban đầu:
   $$Q_{n+1} = \frac{1}{n}\sum_{i=1}^n R_i$$

2. Tách phần tử mới nhất:
   $$Q_{n+1} = \frac{1}{n}(R_n + \sum_{i=1}^{n-1} R_i)$$

3. Biến đổi:
   $$Q_{n+1} = \frac{1}{n}(R_n + (n-1)Q_n)$$
   $$= \frac{1}{n}R_n + \frac{n-1}{n}Q_n$$
   $$= Q_n + \frac{1}{n}(R_n - Q_n)$$

### Ý nghĩa các thành phần
1. **Step Size ($\alpha_n$)**:
   - Trong phương pháp trung bình mẫu: $\alpha_n = \frac{1}{n}$
   - Điều chỉnh mức độ ảnh hưởng của dữ liệu mới
   - Giá trị từ 0 đến 1

2. **Target Error $(R_n - Q_n)$**:
   - Sai số giữa giá trị thực tế và ước tính
   - Chỉ ra hướng và độ lớn cần điều chỉnh

## Ứng dụng cho Bài toán Non-stationary

### Định nghĩa
Bài toán non-stationary là khi phân phối phần thưởng thay đổi theo thời gian.

### Ví dụ:
Một bác sĩ điều trị với 3 phương pháp (P, Y, B):
- Phương pháp B hiệu quả hơn vào mùa đông
- Hiệu quả của các phương pháp thay đổi theo thời gian
- Tỷ lệ thành công: P(0.25), Y(0.75), B(0.9)

### Giải pháp: Sử dụng Step Size Cố định
1. **Cách tiếp cận**:
   - Sử dụng $\alpha_n = \alpha$ (ví dụ: 0.1)
   - Ưu tiên dữ liệu gần đây hơn dữ liệu cũ

2. **Công thức tổng quát**:
   $$Q_{n+1} = Q_n + \alpha(R_n - Q_n)$$
   $$= \alpha R_n + (1-\alpha)Q_n$$
   $$= \alpha R_n + (1-\alpha)[\alpha R_{n-1} + (1-\alpha)Q_{n-1}]$$
   $$= \alpha R_n + (1-\alpha)\alpha R_{n-1} + (1-\alpha)^2Q_{n-1}$$

3. **Trọng số của phần thưởng quá khứ**:
   - $R_n$: $\alpha$
   - $R_{n-1}$: $\alpha(1-\alpha)$
   - $R_{n-2}$: $\alpha(1-\alpha)^2$
   - Giảm theo hàm mũ với thời gian

## Kết luận
1. Phương pháp cập nhật tăng dần giúp:
   - Tiết kiệm bộ nhớ
   - Tính toán hiệu quả
   - Thích ứng với môi trường thay đổi

2. Lựa chọn step size:
   - $\alpha_n = \frac{1}{n}$ cho môi trường stationary
   - $\alpha_n = \alpha$ (cố định) cho môi trường non-stationary
