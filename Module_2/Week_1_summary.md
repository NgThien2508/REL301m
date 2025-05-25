# Tổng kết Tuần 1: K-Armed Bandits và Các Khái niệm Cơ bản

## 1. Vấn đề K-Armed Bandit

### 1.1 Định nghĩa
- **K-Armed Bandit** là một bài toán trong học tăng cường (Reinforcement Learning) trong đó:
  - Agent phải chọn giữa k hành động khác nhau
  - Mỗi hành động mang lại phần thưởng ngẫu nhiên
  - Mục tiêu là tối đa hóa tổng phần thưởng

### 1.2 Cấu trúc cơ bản
```
Agent → Chọn 1 trong k hành động → Nhận phần thưởng
Ví dụ với k = 3:
- Hành động 1: Phần thưởng trung bình thấp 😟
- Hành động 2: Phần thưởng trung bình trung bình 😐
- Hành động 3: Phần thưởng trung bình cao 😊
```

## 2. Giá trị Hành động (Action Values)

### 2.1 Định nghĩa toán học
- **Giá trị thực của hành động** (True Action Value):
  
  $$q_*(a) = \mathbb{E}[R_t | A_t = a], \forall a \in \{1,\ldots,k\}$$
  
  Trong đó:
  - $q_*(a)$: Giá trị thực của hành động $a$
  - $\mathbb{E}[R_t]$: Kỳ vọng phần thưởng tại thời điểm $t$
  - $A_t = a$: Khi chọn hành động $a$

### 2.2 Ước lượng giá trị
1. **Phương pháp trung bình mẫu (Sample-Average Method)**:
   
   $$Q_t(a) = \frac{\sum_{i=1}^{t-1} R_i \cdot \mathbb{1}_{A_i=a}}{\sum_{i=1}^{t-1} \mathbb{1}_{A_i=a}} = \frac{\text{Tổng phần thưởng khi chọn }a}{\text{Số lần chọn }a}$$

2. **Cập nhật gia tăng (Incremental Update)**:
   
   $$Q_{t+1}(a) = Q_t(a) + \frac{1}{N_t(a)}[R_t - Q_t(a)]$$
   
   Trong đó:
   - $Q_t(a)$: Ước lượng hiện tại
   - $R_t$: Phần thưởng mới
   - $N_t(a)$: Số lần chọn $a$
   - $[R_t - Q_t(a)]$: Sai số

## 3. Thăm dò và Khai thác (Exploration vs. Exploitation)

### 3.1 Định nghĩa
- **Thăm dò (Exploration)**: 
  - Cải thiện kiến thức cho lợi ích dài hạn
  - Thử nghiệm các hành động mới

- **Khai thác (Exploitation)**:
  - Sử dụng kiến thức hiện có cho lợi ích ngắn hạn
  - Chọn hành động tốt nhất đã biết

### 3.2 Phương pháp ε-greedy

$$A_t \leftarrow \begin{cases}
    \arg\max_a Q_t(a) & \text{với xác suất } 1-\varepsilon \\
    a \sim \text{Uniform}(\{a_1,\ldots,a_k\}) & \text{với xác suất } \varepsilon
\end{cases}$$

- $\varepsilon$: Tỷ lệ thăm dò (thường 0.1 hoặc nhỏ hơn)
- $1-\varepsilon$: Tỷ lệ khai thác
- Uniform: Chọn ngẫu nhiên đều

## 4. Giá trị Khởi tạo Lạc quan (Optimistic Initial Values)

### 4.1 Nguyên lý
- Khởi tạo $Q_1(a)$ với giá trị cao hơn $q_*(a)$
- Ví dụ: $Q_1(a) = 2.0$ cho mọi $a$
- Tạo động lực thăm dò tự nhiên

### 4.2 Ưu điểm
- Thăm dò có hệ thống ban đầu
- Tự động giảm thăm dò theo thời gian
- Không cần tham số $\varepsilon$

## 5. Phương pháp UCB (Upper-Confidence Bound)

### 5.1 Công thức

$$A_t = \arg\max_a \left[Q_t(a) + c\sqrt{\frac{\ln t}{N_t(a)}}\right]$$

Trong đó:
- $Q_t(a)$: Phần khai thác (exploit)
- $c\sqrt{\frac{\ln t}{N_t(a)}}$: Phần thăm dò (explore)
- $c$: Tham số kiểm soát mức độ thăm dò

### 5.2 Nguyên lý "Upper-Confidence Bound"
- Tự động cân bằng thăm dò và khai thác
- Ưu tiên hành động ít được thử
- Giảm thăm dò khi có nhiều thông tin

## 6. Kết luận

K-Armed Bandit là nền tảng cho các khái niệm quan trọng trong học tăng cường:
- Cân bằng thăm dò và khai thác
- Ước lượng và cập nhật giá trị
- Ra quyết định trong điều kiện không chắc chắn

-------------------------------------------
##### 8-12-2025 at 10PM.
##### Course: Fundamentals of Reinforcement Learning/Module 2.
##### Đọc tài liệu tại: Week 1 Summary
##### Học nội dung từ clip: Week 1 Summary
