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

