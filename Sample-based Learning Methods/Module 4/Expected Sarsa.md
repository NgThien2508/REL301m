# Expected Sarsa Là Gì?

## 1. Tổng Quan
Expected Sarsa là một biến thể của thuật toán Sarsa trong học tăng cường, kết hợp giữa tính chất on-policy và việc sử dụng kỳ vọng toán học để cập nhật giá trị Q.

## 2. Nguyên Lý Hoạt Động
- Agent quan sát trạng thái hiện tại $S_t$
- Chọn hành động $A_t$ theo chính sách (thường là epsilon-greedy)
- Thực hiện hành động, nhận phần thưởng $R_{t+1}$ và trạng thái mới $S_{t+1}$
- Tính giá trị kỳ vọng của Q ở trạng thái tiếp theo dựa trên chính sách hiện tại
- Cập nhật giá trị Q theo công thức:

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \mathbb{E}_{a'}[Q(S_{t+1}, a')] - Q(S_t, A_t)]
$$

Trong đó:
- $\mathbb{E}_{a'}[Q(S_{t+1}, a')]$: Giá trị kỳ vọng của Q ở trạng thái tiếp theo, tính theo xác suất chọn từng hành động $a'$
- $\alpha$: Tốc độ học
- $\gamma$: Hệ số chiết khấu

## 3. So Sánh Với Sarsa và Q-learning
- **Sarsa**: Cập nhật Q dựa trên hành động thực tế agent chọn ở trạng thái tiếp theo (on-policy)
- **Q-learning**: Cập nhật Q dựa trên hành động tối ưu ở trạng thái tiếp theo (off-policy)
- **Expected Sarsa**: Cập nhật Q dựa trên giá trị kỳ vọng của tất cả hành động ở trạng thái tiếp theo (on-policy, giảm phương sai)

## 4. Ưu Điểm Của Expected Sarsa
- Giảm phương sai so với Sarsa truyền thống
- Ổn định hơn khi học
- Kết hợp ưu điểm của Sarsa và Q-learning
- Phù hợp với các môi trường có nhiều hành động khả dĩ

## 5. Ví Dụ Minh Họa
### 5.1. Trò Chơi Đường Đi
- Agent tính toán kỳ vọng phần thưởng ở trạng thái tiếp theo dựa trên xác suất chọn từng hành động
- Cập nhật Q-value dựa trên giá trị trung bình thay vì chỉ một hành động cụ thể

## 6. Kết Luận
Expected Sarsa là một thuật toán mạnh mẽ, giúp cân bằng giữa tính ổn định và hiệu quả trong học tăng cường, đặc biệt hữu ích khi môi trường có nhiều lựa chọn hành động.
