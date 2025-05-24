<!--
layout: default
title: K-Armed Bandit
---

<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

<style>
mjx-container {
  font-size: 10000% !important;
}
</style>
-->

# Giá trị của một Hành động (Value of an Action)

## Định nghĩa
Giá trị của một hành động là phần thưởng kỳ vọng khi hành động đó được thực hiện.

## Công thức toán học
$$q_*(a) = \mathbb{E}[R_t | A_t = a], \quad \forall a \in 1, ..., k$$

## Giải thích các thành phần

### Các biến số
- $q_{*}(a)$: giá trị thực của hành động a không được biết trước, vì vậy chúng ta cần ước tính nó
- $R_t$: phần thưởng tại thời điểm t
- $A_t$: hành động được chọn tại thời điểm t
- $a$: hành động bất kỳ trong tập k hành động

### Ý nghĩa
- $\mathbb{E}[R_t | A_t = a]$ thể hiện giá trị kỳ vọng của phần thưởng tại thời điểm t, với điều kiện hành động a được chọn tại thời điểm đó
- $\forall a \in 1, ..., k$ nghĩa là công thức này áp dụng cho mọi hành động a trong tập k hành động có sẵn

## Phương pháp Trung bình Mẫu (Sample-Average Method)

### Định nghĩa
Phương pháp trung bình mẫu là cách ước tính giá trị của một hành động bằng cách tính trung bình các phần thưởng nhận được khi thực hiện hành động đó.

### Công thức toán học
$$Q_t(a) = \frac{\text{tổng phần thưởng khi chọn }a\text{ trước thời điểm }t}{\text{số lần chọn }a\text{ trước thời điểm }t}$$

Hay biểu diễn dưới dạng toán học:

$$Q_t(a) = \frac{\sum_{i=1}^{t-1} R_i}{t-1}$$

### Giải thích các thành phần
- $Q_t(a)$: giá trị ước tính của hành động $a$ tại thời điểm $t$
- $R_i$: phần thưởng nhận được tại thời điểm $i$
- $t-1$: số lần hành động $a$ đã được chọn trước thời điểm $t$
- $\sum_{i=1}^{t-1}$: tổng các phần thưởng từ lần đầu tiên đến lần $t-1$

### Ý nghĩa
- Công thức này giúp ước tính giá trị thực $q_*(a)$ thông qua việc tính trung bình các phần thưởng đã nhận được
- Giá trị ước tính $Q_t(a)$ sẽ tiến dần đến giá trị thực $q_*(a)$ khi số lần thử nghiệm tăng lên
- Đây là phương pháp đơn giản và hiệu quả để học từ trải nghiệm thực tế

### Ví dụ thực tế:

Giả sử một người đang thử nghiệm 3 nhà hàng khác nhau:

1. **Nhà hàng A (Phở):**
   ```
   Lần 1: 8 điểm (Phở ngon, nước dùng đậm đà)
   Lần 2: 7 điểm (Thịt hơi ít)
   Lần 3: 9 điểm (Phở đặc biệt cuối tuần)
   ```
   $$Q_4(A) = \frac{8 + 7 + 9}{3} = \frac{24}{3} = 8.0$$

2. **Nhà hàng B (Cơm):**
   ```
   Lần 1: 6 điểm (Cơm hơi nguội)
   Lần 2: 8 điểm (Có món mới)
   Lần 3: 7 điểm (Bình thường)
   ```
   $$Q_4(B) = \frac{6 + 8 + 7}{3} = \frac{21}{3} = 7.0$$

3. **Nhà hàng C (Bún):**
   ```
   Lần 1: 9 điểm (Bún rất ngon)
   Lần 2: 5 điểm (Đầu bếp nghỉ, người mới)
   Lần 3: 6 điểm (Đang cải thiện)
   ```
   $$Q_4(C) = \frac{9 + 5 + 6}{3} = \frac{20}{3} \approx 6.67$$

#### Phân tích so sánh

1. **Xếp hạng theo điểm trung bình:**
   - Nhà hàng A (Phở): 8.0 điểm
   - Nhà hàng B (Cơm): 7.0 điểm
   - Nhà hàng C (Bún): 6.67 điểm

2. **Phân tích độ ổn định:**
   - Nhà hàng A: Độ lệch chuẩn thấp (7-9 điểm), chất lượng ổn định
   - Nhà hàng B: Độ lệch trung bình (6-8 điểm), có cải thiện
   - Nhà hàng C: Độ lệch cao (5-9 điểm), chất lượng không ổn định


