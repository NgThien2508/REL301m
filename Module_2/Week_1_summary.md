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
  ```
  q*(a) = E[Rt | At = a]  ∀a ∈ {1,...,k}
  ```
  - q*(a): Giá trị thực của hành động a
  - E[Rt]: Kỳ vọng phần thưởng tại thời điểm t
  - At = a: Khi chọn hành động a

### 2.2 Ước lượng giá trị
1. **Phương pháp trung bình mẫu (Sample-Average Method)**:
   ```
   Qt(a) = (Tổng phần thưởng khi chọn a) / (Số lần chọn a)
         = Σ(Rt) / (t-1)
   ```

2. **Cập nhật gia tăng (Incremental Update)**:
   ```
   Qt+1(a) = Qt(a) + 1/Nt(a) * [Rt - Qt(a)]
   ```
   - Qt(a): Ước lượng hiện tại
   - Rt: Phần thưởng mới
   - Nt(a): Số lần chọn a
   - [Rt - Qt(a)]: Sai số

## 3. Thăm dò và Khai thác (Exploration vs. Exploitation)

### 3.1 Định nghĩa
- **Thăm dò (Exploration)**: 
  - Cải thiện kiến thức cho lợi ích dài hạn
  - Thử nghiệm các hành động mới

- **Khai thác (Exploitation)**:
  - Sử dụng kiến thức hiện có cho lợi ích ngắn hạn
  - Chọn hành động tốt nhất đã biết

### 3.2 Phương pháp ε-greedy
```
At ← {
    argmax Qt(a)               với xác suất 1-ε
    a ~ Uniform({a1...ak})     với xác suất ε
}
```
- ε: Tỷ lệ thăm dò (thường 0.1 hoặc nhỏ hơn)
- 1-ε: Tỷ lệ khai thác
- Uniform: Chọn ngẫu nhiên đều

## 4. Giá trị Khởi tạo Lạc quan (Optimistic Initial Values)

### 4.1 Nguyên lý
- Khởi tạo Qt(a) với giá trị cao hơn q*(a)
- Ví dụ: Q1(a) = 2.0 cho mọi a
- Tạo động lực thăm dò tự nhiên

### 4.2 Ưu điểm
- Thăm dò có hệ thống ban đầu
- Tự động giảm thăm dò theo thời gian
- Không cần tham số ε

## 5. Phương pháp UCB (Upper-Confidence Bound)

### 5.1 Công thức
```
At = argmax[Qt(a) + c*sqrt(ln t/Nt(a))]
```
- Qt(a): Phần khai thác (exploit)
- c*sqrt(ln t/Nt(a)): Phần thăm dò (explore)
- c: Tham số kiểm soát mức độ thăm dò

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
