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

