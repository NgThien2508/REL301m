# Quy trình Quyết định Markov (Markov Decision Processes - MDP)

## Phần 1: Khái niệm Cơ bản

### 1.1. Định nghĩa
Quy trình Quyết định Markov (MDP) là một mô hình toán học dùng để mô tả quá trình ra quyết định trong môi trường không chắc chắn, trong đó kết quả phụ thuộc một phần vào các quyết định và một phần vào yếu tố ngẫu nhiên.

### 1.2. So sánh với K-Armed Bandit

**K-Armed Bandit:**
- Tác nhân luôn gặp cùng một tình huống
- Cùng một hành động luôn là tối ưu
- Chỉ quan tâm đến phần thưởng tức thời

**Ví dụ K-Armed Bandit-:**
```
Tình huống: Chọn 1 trong 3 nhà hàng cho bữa trưa
- Nhà hàng A: Phở (đánh giá trung bình 4.5/5 sao)
- Nhà hàng B: Cơm văn phòng (đánh giá trung bình 4.0/5 sao)
- Nhà hàng C: Bún chả (đánh giá trung bình 3.8/5 sao)

→ Nhà hàng A luôn là lựa chọn tối ưu nhất
→ Không quan tâm đến hôm trước ăn gì
→ Chỉ dựa vào đánh giá trung bình
→ Không cần cân nhắc các yếu tố khác (giá, thời gian chờ, etc.)
```

**MDP:**
- Tình huống thay đổi theo thời gian
- Hành động tối ưu phụ thuộc vào tình huống
- Cân nhắc cả phần thưởng tức thời và tương lai

**Ví dụ MDP-:**
```
Tình huống 1: Giờ cao điểm trưa
- Trạng thái: 
  + 80% bàn đã có khách
  + Hàng đợi 10 người
  + Thời gian chế biến trung bình 15 phút
- Hành động có thể: 
  + Tiếp tục nhận khách (+20k/khách, -1 điểm đánh giá)
  + Từ chối khách mới (0đ, giữ đánh giá)
  + Tăng nhân viên (-100k/giờ, +0.5 điểm đánh giá)
- Ảnh hưởng tương lai: Đánh giá online, khách quen

Tình huống 2: Cuối ngày
- Trạng thái:
  + 20% bàn có khách
  + Nguyên liệu dư 30%
  + 2 giờ trước đóng cửa
- Hành động có thể:
  + Giảm giá 30% (+50k/giờ, nguyên liệu hết)
  + Giữ giá gốc (+20k/giờ, nguyên liệu dư)
  + Đóng cửa sớm (0đ, tiết kiệm chi phí)
- Ảnh hưởng tương lai: Chi phí lưu trữ, lãng phí

Kết quả:
→ Mỗi quyết định ảnh hưởng đến nhiều khía cạnh
→ Chiến lược tối ưu thay đổi theo từng tình huống
→ Cần cân bằng nhiều mục tiêu (doanh thu, đánh giá, chi phí)
```

## Phần 2: Các Thành phần Toán học

### 2.1. Không gian Trạng thái (State Space)
$\mathcal{S}$ là tập hợp tất cả các trạng thái có thể:
- $s \in \mathcal{S}$: một trạng thái cụ thể
- $S_t$: trạng thái tại thời điểm t

### 2.2. Không gian Hành động (Action Space)
$\mathcal{A}(s)$ là tập hợp các hành động có thể trong trạng thái s:
- $a \in \mathcal{A}(s)$: một hành động cụ thể
- $A_t$: hành động được chọn tại thời điểm t

### 2.3. Hàm Phần thưởng (Reward Function)
$\mathcal{R}$ là tập hợp các phần thưởng có thể:
- $r \in \mathcal{R}$: một giá trị phần thưởng
- $R_{t+1}$: phần thưởng nhận được sau hành động $A_t$

### 2.4. Hàm Chuyển trạng thái (Transition Function)
$p(s',r|s,a)$ là xác suất chuyển từ trạng thái s sang s' với phần thưởng r khi thực hiện hành động a:

$$p(s',r|s,a) = P(S_{t+1}=s', R_{t+1}=r|S_t=s, A_t=a)$$

Tổng xác suất phải bằng 1:

$$\sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s',r|s,a) = 1, \forall s \in \mathcal{S}, a \in \mathcal{A}(s)$$

## Phần 3: Ví dụ Minh họa - Con Thỏ và Thức ăn

### 3.1. Mô tả Bài toán
Một con thỏ di chuyển trong môi trường có:
- Cà rốt (phần thưởng +10)
- Bông cải xanh (phần thưởng +3)
- Hổ (phần thưởng -100)

### 3.2. Phân tích theo MDP

**Trạng thái (S):**
```
S = {
    s1: (thỏ, cà_rốt_phải, bông_cải_trái),
    s2: (thỏ, cà_rốt_trái, bông_cải_phải),
    s3: (thỏ, cà_rốt_phải, hổ_phải),
    ...
}
```

**Hành động (A):**
```
A = {
    di_chuyển_trái,
    di_chuyển_phải
}
```

**Phần thưởng (R):**
```
R = {
    +10: ăn cà rốt,
    +3: ăn bông cải,
    -100: gặp hổ
}
```

### 3.3. Các Tình huống Cụ thể

#### Tình huống 1: Lựa chọn Đơn giản
- **Trạng thái:** Cà rốt phải (+10), Bông cải trái (+3)
- **Quyết định tối ưu:** Di chuyển phải
- **Lý do:** Phần thưởng cao hơn, không có rủi ro

#### Tình huống 2: Cân nhắc Rủi ro
- **Trạng thái:** Cà rốt phải (+10) nhưng có hổ (-100)
- **Quyết định tối ưu:** Di chuyển trái
- **Lý do:** Tránh rủi ro lớn trong tương lai

## Phần 4: Tính chất Markov

### 4.1. Định nghĩa Toán học
Tính chất Markov phát biểu rằng trạng thái hiện tại chứa đủ thông tin để dự đoán tương lai:

$$P(S_{t+1}|S_t,A_t) = P(S_{t+1}|S_t,A_t,S_{t-1},A_{t-1},...,S_0,A_0)$$

### 4.2. Ý nghĩa
- Chỉ cần biết trạng thái hiện tại
- Không cần lưu trữ lịch sử
- Đơn giản hóa việc ra quyết định

## Phần 5: Ứng dụng Thực tế

### 5.1. Robotics
- Điều khiển robot tự hành
- Lập kế hoạch đường đi
- Tránh vật cản

### 5.2. Trò chơi
- AI trong game
- Chiến lược tối ưu
- Học từ trải nghiệm

### 5.3. Tài chính
- Quản lý danh mục đầu tư
- Giao dịch tự động
- Quản lý rủi ro

----------------------------------------------------------------------------------------------------------------------------                                                                                                                                    
  ##### 5-17-2025 at 8AM.
  ##### Course: Fundamentals of Reinforcement Learning/Module 3.
  ##### Đọc tài liệu tại: Introduction to Markov Decision Processes.
  ##### Học nội dung từ clip: Introduction to Markov Decision Processes/Markov Decision Processes.