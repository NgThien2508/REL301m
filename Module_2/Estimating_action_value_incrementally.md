# Ước tính Giá trị Hành động theo Phương pháp Tăng dần

## Giới thiệu
Trong thực tế, việc lưu trữ và tính toán tất cả dữ liệu quá khứ có thể gặp khó khăn với bộ dữ liệu lớn. Ví dụ: một trang web có hàng triệu lượt truy cập mỗi ngày, việc tính toán giá trị trung bình của các quảng cáo sẽ tốn nhiều tài nguyên. Vì vậy, chúng ta cần một phương pháp hiệu quả hơn.

### Ví dụ Thực tế: Hệ thống Quảng cáo
Giả sử bạn có một trang web với 3 vị trí đặt quảng cáo (A, B, C):
- Mỗi ngày có 1 triệu lượt click
- Cần tính giá trị trung bình của mỗi vị trí
- Lưu trữ toàn bộ dữ liệu sẽ cần: 3 vị trí × 1 triệu click × 4 byte ≈ 12MB/ngày

## Phương pháp Cập nhật Tăng dần (Incremental Update)

### Công thức Tổng quát và Giải thích
$$Q_{n+1} = Q_n + \alpha_n(R_n - Q_n)$$

**Giải thích từng thành phần:**
1. $Q_{n+1}$: Giá trị ước tính mới sau khi cập nhật
2. $Q_n$: Giá trị ước tính hiện tại
3. $R_n$: Phần thưởng mới nhận được
4. $\alpha_n$: Kích thước bước (step size), điều chỉnh tốc độ học
5. $(R_n - Q_n)$: Sai số giữa giá trị thực và ước tính

**Ví dụ Minh họa:**
```
Giả sử đang theo dõi vị trí quảng cáo A:
- Q₃ = 5.0 (giá trị ước tính hiện tại sau 3 lần)
- R₄ = 7.0 (phần thưởng mới nhận được)
- α₄ = 1/4 = 0.25 (step size)

Tính Q₄:
Q₄ = 5.0 + 0.25(7.0 - 5.0)
   = 5.0 + 0.25 × 2.0
   = 5.0 + 0.5
   = 5.5
```

### Chứng minh từ Phương pháp Trung bình Mẫu
#### Bước 1: Công thức ban đầu
$$Q_{n+1} = \frac{1}{n}\sum_{i=1}^n R_i$$

**Giải thích:** Đây là công thức trung bình cộng thông thường, tính tổng tất cả phần thưởng chia cho số lần.

**Ví dụ:**
```
Có 4 phần thưởng: [6, 4, 8, 6]
Q₅ = (6 + 4 + 8 + 6)/4 = 24/4 = 6
```

#### Bước 2: Tách phần tử mới nhất
$$Q_{n+1} = \frac{1}{n}(R_n + \sum_{i=1}^{n-1} R_i)$$

**Giải thích:** Tách riêng phần thưởng mới nhất để chuẩn bị cho việc biến đổi.

**Ví dụ:**
```
Q₅ = (6 + (6 + 4 + 8))/4
   = (6 + 18)/4
```

#### Bước 3: Biến đổi
$$Q_{n+1} = \frac{1}{n}(R_n + (n-1)Q_n)$$
$$= \frac{1}{n}R_n + \frac{n-1}{n}Q_n$$
$$= Q_n + \frac{1}{n}(R_n - Q_n)$$

**Giải thích từng bước:**
1. Thay tổng cũ bằng (n-1) nhân với trung bình cũ
2. Tách phân số
3. Biến đổi thành dạng cập nhật tăng dần

**Ví dụ hoàn chỉnh:**
```
Dữ liệu: [6, 4, 8, 6]
Q₄ = 6.0

Cách 1 (Trung bình thông thường):
Q₅ = (6 + 4 + 8 + 6)/4 = 6.0

Cách 2 (Cập nhật tăng dần):
Q₅ = 6.0 + (1/4)(6 - 6.0)
   = 6.0 + 0
   = 6.0
```

### Ứng dụng cho Bài toán Non-stationary

#### Ví dụ Chi tiết: Hệ thống Khuyến nghị Phim
```
Giả sử một phim có điểm đánh giá thay đổi theo thời gian:
- Tuần 1-2: Điểm trung bình 8.0 (mới ra mắt)
- Tuần 3-4: Điểm trung bình 7.0 (hype giảm)
- Tuần 5-6: Điểm trung bình 7.5 (word of mouth tốt)

Với α = 0.1:
1. Sau tuần 2: Q = 8.0
2. Sau tuần 4: 
   Q = 8.0 + 0.1(7.0 - 8.0) = 7.9
3. Sau tuần 6:
   Q = 7.9 + 0.1(7.5 - 7.9) = 7.86
```

