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

#### A. Trạng thái (State)
**Định nghĩa:** Trạng thái là mức năng lượng pin của robot
```
S = {low, high}
```

**Giải thích:**
- `high`: Pin đầy, robot hoạt động tốt
- `low`: Pin yếu, cần cân nhắc sạc
- Chỉ có 2 trạng thái để đơn giản hóa bài toán

#### B. Hành động (Action)
**Khi pin cao (high):**
```
A(high) = {search, wait}
```
- `search`: Chủ động tìm kiếm lon
- `wait`: Đứng yên chờ lon được mang đến

**Khi pin thấp (low):**
```
A(low) = {search, wait, recharge}
```
- Có thêm lựa chọn `recharge`: Đi sạc pin
- Không cho phép sạc khi pin cao (vì không cần thiết)

#### C. Phần thưởng (Reward)
```
r_search = +10  // Tìm được lon
r_wait = +1    // Chờ đợi
r_rescued = -20 // Bị hết pin
```

**Ý nghĩa:**
- Khuyến khích tìm lon (+10)
- Chấp nhận chờ đợi (+1)
- Phạt nặng việc hết pin (-20)

### 1.3. Động lực Hệ thống (Chi tiết)

#### A. Từ Trạng thái Pin Cao (High)

1. **Hành động Tìm kiếm (Search):**
   ```
   P(high|high,search) = α        // Xác suất giữ pin cao
   P(low|high,search) = 1-α      // Xác suất pin giảm
   R(high,search) = +10          // Phần thưởng
   ```
   
   *Giải thích:*
   - α là xác suất pin vẫn cao sau khi tìm kiếm
   - (1-α) là xác suất pin giảm xuống thấp
   - Luôn nhận được +10 điểm nếu tìm thấy lon

2. **Hành động Chờ đợi (Wait):**
   ```
   P(high|high,wait) = 1.0       // Chắc chắn giữ pin cao
   R(high,wait) = +1             // Phần thưởng nhỏ
   ```

#### B. Từ Trạng thái Pin Thấp (Low)

1. **Hành động Tìm kiếm (Search):**
   ```
   P(low|low,search) = β         // Xác suất tiếp tục hoạt động
   P(high|low,search) = 1-β      // Xác suất cần cứu hộ
   R(low,search) = +10 hoặc -20  // Phần thưởng phụ thuộc kết quả
   ```

2. **Hành động Chờ đợi (Wait):**
   ```
   P(low|low,wait) = 1.0         // Giữ nguyên trạng thái
   R(low,wait) = +1              // Phần thưởng nhỏ
   ```

3. **Hành động Sạc pin (Recharge):**
   ```
   P(high|low,recharge) = 1.0    // Chắc chắn pin sẽ đầy
   R(low,recharge) = 0           // Không có phần thưởng
   ```

### 1.4. Chiến lược Tối ưu

**Khi pin cao:**
- Nên tìm kiếm nếu α cao (pin ít khi giảm)
- Nên chờ đợi nếu α thấp (pin dễ giảm)

**Khi pin thấp:**
- Nên sạc nếu β thấp (dễ hết pin)
- Có thể tìm kiếm nếu β cao (ít rủi ro)
- Chờ đợi là lựa chọn an toàn

## 2. Tính Linh Hoạt của MDP

### 2.1. Về Trạng thái (State)

**Cấp thấp (Low-level):**
```
Ví dụ: Camera theo dõi giao thông
- Giá trị pixel từ camera
- Dữ liệu cảm biến thô
- Tín hiệu radar
```

**Cấp cao (High-level):**
```
Ví dụ: Hệ thống quản lý kho
- Số lượng hàng trong kho
- Trạng thái đơn hàng
- Vị trí sản phẩm
```

### 2.2. Về Hành động (Action)

**Cấp thấp:**
```
Ví dụ: Robot công nghiệp
- Điện áp động cơ: 5V, 12V
- Góc quay servo: 30°, 45°
- Tốc độ băng chuyền: 1m/s
```

**Cấp cao:**
```
Ví dụ: Hệ thống tự động hóa
- "Di chuyển đến vị trí A"
- "Nhặt sản phẩm"
- "Tối ưu hóa lộ trình"
```

### 2.3. Về Thời gian

**Thời gian rời rạc:**
```
Ví dụ 1: Robot nhà máy
- Mỗi 100ms cập nhật một lần
- Theo chu kỳ sản xuất
- Theo ca làm việc

Ví dụ 2: Giao dịch chứng khoán
- Mỗi phiên giao dịch
- Mỗi ngày/tuần
- Theo quý
```

## 3. Ví dụ Thực tế: Robot Gắp và Đặt

### 3.1. Phân tích Chi tiết

**Trạng thái (State):**
```python
state = {
    'joint_angles': [θ1, θ2, θ3],    # Góc các khớp
    'joint_velocities': [ω1, ω2, ω3], # Vận tốc góc
    'gripper_state': 0/1,            # Trạng thái kẹp
    'object_position': [x, y, z]      # Vị trí đối tượng
}
```

**Hành động (Action):**
```python
action = {
    'motor_voltages': [V1, V2, V3],  # Điện áp động cơ
    'gripper_command': 'open/close'   # Điều khiển kẹp
}
```

**Phần thưởng (Reward):**
```python
reward = {
    'success': +100,          # Đặt thành công
    'energy': -1 * energy_used, # Tiêu thụ năng lượng
    'drop': -50,              # Làm rơi vật
    'collision': -30          # Va chạm
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


