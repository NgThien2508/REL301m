# Temporal Difference (TD) Learning

## 1. Tổng Quan
Temporal Difference (TD) learning là một phương pháp học tăng cường kết hợp giữa Monte Carlo và Dynamic Programming. Phương pháp này cho phép học từng bước, cập nhật giá trị dựa trên sự khác biệt giữa dự đoán liên tiếp.

## 2. Các Thành Phần Chính

### 2.1. TD Error
- Đo lường sự khác biệt giữa dự đoán
- Cập nhật giá trị dựa trên sai số
- Học từng bước
- Cải thiện dự đoán

### 2.2. Bootstrapping
- Sử dụng giá trị ước tính
- Cập nhật dựa trên dự đoán
- Học nhanh hơn
- Hiệu quả hơn Monte Carlo

## 3. Công Thức Toán Học

### 3.1. TD Error
$$\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$$

### 3.2. Cập Nhật Giá Trị
$$V(S_t) \leftarrow V(S_t) + \alpha \delta_t$$

Trong đó:
- $\delta_t$: TD error
- $R_{t+1}$: Phần thưởng
- $\gamma$: Hệ số chiết khấu
- $\alpha$: Tốc độ học

## 4. Ứng Dụng Thực Tế

### 4.1. Trong Trò Chơi
- Học chiến lược tối ưu
- Cải thiện hiệu suất
- Thích ứng với thay đổi
- Tối ưu hóa quyết định

### 4.2. Trong Robot Học
- Học các kỹ năng phức tạp
- Cải thiện khả năng ra quyết định
- Thích ứng với môi trường
- Tối ưu hóa hiệu suất

## 5. Ưu Điểm và Hạn Chế

### 5.1. Ưu Điểm
- Học từng bước
- Không yêu cầu mô hình
- Hội tụ nhanh hơn Monte Carlo
- Hiệu quả trong nhiều bài toán

### 5.2. Hạn Chế
- Có thể không ổn định
- Phụ thuộc vào dự đoán
- Yêu cầu điều chỉnh tham số
- Có thể bị thiên vị

## 6. So Sánh Với Các Phương Pháp Khác

### 6.1. So Với Monte Carlo
- Học từng bước vs học theo tập
- Hội tụ nhanh hơn
- Hiệu quả hơn trong nhiều trường hợp
- Yêu cầu ít bộ nhớ hơn

### 6.2. So Với Dynamic Programming
- Không yêu cầu mô hình
- Học từ kinh nghiệm
- Thích ứng với môi trường
- Linh hoạt hơn

## 7. Kết Luận
Temporal Difference learning cung cấp một cách tiếp cận hiệu quả để học trong học tăng cường, kết hợp ưu điểm của Monte Carlo và Dynamic Programming. Mặc dù có một số hạn chế, phương pháp này vẫn được sử dụng rộng rãi trong nhiều ứng dụng thực tế.
