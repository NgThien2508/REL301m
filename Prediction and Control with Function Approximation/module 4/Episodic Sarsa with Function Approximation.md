# Episodic Sarsa với Xấp Xỉ Hàm

## Tổng Quan
Episodic Sarsa là phương pháp GPI sử dụng xấp xỉ hàm để ước lượng giá trị hành động, cho phép xử lý không gian trạng thái lớn.

## Biểu Diễn Đặc Trưng Phụ Thuộc Hành Động

### Cấu Trúc Cơ Bản
- Vector trọng số: $w \in \mathbb{R}^d$
- Vector đặc trưng: $\phi(s,a) \in \mathbb{R}^d$
- Giá trị hành động: $\hat{q}(s,a,w) = w^T \phi(s,a)$

### Xếp Chồng Đặc Trưng
- Đặc trưng cho mỗi hành động
- Kết hợp thành vector lớn
- Cho phép biểu diễn phức tạp

## Tính Toán Giá Trị Hành Động

### Công Thức
$$\hat{q}(s,a,w) = w^T \phi(s,a)$$
- $w$: vector trọng số
- $\phi(s,a)$: vector đặc trưng
- $\hat{q}$: giá trị ước lượng

### Mạng Nơ-ron
- Đầu vào: trạng thái và hành động
- Đầu ra: giá trị hành động
- Tương đương với xếp chồng đặc trưng

## Tile Coding

### Biểu Diễn
- Sử dụng tile coding
- Đặc trưng cho mỗi hành động
- Hiệu quả tính toán

### So Sánh
- Tile coding: đặc trưng cố định
- Mạng nơ-ron: học đặc trưng
- Cả hai đều hiệu quả

## Thuật Toán Sarsa

### Khác Biệt với Sarsa Thông Thường
- Sử dụng hàm xấp xỉ
- Cập nhật trọng số
- Không cần bảng Q

### Cập Nhật Trọng Số
$$w_{t+1} = w_t + \alpha \delta_t \nabla_w \hat{q}(S_t,A_t,w_t)$$
- $\alpha$: tốc độ học
- $\delta_t$: TD error
- $\nabla_w \hat{q}$: gradient

## Kết Luận
Episodic Sarsa với xấp xỉ hàm cung cấp phương pháp hiệu quả để học chính sách trong không gian trạng thái lớn, kết hợp ưu điểm của Sarsa và xấp xỉ hàm.
