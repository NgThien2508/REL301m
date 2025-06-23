# Tổng quan về Expected Sarsa và Q-learning với Function Approximation

Bài viết này đề cập đến Expected Sarsa và Q-learning khi sử dụng phương pháp xấp xỉ hàm (function approximation) trong học tăng cường, đồng thời làm rõ mối liên hệ giữa hai thuật toán này.

## Expected Sarsa với Function Approximation

- Expected Sarsa cập nhật vector trọng số dựa trên giá trị kỳ vọng của các hành động ở trạng thái tiếp theo, thay vì chỉ dựa vào một hành động được chọn ngẫu nhiên.
- Kỳ vọng này được tính bằng cách lấy tổng các giá trị hành động, mỗi giá trị được nhân với xác suất chọn hành động đó theo chính sách mục tiêu.

**Công thức cập nhật:**
$$
W \leftarrow W + \alpha \left( R + \gamma \sum_{a} \pi(a|s') Q(s', a; W) - Q(s, a; W) \right)
$$

Trong đó:
- $W$: vector trọng số của bộ xấp xỉ hàm.
- $\alpha$: hệ số học.
- $R$: phần thưởng nhận được.
- $\gamma$: hệ số chiết khấu.
- $s'$: trạng thái tiếp theo.
- $\pi(a|s')$: xác suất chọn hành động $a$ ở trạng thái $s'$ theo chính sách mục tiêu.
- $Q(s', a; W)$: giá trị hành động ước lượng với trọng số $W$.

## Q-learning với Function Approximation

- Q-learning có thể xem là một trường hợp riêng của Expected Sarsa, khi chính sách mục tiêu là greedy với các giá trị hành động xấp xỉ.
- Công thức cập nhật của Q-learning sử dụng giá trị lớn nhất trong các hành động ở trạng thái tiếp theo thay vì kỳ vọng:

$$
W \leftarrow W + \alpha \left( R + \gamma \max_{a} Q(s', a; W) - Q(s, a; W) \right)
$$

## Từ Sarsa đến Expected Sarsa

- Việc cập nhật trong Sarsa với function approximation tương tự như dạng bảng, sử dụng gradient và hệ số học.
- Expected Sarsa mở rộng bằng cách tính giá trị cho mọi hành động ở trạng thái tiếp theo dựa trên vector trọng số.

## Kết luận

- Expected Sarsa và Q-learning với function approximation giúp mở rộng các thuật toán TD control cho các không gian trạng thái lớn hoặc liên tục.
- Điểm khác biệt chính là Expected Sarsa dùng kỳ vọng theo chính sách, còn Q-learning dùng giá trị lớn nhất để cập nhật. 