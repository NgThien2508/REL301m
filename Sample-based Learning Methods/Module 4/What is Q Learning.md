# Q-Learning Là Gì?

## 1. Tổng Quan
Q-learning là một thuật toán học tăng cường (reinforcement learning) không cần mô hình (model-free), giúp agent học cách tối ưu hóa hành động trong môi trường để tối đa hóa phần thưởng tích lũy.

## 2. Nguyên Lý Hoạt Động
- Agent quan sát trạng thái hiện tại $S_t$
- Chọn hành động $A_t$ dựa trên chính sách (thường là epsilon-greedy)
- Nhận phần thưởng $R_{t+1}$ và chuyển sang trạng thái mới $S_{t+1}$
- Cập nhật giá trị Q theo công thức:

$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t)]
$$

Trong đó:
- $\alpha$: Tốc độ học (learning rate)
- $\gamma$: Hệ số chiết khấu (discount factor)
- $\max_{a'} Q(S_{t+1}, a')$: Giá trị Q lớn nhất ở trạng thái tiếp theo

## 3. Đặc Điểm Nổi Bật
- Không cần biết trước mô hình môi trường
- Học từ trải nghiệm thực tế
- Có thể áp dụng cho môi trường rời rạc hoặc liên tục (sau khi rời rạc hóa)
- Là thuật toán off-policy

## 4. Quy Trình Thuật Toán
1. Khởi tạo bảng Q với giá trị tùy ý
2. Lặp lại cho đến khi hội tụ:
   - Quan sát trạng thái hiện tại $S_t$
   - Chọn hành động $A_t$ (theo epsilon-greedy)
   - Thực hiện hành động, nhận $R_{t+1}$ và $S_{t+1}$
   - Cập nhật $Q(S_t, A_t)$ theo công thức trên
   - Chuyển sang trạng thái mới

## 5. Ví Dụ Minh Họa
### 5.1. Trò Chơi Đường Đi (Gridworld)
- Agent di chuyển trên lưới để tìm đường về đích
- Mỗi bước đi nhận phần thưởng âm, về đích nhận phần thưởng dương
- Q-learning giúp agent học đường đi ngắn nhất

### 5.2. Robot Học Di Chuyển
- Robot học cách tránh vật cản và tối ưu hóa đường đi
- Không cần biết trước bản đồ môi trường

## 6. Ưu Điểm và Hạn Chế
### 6.1. Ưu Điểm
- Đơn giản, dễ triển khai
- Không cần mô hình môi trường
- Hiệu quả với nhiều loại bài toán

### 6.2. Hạn Chế
- Chậm hội tụ với không gian trạng thái lớn
- Cần nhiều bộ nhớ nếu trạng thái/hành động nhiều
- Có thể không tối ưu nếu epsilon không được điều chỉnh hợp lý

## 7. Kết Luận
Q-learning là một trong những thuật toán nền tảng của học tăng cường, giúp agent học tối ưu hóa hành động thông qua trải nghiệm mà không cần biết trước động học môi trường.
