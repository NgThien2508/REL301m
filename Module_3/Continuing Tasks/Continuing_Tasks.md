# Nhiệm Vụ Liên Tục Trong Reinforcement Learning

## 1. Giới Thiệu về Nhiệm Vụ Liên Tục
Trong Reinforcement Learning, nhiệm vụ liên tục (Continuing Tasks) là những tác vụ không có điểm kết thúc tự nhiên, trong đó agent phải tương tác với môi trường một cách liên tục và không ngừng. Đây là mô hình phù hợp cho nhiều ứng dụng thực tế trong cuộc sống.

### 1.1. Đặc Điểm Chính
- Không có trạng thái kết thúc xác định
- Tương tác agent-môi trường diễn ra vô hạn
- Cần cơ chế đặc biệt để xử lý phần thưởng tích lũy

### 1.2. Ứng Dụng Điển Hình
- Quản lý danh mục đầu tư
- Điều khiển robot trong nhà máy
- Hệ thống điều khiển quá trình công nghiệp
- Quản lý tài nguyên máy chủ

## 2. Phân Biệt Các Loại Nhiệm Vụ

### 2.1. Nhiệm Vụ Theo Tập (Episodic Tasks)
#### Đặc trưng:
- Có điểm bắt đầu và kết thúc rõ ràng
- Độ dài hữu hạn
- Return có thể tính trực tiếp

#### Ví dụ minh họa:
1. **Game Super Mario**
   - Bắt đầu: Mario ở vị trí xuất phát
   - Kết thúc: Qua màn/Game over
   - Return: Tổng điểm thu được

2. **Cờ vua**
   - Bắt đầu: Vị trí chuẩn
   - Kết thúc: Thắng/Thua/Hòa
   - Return: +1/-1/0

### 2.2. Nhiệm Vụ Liên Tục (Continuing Tasks)
#### Đặc trưng:
- Không có điểm kết thúc tự nhiên
- Độ dài vô hạn
- Cần chiết khấu để tính Return

#### Ví dụ minh họa:
1. **Hệ thống giao thông thông minh**
   - State: Mật độ xe, thời gian
   - Action: Điều chỉnh đèn tín hiệu
   - Reward: -1 × (thời gian chờ trung bình)

2. **Quản lý năng lượng tòa nhà**
   - State: Nhiệt độ, độ ẩm, lượng người
   - Action: Điều chỉnh HVAC
   - Reward: -(chi phí năng lượng + độ không thoải mái)

## 3. Chiết Khấu Trong Nhiệm Vụ Liên Tục

### 3.1. Tại Sao Cần Chiết Khấu?
1. **Vấn đề toán học**:
   - Tổng phần thưởng có thể phát tán
   - Khó so sánh các chuỗi vô hạn
   - Cần giới hạn giá trị Return

2. **Ý nghĩa thực tế**:
   - Phần thưởng tương lai kém chắc chắn
   - Ưu tiên phần thưởng gần hơn
   - Phản ánh chi phí cơ hội

### 3.2. Công Thức Chiết Khấu
#### Return với chiết khấu:
$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ...$$

Trong đó:
- $G_t$: Return tại thời điểm t
- $R_t$: Phần thưởng tức thời
- $\gamma$: Hệ số chiết khấu (0 ≤ γ < 1)

#### Dạng đệ quy:
$$G_t = R_{t+1} + \gamma G_{t+1}$$

### 3.3. Ảnh Hưởng của γ
#### γ ≈ 0: "Cận thị"
- Chỉ quan tâm phần thưởng tức thời
- Bỏ qua hậu quả dài hạn
- Thích hợp cho nhiệm vụ đơn giản

#### γ ≈ 1: "Viễn thị"
- Coi trọng phần thưởng tương lai
- Học các chiến lược phức tạp
- Rủi ro mất ổn định số học

## 4. Ví Dụ Chi Tiết: Hệ Thống Giao Dịch Tự Động

### 4.1. Mô Tả Hệ Thống
#### State Space:
- Giá cổ phiếu hiện tại
- Khối lượng giao dịch
- Chỉ số thị trường
- Dữ liệu kinh tế vĩ mô

#### Action Space:
- Mua/Bán/Giữ nguyên
- Số lượng giao dịch
- Loại lệnh (Market/Limit)

#### Reward:
- Lợi nhuận ròng sau phí
- Phạt cho rủi ro quá mức
- Thưởng cho đa dạng hóa

### 4.2. Chiến Lược Chiết Khấu
- γ = 0.95: Cân bằng ngắn-trung hạn
- Reward scale: [-1, 1] sau chuẩn hóa
- Horizon hiệu dụng ≈ 20 bước

### 4.3. Thách Thức
1. **Độ trễ phần thưởng**:
   - Kết quả giao dịch không tức thời
   - Cần credit assignment dài hạn
   - Nhiễu trong tín hiệu phần thưởng

2. **Môi trường không dừng**:
   - Thị trường luôn thay đổi
   - Cần thích nghi liên tục
   - Khó học mô hình cố định

## 5. Kỹ Thuật Triển Khai

### 5.1. Xử Lý Horizon Vô Hạn
1. **Sliding window**:
   - Chỉ xét N bước gần nhất
   - Cập nhật liên tục cửa sổ
   - Giảm độ phức tạp tính toán

2. **Bootstrapping**:
   - Ước lượng giá trị tương lai
   - Cập nhật theo TD learning
   - Giảm variance trong học tập

### 5.2. Chuẩn Hóa Phần Thưởng
1. **Min-max scaling**:
   - Map rewards về [-1, 1]
   - Giữ tỷ lệ tương đối
   - Ổn định học tập

2. **Z-score normalization**:
   - Chuẩn hóa theo phân phối
   - Xử lý outliers
   - Thích nghi với scale thay đổi

## 6. Kết Luận
Nhiệm vụ liên tục đòi hỏi:
- Thiết kế phần thưởng hợp lý
- Lựa chọn γ phù hợp
- Xử lý vấn đề horizon vô hạn
- Cân bằng ngắn-dài hạn

-------------------------------------------
##### Cập nhật: 5-27-2025 lúc 8PM
##### Khóa học: Fundamentals of Reinforcement Learning - Module 3
##### Tài liệu: Continuing Tasks
##### Học nội dung từ clip: Continuing Tasks
