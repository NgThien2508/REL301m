# Định Lý Gradient Chính Sách

## Tổng Quan
Định lý gradient chính sách cung cấp cách ước lượng gradient của phần thưởng trung bình từ kinh nghiệm, cho phép tối ưu hóa chính sách.

## Quá Trình Tối Ưu Hóa

### Mục Tiêu
- Tối đa hóa phần thưởng trung bình
- Tìm chính sách tối ưu
- Sử dụng gradient ascent

### Ước Lượng Gradient
- Từ dữ liệu mẫu
- Không cần mô hình
- Hiệu quả tính toán

## Biểu Diễn Định Lý

### Công Thức
$$\nabla_\theta J(\theta) = \mathbb{E}_\pi[\nabla_\theta \log \pi(A_t|S_t,\theta)q_\pi(S_t,A_t)]$$
- $J(\theta)$: phần thưởng trung bình
- $\pi(A_t|S_t,\theta)$: chính sách
- $q_\pi(S_t,A_t)$: giá trị hành động

### Thành Phần
- Gradient log chính sách
- Giá trị hành động
- Kỳ vọng theo phân phối trạng thái

## Ví Dụ Minh Họa

### Grid World
- Trạng thái: vị trí trong lưới
- Hành động: di chuyển
- Phần thưởng: đạt đích

### Điều Chỉnh Tham Số
- Tăng xác suất hành động tốt
- Giảm xác suất hành động xấu
- Dựa trên giá trị hành động

## Ứng Dụng

### Actor-Critic
- Actor: chính sách
- Critic: giá trị hành động
- Cập nhật song song

### Robot
- Học chính sách điều khiển
- Tối ưu hóa chuyển động
- Thích ứng với môi trường

## Kết Luận
Định lý gradient chính sách cung cấp nền tảng lý thuyết cho việc học chính sách trực tiếp, cho phép tối ưu hóa hiệu quả trong nhiều bài toán thực tế.
