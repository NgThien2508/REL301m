# Gradient Monte Carlo cho Đánh Giá Chính Sách

## Tổng Quan
Gradient Monte Carlo là phương pháp ước lượng giá trị sử dụng gradient descent và returns từ Monte Carlo để đánh giá chính sách.

## Nguyên Lý

### Hàm Mục Tiêu
$$J(w) = \frac{1}{2} \mathbb{E}[(G_t - \hat{v}(S_t,w))^2]$$
Trong đó:
- $G_t$: return từ thời điểm t
- $\hat{v}(S_t,w)$: giá trị ước lượng
- $w$: tham số cần học

### Cập Nhật Gradient
$$w_{t+1} = w_t + \alpha[G_t - \hat{v}(S_t,w_t)]\nabla_w \hat{v}(S_t,w_t)$$

## Đặc Điểm

### Ưu Điểm
- Ước lượng không thiên vị
- Hội tụ đến giá trị thực
- Đơn giản trong triển khai

### Hạn Chế
- Cần đợi kết thúc episode
- Phương sai cao
- Học chậm hơn TD

## Thuật Toán

### Khởi Tạo
- Vector trọng số w
- Tốc độ học α
- Hàm xấp xỉ giá trị

### Vòng Lặp Học
1. **Thu thập episode**
   - Theo dõi chính sách π
   - Ghi lại trạng thái và phần thưởng

2. **Tính returns**
   - Tính Gt cho mỗi bước thời gian
   - Sử dụng discount factor γ

3. **Cập nhật trọng số**
   - Tính gradient
   - Cập nhật w

## Ứng Dụng

### Xấp Xỉ Tuyến Tính
- $\hat{v}(s,w) = w^T \phi(s)$
- $\nabla_w \hat{v}(s,w) = \phi(s)$

### Mạng Nơ-ron
- Sử dụng backpropagation
- Cập nhật tất cả các lớp

## Kết Luận
Gradient Monte Carlo cung cấp phương pháp đánh giá chính sách đơn giản và hiệu quả, đặc biệt phù hợp với các bài toán có episode ngắn.
