# Các Công Thức Quan Trọng Trong TD Learning

## 1. Tổng Quan
Temporal Difference (TD) learning sử dụng các công thức cập nhật giá trị trạng thái hoặc giá trị hành động dựa trên sự khác biệt tạm thời (TD error). Dưới đây là các công thức quan trọng nhất trong TD learning.

## 2. Công Thức TD Error

### 2.1. TD Error Cho Hàm Giá Trị Trạng Thái
$$
\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)
$$
- $\delta_t$: TD error tại thời điểm $t$
- $R_{t+1}$: Phần thưởng nhận được sau khi thực hiện hành động tại $S_t$
- $\gamma$: Hệ số chiết khấu
- $V(S_{t+1})$: Giá trị ước tính của trạng thái tiếp theo
- $V(S_t)$: Giá trị ước tính của trạng thái hiện tại

### 2.2. TD Error Cho Hàm Giá Trị Hành Động (Q-learning, Sarsa)
$$
\delta_t = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)
$$
- $Q(S_t, A_t)$: Giá trị hành động tại thời điểm $t$
- $Q(S_{t+1}, A_{t+1})$: Giá trị hành động tiếp theo

## 3. Công Thức Cập Nhật Giá Trị

### 3.1. Cập Nhật Hàm Giá Trị Trạng Thái
$$
V(S_t) \leftarrow V(S_t) + \alpha \delta_t
$$
- $\alpha$: Tốc độ học

### 3.2. Cập Nhật Hàm Giá Trị Hành Động (Q-learning)
$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a') - Q(S_t, A_t)]
$$

### 3.3. Cập Nhật Hàm Giá Trị Hành Động (Sarsa)
$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha [R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]
$$

## 4. Ý Nghĩa Các Tham Số
- $\alpha$: Tốc độ học (learning rate)
- $\gamma$: Hệ số chiết khấu (discount factor)
- $R_{t+1}$: Phần thưởng nhận được
- $S_t, S_{t+1}$: Trạng thái hiện tại và tiếp theo
- $A_t, A_{t+1}$: Hành động hiện tại và tiếp theo

## 5. Kết Luận
Các công thức trên là nền tảng cho các thuật toán TD learning như TD(0), Sarsa, Q-learning. Việc hiểu rõ và áp dụng đúng các công thức này giúp tối ưu hóa quá trình học tăng cường. 