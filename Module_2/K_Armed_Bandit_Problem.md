---
layout: default
title: K-Armed Bandit
---

<script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

<style>
mjx-container {
  font-size: 180% !important;
}
</style>


# Thảo luận về vấn đề của K-Armed bandit
## Giới thiệu
K-Armed problem là bài toán kinh điển trong học tăng cường. Nó giả định ra các tình huống mà bạn phải lựa chọn giữa k hành động(k=n) khác nhau, mỗi hành động mang lại kết quả, giá trị ngẫu nhiên với mục đích là tối ưu hóa giá trị nhận được qua một loạt các lần thử cho từng trường hợp.
## Ví dụ thực tế
Giả định rằng bác sĩ (agent) chữa bệnh cho bệnh nhân với 3 phương pháp được áp dụng cho việc điều trị(K=3). 
- Bác sĩ phải lựa chọn giữa 3 hành động khác nhau k=3 (actions) để kê đơn điều trị ví dụ như thuốc A, thuốc B, thuốc C.
- Mỗi phương pháp điều trị là 1 hành động và hiệu quả của 3 phương pháp là khác nhau.
- Mỗi hành động sẽ mang lại kết quả ngẫu nhiên (reward) cho bệnh nhân.
    + Một phương pháp điều trị dường như hoạt động tốt hơn các phương pháp khác ví dụ như thuốc C.
    + Có thể một trong các phương pháp điều trị khác như thuốc A hoặc B thực sự tốt hơn nhưng hiệu quả của nó không được biết đến ngay lập tức.
    + Nhưng nếu nó thật sự không tốt thì sẽ ảnh hưởng đến tình trnagj sức khỏe của bệnh nhân.
    > Minh chứng cho mỗi hành động cho ra kết quả ngẫu nhiên trong điều kiện không chắc chắn. 
- Mục đích là tối ưu hóa phương pháp chữa bệnh tốt nhất cho bệnh nhân
## Action values
- Values là giá trị phần thưởng dự kiến của mỗi hành động trong một tình huống
    * Với công thức: 

$$
q_*(a) \overset{\text{.}}{=} \mathbb{E}[R_t \mid A_t = a], \quad \forall a \in \{1, \ldots, k\}
$$

     