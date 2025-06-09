# Tại Sao Q-learning Là Off-Policy?

## 1. Tổng Quan
Q-learning là một thuật toán học tăng cường off-policy, nghĩa là quá trình cập nhật giá trị không phụ thuộc vào chính sách mà agent đang thực hiện khi thu thập dữ liệu.

## 2. Định Nghĩa Off-Policy
- **Off-policy**: Học giá trị tối ưu dựa trên một chính sách khác với chính sách đang được sử dụng để tương tác với môi trường.
- Chính sách hành động (behavior policy) có thể khác với chính sách mục tiêu (target policy).

## 3. Cơ Chế Cập Nhật Trong Q-learning
- Q-learning cập nhật giá trị Q dựa trên hành động tối ưu ở trạng thái tiếp theo, bất kể agent thực tế chọn hành động nào.
- Công thức cập nhật:

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t)]
$$

- $\max_{a'} Q(S_{t+1}, a')$ là hành động tốt nhất theo chính sách mục tiêu (greedy), không nhất thiết là hành động agent vừa thực hiện.

## 4. Ví Dụ Minh Họa
### 4.1. Trò Chơi Đường Đi
- Agent di chuyển ngẫu nhiên (exploration) nhưng cập nhật Q dựa trên hành động tốt nhất ở trạng thái tiếp theo.
- Nhờ đó, agent có thể học chính sách tối ưu dù không luôn chọn hành động tối ưu khi tương tác.

### 4.2. So Sánh Với Sarsa (On-policy)
- Sarsa cập nhật Q dựa trên chính hành động agent thực hiện ở trạng thái tiếp theo (on-policy).
- Q-learning cập nhật Q dựa trên hành động tối ưu (off-policy).

## 5. Ưu Điểm Của Off-Policy
- Cho phép học chính sách tối ưu trong khi vẫn khám phá môi trường
- Linh hoạt hơn trong việc thu thập dữ liệu
- Có thể sử dụng dữ liệu từ nhiều nguồn khác nhau

## 6. Kết Luận
Q-learning là off-policy vì nó cập nhật giá trị dựa trên chính sách tối ưu (greedy), không phụ thuộc vào chính sách hành động thực tế của agent. Điều này giúp Q-learning học hiệu quả hơn trong nhiều tình huống thực tế.
