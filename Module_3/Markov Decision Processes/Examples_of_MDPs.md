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

$$\mathcal{S} = \{\text{low}, \text{high}\}$$

**Giải thích:**
- $s = \text{high}$: Pin đầy, robot hoạt động tốt
- $s = \text{low}$: Pin yếu, cần cân nhắc sạc
- Chỉ có 2 trạng thái để đơn giản hóa bài toán

#### B. Hành động (Action - $\mathcal{A}$)
**Khi pin cao:**

$$\mathcal{A}(\text{high}) = \{\text{search}, \text{wait}\}$$

- $a = \text{search}$: Chủ động tìm kiếm lon
- $a = \text{wait}$: Đứng yên chờ lon được mang đến

**Khi pin thấp:**

$$\mathcal{A}(\text{low}) = \{\text{search}, \text{wait}, \text{recharge}\}$$

- Có thêm lựa chọn $a = \text{recharge}$: Đi sạc pin
- Không cho phép sạc khi pin cao (vì không cần thiết)

#### C. Phần thưởng (Reward - $\mathcal{R}$)

$$\mathcal{R}(s,a) = \begin{cases} 
+10 & \text{khi } a = \text{search} \text{ và tìm được lon} \\
+1 & \text{khi } a = \text{wait} \\
-20 & \text{khi hết pin cần cứu hộ}
\end{cases}$$

### 1.3. Động lực Hệ thống (Chi tiết)

#### A. Từ Trạng thái Pin Cao ($s = \text{high}$)

1. **Hành động Tìm kiếm ($a = \text{search}$):**

