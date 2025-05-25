# Ví dụ về Quy trình Quyết định Markov (Examples of MDPs)

## 1. Ví dụ Robot Tái chế (Recycling Robot)

### 1.1. Giới thiệu Bài toán
Robot tái chế là một ví dụ điển hình về MDP, giúp chúng ta hiểu cách áp dụng lý thuyết vào thực tế.

**Tình huống thực tế:**
- Robot hoạt động trong văn phòng
- Thu gom lon nước ngọt để tái chế
- Sử dụng pin sạc được
- Cần cân bằng giữa nhiệm vụ và năng lượng

### 1.2. Phân tích Thành phần MDP

#### A. Trạng thái (State - $\mathcal{S}$)
**Định nghĩa:** Trạng thái là mức năng lượng pin của robot

$\mathcal{S} = \{low, high\}$

**Giải thích:**
- $s = high$: Pin đầy, robot hoạt động tốt
- $s = low$: Pin yếu, cần cân nhắc sạc
- Chỉ có 2 trạng thái để đơn giản hóa bài toán

#### B. Hành động (Action - $\mathcal{A}$)
**Khi pin cao:**

$\mathcal{A}(high) = \{search, wait\}$

- $a = search$: Chủ động tìm kiếm lon
- $a = wait$: Đứng yên chờ lon được mang đến

**Khi pin thấp:**

$\mathcal{A}(low) = \{search, wait, recharge\}$

- Có thêm lựa chọn $a = recharge$: Đi sạc pin
- Không cho phép sạc khi pin cao (vì không cần thiết)

#### C. Phần thưởng (Reward - $\mathcal{R}$)

$\mathcal{R}(s,a) = \begin{cases} 
+10 & \text{khi } a = search \text{ và tìm được lon} \\
+1 & \text{khi } a = wait \\
-20 & \text{khi hết pin cần cứu hộ}
\end{cases}$

### 1.3. Động lực Hệ thống (Chi tiết)

#### A. Từ Trạng thái Pin Cao ($s = high$)

1. **Hành động Tìm kiếm ($a = search$):**

