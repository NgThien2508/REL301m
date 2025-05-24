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

* Giá trị của một hành động là phần thưởng kỳ vọng khi hành động đó được thực hiện

Công thức toán học:

$$q_*(a) = \mathbb{E}[R_t | A_t = a], \quad \forall a \in 1, ..., k$$

+ $q_{*}(a)$: giá trị thực của hành động a không được biết trước, vì vậy chúng ta cần ước tính nó
+ $R_t$: phần thưởng tại thời điểm t
+ $A_t$: hành động được chọn tại thời điểm t
+ $a$: hành động bất kỳ trong tập k hành động