$$P(s' = \text{high} \mid s = \text{high}, a = \text{search}) = \alpha$$

$$P(s' = \text{low} \mid s = \text{high}, a = \text{search}) = 1 - \alpha$$

$$R(\text{high}, \text{search}) = +10$$

*Giải thích:*
- $\alpha$ là xác suất pin vẫn cao sau khi tìm kiếm
- $(1-\alpha)$ là xác suất pin giảm xuống thấp
- Luôn nhận được $+10$ điểm nếu tìm thấy lon

2. **Hành động Chờ đợi ($a = \text{wait}$):**

$$P(s' = \text{high} \mid s = \text{high}, a = \text{wait}) = 1.0$$

$$R(\text{high}, \text{wait}) = +1$$

#### B. Từ Trạng thái Pin Thấp ($s = \text{low}$)

1. **Hành động Tìm kiếm ($a = \text{search}$):**

$$P(s' = \text{low} \mid s = \text{low}, a = \text{search}) = \beta$$

$$P(s' = \text{high} \mid s = \text{low}, a = \text{search}) = 1 - \beta$$

$$R(\text{low}, \text{search}) = \begin{cases}
+10 & \text{nếu tiếp tục hoạt động} \\
-20 & \text{nếu hết pin}
\end{cases}$$

2. **Hành động Chờ đợi ($a = \text{wait}$):**

$$P(s' = \text{low} \mid s = \text{low}, a = \text{wait}) = 1.0$$

$$R(\text{low}, \text{wait}) = +1$$

3. **Hành động Sạc pin ($a = \text{recharge}$):**

$$P(s' = \text{high} \mid s = \text{low}, a = \text{recharge}) = 1.0$$

$$R(\text{low}, \text{recharge}) = 0$$

### 1.4. Chiến lược Tối ưu ($\pi^*$)

**Khi pin cao ($s = \text{high}$):**
- $\pi^*(\text{high}) = \text{search}$ nếu $\alpha > \frac{9}{10}$ (pin ít khi giảm)
- $\pi^*(\text{high}) = \text{wait}$ nếu $\alpha < \frac{9}{10}$ (pin dễ giảm)

**Khi pin thấp ($s = \text{low}$):**
- $\pi^*(\text{low}) = \text{recharge}$ nếu $\beta < \frac{30}{31}$ (dễ hết pin)
- $\pi^*(\text{low}) = \text{search}$ nếu $\beta > \frac{30}{31}$ (ít rủi ro)
- $\pi^*(\text{low}) = \text{wait}$ là lựa chọn an toàn

## 2. Tính Linh Hoạt của MDP

### 2.1. Về Trạng thái (State - $\mathcal{S}$)

**Cấp thấp (Low-level):**
Ví dụ: Camera theo dõi giao thông
$\mathcal{S} = \{\mathbf{x} \in \mathbb{R}^n \mid \mathbf{x} \text{ là vector pixel}\}$

**Cấp cao (High-level):**
Ví dụ: Hệ thống quản lý kho
$\mathcal{S} = \{(q,l,p) \mid q \in \mathbb{N}, l \in \mathbb{R}^3, p \in \{0,1\}\}$

### 2.2. Về Hành động (Action - $\mathcal{A}$)

**Cấp thấp:**
Ví dụ: Robot công nghiệp
$\mathcal{A} = \{(\mathbf{v}, \boldsymbol{\theta}, \boldsymbol{\omega}) \mid \mathbf{v} \in \mathbb{R}^3, \boldsymbol{\theta} \in [-\pi,\pi]^3, \boldsymbol{\omega} \in \mathbb{R}^3\}$

**Cấp cao:**
Ví dụ: Hệ thống tự động hóa
$\mathcal{A} = \{\text{"Di chuyển"}, \text{"Nhặt"}, \text{"Tối ưu"}\}$

### 2.3. Về Thời gian ($t$)

**Thời gian rời rạc:**
$t \in \{0, \Delta t, 2\Delta t, \ldots\}$ với $\Delta t$ là chu kỳ cập nhật

Ví dụ 1: Robot nhà máy
$\Delta t = 100\text{ ms}$

Ví dụ 2: Giao dịch chứng khoán
$\Delta t = 1\text{ ngày}$

## 3. Ví dụ Thực tế: Robot Gắp và Đặt

### 3.1. Phân tích Chi tiết

**Trạng thái (State):**
```python
# Định nghĩa không gian trạng thái
# S = {(θ, ω, g, p) | θ, ω ∈ ℝ³, g ∈ {0,1}, p ∈ ℝ³}

state = {
    'joint_angles': [θ₁, θ₂, θ₃],         # Góc các khớp
    'joint_velocities': [ω₁, ω₂, ω₃],      # Vận tốc góc
    'gripper_state': 'g ∈ {0,1}',          # Trạng thái kẹp
    'object_position': '(x, y, z)'         # Vị trí đối tượng
}
```

Trong đó:
$\mathcal{S} = \{(\boldsymbol{\theta}, \boldsymbol{\omega}, g, \mathbf{p}) \mid \boldsymbol{\theta}, \boldsymbol{\omega} \in \mathbb{R}^3, g \in \{0,1\}, \mathbf{p} \in \mathbb{R}^3\}$

**Hành động (Action):**
```python
# Định nghĩa không gian hành động
# A = {(V, cmd) | V ∈ ℝ³, cmd ∈ {"open", "close"}}

action = {
    'motor_voltages': [V₁, V₂, V₃],        # Điện áp động cơ
    'gripper_command': 'open/close'         # Điều khiển kẹp
}
```

Trong đó:
$\mathcal{A} = \{(\mathbf{V}, \text{cmd}) \mid \mathbf{V} \in \mathbb{R}^3, \text{cmd} \in \{\text{"open"}, \text{"close"}\}\}$

**Phần thưởng (Reward):**
```python
# Định nghĩa hàm phần thưởng
# R(s,a,s') = +100 (thành công), -E(a) (năng lượng), -50 (rơi), -30 (va chạm)

reward = {
    'success': +100,        # Đặt thành công
    'energy': '-E(a)',      # Chi phí năng lượng
    'drop': -50,           # Làm rơi vật
    'collision': -30       # Va chạm
}
```

Trong đó:
$\mathcal{R}(s,a,s') = \begin{cases}
+100 & \text{khi đặt thành công} \\
-E(a) & \text{chi phí năng lượng} \\
-50 & \text{khi làm rơi vật} \\
-30 & \text{khi va chạm}
\end{cases}$

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