$P(s'=high|s=high,a=search) = \alpha$ 

$P(s'=low|s=high,a=search) = 1-\alpha$

$R(high,search) = +10$

*Giải thích:*
- $\alpha$ là xác suất pin vẫn cao sau khi tìm kiếm
- $(1-\alpha)$ là xác suất pin giảm xuống thấp
- Luôn nhận được $+10$ điểm nếu tìm thấy lon

2. **Hành động Chờ đợi ($a = wait$):**

$P(s'=high|s=high,a=wait) = 1.0$

$R(high,wait) = +1$

#### B. Từ Trạng thái Pin Thấp ($s = low$)

1. **Hành động Tìm kiếm ($a = search$):**

$P(s'=low|s=low,a=search) = \beta$

$P(s'=high|s=low,a=search) = 1-\beta$

$R(low,search) = \begin{cases}
+10 & \text{nếu tiếp tục hoạt động} \\
-20 & \text{nếu hết pin}
\end{cases}$

2. **Hành động Chờ đợi ($a = wait$):**

$P(s'=low|s=low,a=wait) = 1.0$

$R(low,wait) = +1$

3. **Hành động Sạc pin ($a = recharge$):**

$P(s'=high|s=low,a=recharge) = 1.0$

$R(low,recharge) = 0$

### 1.4. Chiến lược Tối ưu ($\pi^*$)

**Khi pin cao ($s = high$):**
- $\pi^*(high) = search$ nếu $\alpha > \frac{9}{10}$ (pin ít khi giảm)
- $\pi^*(high) = wait$ nếu $\alpha < \frac{9}{10}$ (pin dễ giảm)

**Khi pin thấp ($s = low$):**
- $\pi^*(low) = recharge$ nếu $\beta < \frac{30}{31}$ (dễ hết pin)
- $\pi^*(low) = search$ nếu $\beta > \frac{30}{31}$ (ít rủi ro)
- $\pi^*(low) = wait$ là lựa chọn an toàn

## 2. Tính Linh Hoạt của MDP

### 2.1. Về Trạng thái (State - $\mathcal{S}$)

**Cấp thấp (Low-level):**
```
Ví dụ: Camera theo dõi giao thông
$\mathcal{S} = \{x \in \mathbb{R}^n | x \text{ là vector pixel}\}$
```

**Cấp cao (High-level):**
```
Ví dụ: Hệ thống quản lý kho
$\mathcal{S} = \{(q,l,p) | q \text{ là số lượng}, l \text{ là vị trí}, p \text{ là trạng thái}\}$
```

### 2.2. Về Hành động (Action - $\mathcal{A}$)

**Cấp thấp:**
```
Ví dụ: Robot công nghiệp
$\mathcal{A} = \{(v,\theta,\omega) | v \text{ là điện áp}, \theta \text{ là góc}, \omega \text{ là tốc độ}\}$
```

**Cấp cao:**
```
Ví dụ: Hệ thống tự động hóa
$\mathcal{A} = \{\text{"Di chuyển"}, \text{"Nhặt"}, \text{"Tối ưu"}\}$
```

### 2.3. Về Thời gian ($t$)

**Thời gian rời rạc:**
```
$t \in \{0, \Delta t, 2\Delta t, ...\}$ với $\Delta t$ là chu kỳ cập nhật

Ví dụ 1: Robot nhà máy
$\Delta t = 100ms$

Ví dụ 2: Giao dịch chứng khoán
$\Delta t = 1 \text{ ngày}$
```

## 3. Ví dụ Thực tế: Robot Gắp và Đặt

### 3.1. Phân tích Chi tiết

**Trạng thái (State):**
```python
$\mathcal{S} = \{(θ, ω, g, p) | θ \in \mathbb{R}^3, ω \in \mathbb{R}^3, g \in \{0,1\}, p \in \mathbb{R}^3\}$

state = {
    'joint_angles': $[θ_1, θ_2, θ_3]$,    # Góc các khớp
    'joint_velocities': $[ω_1, ω_2, ω_3]$, # Vận tốc góc
    'gripper_state': $g \in \{0,1\}$,      # Trạng thái kẹp
    'object_position': $(x, y, z)$         # Vị trí đối tượng
}
```

**Hành động (Action):**
```python
$\mathcal{A} = \{(V, cmd) | V \in \mathbb{R}^3, cmd \in \{\text{"open"}, \text{"close"}\}\}$

action = {
    'motor_voltages': $[V_1, V_2, V_3]$,  # Điện áp động cơ
    'gripper_command': 'open/close'        # Điều khiển kẹp
}
```

**Phần thưởng (Reward):**
```python
$\mathcal{R}(s,a,s') = \begin{cases}
+100 & \text{đặt thành công} \\
-E(a) & \text{năng lượng tiêu thụ} \\
-50 & \text{làm rơi vật} \\
-30 & \text{va chạm}
\end{cases}$

reward = {
    'success': +100,
    'energy': $-1 \times E(a)$,
    'drop': -50,
    'collision': -30
}
```

### 3.2. Ứng dụng Thực tế

1. **Trong Sản xuất:**
   - Lắp ráp linh kiện
   - Đóng gói sản phẩm
   - Kiểm tra chất lượng

2. **Trong Logistics:**
   - Sắp xếp hàng hóa
   - Quản lý kho tự động
   - Vận chuyển vật liệu

## 4. Kết luận và Ứng dụng

### 4.1. Ưu điểm của MDP
- Mô hình hóa được nhiều bài toán thực tế
- Linh hoạt trong việc định nghĩa các thành phần
- Có thể điều chỉnh độ chi tiết của mô hình
- Cân bằng được nhiều mục tiêu khác nhau

### 4.2. Lưu ý Khi Áp dụng
- Cần xác định rõ mục tiêu bài toán
- Chọn mức độ chi tiết phù hợp
- Cân nhắc khả năng tính toán
- Đảm bảo tính khả thi trong thực tế

----------------------------------------------------------------------------------------------------------------------------                                                                                                                                    
  ##### 5-20-2025 at 10AM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 3.
  ##### Đọc tài liệu tại: Introduction to Markov Decision Processes.
  ##### Học nội dung từ clip: Introduction to Markov Decision Processes/Markov Decision Processes.


