# Exercise 3.24

**Figure 3.5** cho giá trị tối ưu của trạng thái tốt nhất trong gridworld là 24.4 (làm tròn đến một chữ số thập phân). Sử dụng công thức (3.8) và giá trị tối ưu này để biểu diễn giá trị một cách ký hiệu, sau đó tính ra đến ba chữ số thập phân.

---

## 1. Viết lại công thức return

$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$

---

## 2. Sử dụng ký hiệu $G_t^{(A)}$ cho return bắt đầu ở A

Giả sử tại trạng thái A, phần thưởng nhận được là 10 ở bước đầu, các bước sau là 0, ngoại trừ sau 5 bước lại nhận được 10 (do quay lại A):

$$G_t^{(A)} = 10 + \gamma \cdot 0 + \gamma^2 \cdot 0 + \gamma^3 \cdot 0 + \gamma^4 \cdot 0 + \gamma^5 R_{t+6} + \gamma^6 R_{t+7} + \ldots$$

Vì sau 5 bước lại quay về A, nên:

$$G_t^{(A)} = 10 + \gamma^5 G_{t+5}^{(A)}$$

---

## 3. Giá trị kỳ vọng trạng thái (Value function)

Giá trị tối ưu tại A:

$$v_{\star}(A) = \mathbb{E}[G_t | S_t = A, \pi = \pi_{\star}]$$

Theo Bellman:

$$v_{\star}(A) = 10 + \gamma^5 v_{\star}(A)$$

---

## 4. Giải phương trình

Chuyển vế:

$$v_{\star}(A) - \gamma^5 v_{\star}(A) = 10$$

$$v_{\star}(A) (1 - \gamma^5) = 10$$

$$v_{\star}(A) = \frac{10}{1 - \gamma^5}$$

---

## 5. Thay số cụ thể

Với $\gamma = 0.9$:

$$\gamma^5 = (0.9)^5 = 0.59049$$

$$1 - \gamma^5 = 1 - 0.59049 = 0.40951$$

$$v_{\star}(A) = \frac{10}{0.40951} \approx 24.414$$

---

## 6. Kết luận

Giá trị tối ưu của trạng thái tốt nhất là:

$$\boxed{v_{\star}(A) \approx 24.414}$$

Làm tròn đến một chữ số thập phân: 24.4

---

**Tóm lại:**
- Viết lại công thức return.
- Nhận diện chu kỳ nhận thưởng (cứ 5 bước lại nhận 10 điểm).
- Thiết lập phương trình Bellman cho trạng thái A.
- Giải phương trình để tìm giá trị tối ưu.
- Thay số cụ thể để ra kết quả cuối cùng.
