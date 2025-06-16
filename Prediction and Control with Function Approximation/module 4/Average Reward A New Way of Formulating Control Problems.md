# Phần Thưởng Trung Bình: Cách Tiếp Cận Mới cho Bài Toán Điều Khiển

## Tổng Quan
Phần thưởng trung bình cung cấp cách tiếp cận mới cho bài toán điều khiển, cho phép tối ưu hóa hiệu suất dài hạn mà không cần hệ số chiết khấu.

## MDP Tầm Nhìn Hạn Chế

### Cấu Trúc
- Hai chính sách xác định
- Phần thưởng khác nhau
- Không gian trạng thái đơn giản

### So Sánh Chính Sách
- Chính sách 1: phần thưởng thấp
- Chính sách 2: phần thưởng cao
- Khác biệt rõ ràng

## Hàm Giá Trị dưới Chiết Khấu

### Chính Sách 1
$$V_1(s) = \sum_{t=0}^{\infty} \gamma^t R_1$$
- $R_1$: phần thưởng thấp
- $\gamma$: hệ số chiết khấu

### Chính Sách 2
$$V_2(s) = \sum_{t=0}^{\infty} \gamma^t R_2$$
- $R_2$: phần thưởng cao
- $\gamma$: hệ số chiết khấu

## Phần Thưởng Trung Bình

### Định Nghĩa
$$R_\pi = \lim_{t \to \infty} \frac{1}{t} \sum_{k=0}^{t-1} R_k$$
- $R_\pi$: phần thưởng trung bình
- $R_k$: phần thưởng tại bước k

### Tần Suất Thăm Trạng Thái
- $\mu_\pi(s)$: tần suất thăm trạng thái s
- $\sum_s \mu_\pi(s) = 1$
- Phần thưởng trung bình = tổng có trọng số

## Phần Thưởng Vi Phân

### Định Nghĩa
$$G_t = R_{t+1} - R_\pi + R_{t+2} - R_\pi + ...$$
- Đo lường phần thưởng vượt trội
- So sánh với phần thưởng trung bình
- Cho phép so sánh hành động

## Hàm Giá Trị Vi Phân

### Định Nghĩa
$$v_\pi(s) = \mathbb{E}_\pi[G_t|S_t=s]$$
- Giá trị kỳ vọng của phần thưởng vi phân
- Phương trình Bellman tương ứng
- Cơ sở cho thuật toán học

## Thuật Toán Sarsa Vi Phân

### Khác Biệt với Sarsa Thông Thường
- Theo dõi phần thưởng trung bình
- Cập nhật dựa trên phần thưởng vi phân
- Không cần hệ số chiết khấu

### Cập Nhật
- Cập nhật phần thưởng trung bình
- Cập nhật giá trị hành động
- Cập nhật chính sách

## Kết Luận
Phần thưởng trung bình cung cấp cách tiếp cận mới và hiệu quả cho bài toán điều khiển, đặc biệt phù hợp với các bài toán cần tối ưu hóa hiệu suất dài hạn.
