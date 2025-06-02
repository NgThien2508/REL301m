# Mục Tiêu của Reinforcement Learning (RL)

## 1. Giới thiệu
Trong Reinforcement Learning (Học tăng cường), mục tiêu chính của agent (tác tử) là tối đa hóa phần thưởng (reward) trong tương lai. Điều này phức tạp hơn nhiều so với việc chỉ đơn thuần tối đa hóa phần thưởng tức thời.

## 2. Tại sao không chỉ tối đa hóa phần thưởng tức thời?
- Trong môi trường MDP (Markov Decision Process), một hành động có thể:
  - Mang lại phần thưởng lớn trong ngắn hạn
  - Nhưng dẫn đến trạng thái có phần thưởng thấp trong dài hạn
- Ví dụ: Robot học đi
  - Phần thưởng tỷ lệ thuận với chuyển động tiến về phía trước
  - Nếu chỉ tối đa hóa phần thưởng tức thời: Robot sẽ lao nhanh về phía trước và ngã
  - Nếu tối đa hóa tổng phần thưởng: Robot sẽ học cách đi nhanh nhưng cẩn thận

## 3. Định nghĩa chính thức về Return
### Return (Phần thưởng tích lũy)
- Ký hiệu: G_t (G tại thời điểm t)
- Định nghĩa: Tổng của các phần thưởng nhận được sau thời điểm t
- Đặc điểm:
  - Là một biến ngẫu nhiên
  - Phụ thuộc vào tính ngẫu nhiên của:
    + Chuyển trạng thái trong môi trường
    + Phần thưởng nhận được

### Expected Return (Kỳ vọng phần thưởng)
- Agent cần tối đa hóa expected return thay vì return đơn thuần
- Tổng phần thưởng phải hữu hạn
- Có thời điểm kết thúc T xác định

## 4. Episodic Tasks (Tác vụ theo tập)
### Đặc điểm:
- Tương tác agent-môi trường được chia thành các episode độc lập
- Mỗi episode:
  - Bắt đầu độc lập với episode trước
  - Kết thúc tại trạng thái terminal
  - Agent được reset về trạng thái khởi đầu

### Ví dụ: Trò chơi cờ vua
- Một ván cờ = một episode
- Điều kiện kết thúc:
  - Chiếu hết
  - Hòa cờ
  - Đầu hàng
- Mỗi ván đều bắt đầu với cùng vị trí quân cờ ban đầu

## 5. Tổng kết
1. Mục tiêu của agent trong RL là tối đa hóa expected return
2. Return là tổng phần thưởng tích lũy, là biến ngẫu nhiên
3. Episodic tasks chia tương tác thành các episode độc lập
4. Mỗi episode có điểm bắt đầu và kết thúc rõ ràng

## 6. Ví dụ chi tiết

### 6.1. Ví dụ về Robot học đi (Continuous Task)
#### Môi trường:
- **State (Trạng thái)**: 
  - Vị trí các khớp chân
  - Tốc độ di chuyển
  - Góc nghiêng của thân
  - Áp lực lên mỗi chân

#### Hành động:
- Điều chỉnh góc các khớp
- Tăng/giảm lực ở mỗi chân

#### Phần thưởng:
- +1 cho mỗi mét di chuyển về phía trước
- -1 khi ngã
- -0.1 cho mỗi đơn vị năng lượng tiêu thụ

#### Chiến lược tối ưu:
- Ngắn hạn: Lao nhanh về phía trước → Ngã → Phần thưởng âm lớn
- Dài hạn: Di chuyển ổn định → Tích lũy phần thưởng dương đều đặn

### 6.2. Ví dụ về Game Mario (Episodic Task)
#### State:
- Vị trí Mario
- Vị trí các enemy
- Địa hình xung quanh
- Power-up đang có

#### Hành động:
- Di chuyển trái/phải
- Nhảy/Ngồi xuống
- Chạy/Đi bộ
- Sử dụng power-up

#### Phần thưởng:
- Thu thập xu: +1
- Ăn nấm: +10
- Tiêu diệt enemy: +5
- Chết: -50
- Hoàn thành màn: +100
- Thời gian còn lại: +0.1 mỗi giây

#### Chiến lược học:
1. **Giai đoạn đầu**:
   - Học cách di chuyển cơ bản
   - Tránh rơi xuống hố
   
2. **Giai đoạn giữa**:
   - Học cách đối phó với enemy
   - Thu thập power-up
   
3. **Giai đoạn cao cấp**:
   - Tối ưu điểm số
   - Tìm đường đi nhanh nhất
   - Khám phá đường đi bí mật
