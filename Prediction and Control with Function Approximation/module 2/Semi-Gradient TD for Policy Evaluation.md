# Semi-Gradient TD cho Đánh Giá Chính Sách

## Tổng Quan
Semi-Gradient TD là phương pháp ước lượng giá trị kết hợp giữa Temporal Difference và gradient descent, sử dụng bootstrap để cập nhật trọng số.

## Nguyên Lý

### TD Target
$$\delta_t = R_{t+1} + \gamma \hat{v}(S_{t+1},w_t) - \hat{v}(S_t,w_t)$$
Trong đó:
- $R_{t+1}$: phần thưởng
- $\gamma$: hệ số chiết khấu
- $\hat{v}(S_t,w_t)$: giá trị ước lượng

### Cập Nhật Trọng Số
$$w_{t+1} = w_t + \alpha \delta_t \nabla_w \hat{v}(S_t,w_t)$$

## Đặc Điểm

### Ưu Điểm
- Học trực tuyến
- Phương sai thấp
- Hội tụ nhanh

### Hạn Chế
- Thiên vị do bootstrap
- Phụ thuộc vào giá trị khởi tạo
- Có thể không hội tụ

## Thuật Toán

### Khởi Tạo
- Vector trọng số w
- Tốc độ học α
- Hàm xấp xỉ giá trị

### Vòng Lặp Học
1. **Quan sát trạng thái**
   - Nhận St từ môi trường
   - Tính $\hat{v}(S_t,w_t)$

2. **Thực hiện hành động**
   - Chọn At theo π
   - Nhận Rt+1 và St+1

3. **Cập nhật trọng số**
   - Tính TD error
   - Cập nhật w

## Ứng Dụng

### Xấp Xỉ Tuyến Tính
- $\hat{v}(s,w) = w^T \phi(s)$
- $\nabla_w \hat{v}(s,w) = \phi(s)$

### Mạng Nơ-ron
- Sử dụng backpropagation
- Cập nhật tất cả các lớp

## Kết Luận
Semi-Gradient TD cung cấp phương pháp đánh giá chính sách hiệu quả, đặc biệt phù hợp với các bài toán cần học nhanh và ổn định.