#### Áp dụng thực tế
- Sử dụng dữ liệu này để quyết định chọn nhà hàng cho các dịp khác nhau
- Tiếp tục cập nhật đánh giá để có cái nhìn chính xác hơn
- Có thể bổ sung thêm các tiêu chí khác như giá cả, thời gian chờ, không gian...

## Lựa chọn Hành động (Action Selection)

### Định nghĩa
Trong quá trình học tăng cường, tác tử (agent) phải cân bằng giữa hai chiến lược:
1. **Khai thác (Exploitation)**: Chọn hành động tốt nhất dựa trên kiến thức hiện tại
2. **Khám phá (Exploration)**: Thử nghiệm các hành động mới để tìm kiếm giải pháp tốt hơn

### Hành động Tham lam (Greedy Action)
- Là hành động có giá trị ước tính cao nhất tại thời điểm hiện tại
- Được tính bằng cách lấy argmax của các giá trị ước tính
- Công thức: $$A_t = \underset{a}{\operatorname{argmax}} Q_t(a)$$

### Ví dụ với bài toán chọn nhà hàng:

Dựa trên dữ liệu sau 3 lần thử:

1. **Giá trị ước tính của các nhà hàng:**
   - Q(A) = 8.0 (Phở)
   - Q(B) = 7.0 (Cơm)
   - Q(C) = 6.67 (Bún)

2. **Chiến lược Khai thác (Exploitation):**
   - Chọn nhà hàng A (Phở) vì Q(A) = 8.0 là cao nhất
   - Ưu điểm: Đảm bảo được trải nghiệm tốt dựa trên dữ liệu hiện có
   - Nhược điểm: Có thể bỏ lỡ cơ hội tìm được nhà hàng ngon hơn

3. **Chiến lược Khám phá (Exploration):**
   - Thử nhà hàng B hoặc C mặc dù điểm thấp hơn
   - Ưu điểm: 
     + Có thể phát hiện sự cải thiện (ví dụ: đầu bếp mới)
     + Tích lũy thêm thông tin về các lựa chọn khác
   - Nhược điểm: Rủi ro có trải nghiệm không tốt

### Đánh đổi giữa Khai thác và Khám phá

1. **Khai thác (Exploitation):**
   ```
   - Khi nào sử dụng: 
     + Cần đảm bảo trải nghiệm tốt
     + Có thời gian giới hạn
     + Đã có đủ thông tin về các lựa chọn
   - Trong ví dụ: Chọn nhà hàng A cho bữa ăn quan trọng
   ```

2. **Khám phá (Exploration):**
   ```
   - Khi nào sử dụng:
     + Có thời gian để thử nghiệm
     + Muốn tìm kiếm lựa chọn tốt hơn
     + Chưa có đủ thông tin về các lựa chọn
   - Trong ví dụ: Thử nhà hàng B hoặc C trong bữa ăn thông thường
   ```

### Lưu ý quan trọng
1. Không thể vừa khai thác (Exploitation) vừa khám phá (Exploration) cùng lúc
2. Cần cân bằng giữa hai chiến lược để tối ưu hóa kết quả dài hạn
3. Tỷ lệ giữa khai thác và khám phá có thể thay đổi theo thời gian:
   - Giai đoạn đầu: Ưu tiên khám phá
   - Giai đoạn sau: Ưu tiên khai thác

## Kết luận

### Tổng quan về Action Value
1. **Định nghĩa và Ý nghĩa:**
   - Action Value là giá trị kỳ vọng của phần thưởng khi thực hiện một hành động
   - Giúp đánh giá và so sánh hiệu quả của các hành động khác nhau
   - Là nền tảng cho việc ra quyết định trong học tăng cường

2. **Phương pháp Ước tính:**
   - Sử dụng phương pháp trung bình mẫu để ước tính giá trị thực
   - Cập nhật liên tục dựa trên phản hồi từ môi trường
   - Độ chính xác tăng theo số lượng mẫu thu thập được

3. **Chiến lược Lựa chọn Hành động:**
   - Cân bằng giữa Khai thác (Exploitation) và Khám phá (Exploration)
   - Khai thác: tận dụng kiến thức hiện có để đạt phần thưởng cao
   - Khám phá: tìm kiếm các cơ hội mới tiềm năng