#### Phân tích Trọng số Phần thưởng
```
Với α = 0.1, trọng số của các phần thưởng:
- Phần thưởng hiện tại: 0.1
- Phần thưởng trước đó: 0.1 × 0.9 = 0.09
- Hai lần trước: 0.1 × 0.9² = 0.081
- Ba lần trước: 0.1 × 0.9³ = 0.073
```

## Bài toán Non-stationary (Môi trường Không Dừng)

### 1. Định nghĩa
- **Stationary (Môi trường Dừng)**: Phân phối xác suất của phần thưởng KHÔNG thay đổi theo thời gian
- **Non-stationary (Môi trường Không Dừng)**: Phân phối xác suất của phần thưởng CÓ thay đổi theo thời gian

### 2. Ví dụ Thực tế: Nhà hàng
```
Nhà hàng A (Môi trường Stationary):
- Đầu bếp không thay đổi
- Menu cố định
- Chất lượng ổn định
→ Điểm đánh giá dao động quanh 8.0 ± 0.5

Nhà hàng B (Môi trường Non-stationary):
- Đầu bếp thường xuyên thay đổi
- Menu thay đổi theo mùa
- Chất lượng không ổn định
→ Điểm đánh giá thay đổi nhiều: 6.0 → 8.0 → 7.0
```

### 3. Vấn đề với Phương pháp Trung bình Mẫu
#### Trong môi trường Stationary:
```
Nhà hàng A - 10 đánh giá gần nhất:
[8.0, 7.8, 8.2, 7.9, 8.1, 8.0, 7.8, 8.2, 7.9, 8.1]
Trung bình = 8.0 (phản ánh chính xác chất lượng)
```

#### Trong môi trường Non-stationary:
```
Nhà hàng B - 10 đánh giá theo thời gian:
[6.0, 6.2, 6.0, 7.5, 7.8, 8.0, 7.5, 7.0, 6.8, 6.5]
Trung bình = 7.0 (KHÔNG phản ánh chính xác chất lượng hiện tại)
```

### 4. Giải pháp: Sử dụng Step Size (α) Cố định

#### Nguyên lý hoạt động:
1. Thay vì sử dụng $\alpha = \frac{1}{n}$, ta sử dụng α cố định (ví dụ: 0.1)
2. Điều này giúp ưu tiên dữ liệu gần đây hơn
3. Công thức: $Q_{n+1} = Q_n + \alpha(R_n - Q_n)$

#### Phân tích trọng số:
Với α = 0.1, trọng số của các phần thưởng sẽ giảm dần theo thời gian:
```
Thời điểm hiện tại (n):   0.100 = 0.1
Lần trước (n-1):          0.090 = 0.1 × 0.9
Hai lần trước (n-2):      0.081 = 0.1 × 0.9²
Ba lần trước (n-3):       0.073 = 0.1 × 0.9³
```

### 5. Ví dụ Chi tiết: Đánh giá Hiệu quả Thuốc
```
Một loại thuốc có hiệu quả thay đổi theo mùa:
Mùa hè: Hiệu quả 60%
Mùa thu: Hiệu quả 75%
Mùa đông: Hiệu quả 90%

Theo dõi bằng α = 0.1:

Ban đầu (mùa hè):
Q₁ = 60%

Chuyển sang mùa thu:
Q₂ = 60% + 0.1(75% - 60%) = 61.5%
Q₃ = 61.5% + 0.1(75% - 61.5%) = 62.85%
Q₄ = 62.85% + 0.1(75% - 62.85%) = 64.07%

Chuyển sang mùa đông:
Q₅ = 64.07% + 0.1(90% - 64.07%) = 66.66%
Q₆ = 66.66% + 0.1(90% - 66.66%) = 69.00%

→ Giá trị Q dần dần thích nghi với hiệu quả mới của thuốc
```

### 6. So sánh Hai Phương pháp

#### Phương pháp Trung bình Mẫu ($\alpha = \frac{1}{n}$):
```
Ưu điểm:
- Chính xác cho môi trường stationary
- Hội tụ về giá trị thực

Nhược điểm:
- Phản ứng chậm với thay đổi
- Coi trọng dữ liệu cũ và mới như nhau
```

#### Phương pháp Step Size Cố định (α = 0.1):
```
Ưu điểm:
- Thích nghi nhanh với thay đổi
- Ưu tiên dữ liệu gần đây
- Phù hợp với môi trường non-stationary

Nhược điểm:
- Không hội tụ về một giá trị cố định
- Luôn dao động quanh giá trị thực
```

### 7. Kết luận
1. Chọn phương pháp phù hợp với môi trường:
   - Môi trường ổn định → Dùng trung bình mẫu
   - Môi trường thay đổi → Dùng step size cố định

2. Lựa chọn giá trị α:
   - α lớn (0.5-0.9): Thích nghi nhanh, dao động mạnh
   - α nhỏ (0.1-0.3): Thích nghi chậm, ổn định hơn