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

## Kết luận với Ví dụ Tổng hợp
```
So sánh hai phương pháp với dữ liệu thay đổi:
[8, 8, 7, 7, 7.5, 7.5]

1. Trung bình thông thường:
   Q = (8+8+7+7+7.5+7.5)/6 = 7.5

2. Cập nhật tăng dần (α = 0.1):
   Q₁ = 8.0
   Q₂ = 8.0 + 0.1(8-8) = 8.0
   Q₃ = 8.0 + 0.1(7-8) = 7.9
   Q₄ = 7.9 + 0.1(7-7.9) = 7.81
   Q₅ = 7.81 + 0.1(7.5-7.81) = 7.78
   Q₆ = 7.78 + 0.1(7.5-7.78) = 7.75

→ Phương pháp tăng dần phản ánh tốt hơn xu hướng gần đây