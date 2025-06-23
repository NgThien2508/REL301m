# Tổng quan về so sánh TD Learning và Monte Carlo

Bài viết này phân tích sự khác biệt giữa hai phương pháp học tăng cường: Temporal Difference (TD) Learning và Monte Carlo, dựa trên một thí nghiệm minh họa cụ thể.

## Đối chiếu TD Learning và Monte Carlo

- Thí nghiệm sử dụng một mô hình quyết định đơn giản với năm trạng thái và hai lựa chọn hành động, đánh giá chính sách chọn hành động ngẫu nhiên.
- TD Learning cập nhật giá trị trạng thái ngay sau mỗi bước, còn Monte Carlo chỉ cập nhật sau khi kết thúc toàn bộ episode.

## Đánh giá quá trình học

- Qua nhiều episode, TD Learning tiến gần đến giá trị thực nhanh hơn so với Monte Carlo.
- Tốc độ hội tụ và độ chính xác phụ thuộc vào learning rate: tốc độ học cao giúp hội tụ nhanh nhưng sai số cuối cùng lớn hơn, tốc độ học thấp cho kết quả chính xác hơn nhưng chậm hơn.

## Điểm khác biệt chính

- **Thời điểm cập nhật:**
  - TD Learning: cập nhật liên tục sau mỗi bước, dựa trên giá trị trạng thái tiếp theo.
  - Monte Carlo: chỉ cập nhật sau khi hoàn thành một episode, dựa trên tổng phần thưởng thu được.
- **Cách tiếp cận:**
  - TD Learning: kết hợp ý tưởng từ dynamic programming và Monte Carlo, có thể học từ các episode chưa hoàn chỉnh.
  - Monte Carlo: chỉ sử dụng các episode hoàn chỉnh để tính giá trị trung bình.

## TD Error trong TD Learning

- TD error là chênh lệch giữa giá trị dự đoán của trạng thái hiện tại và giá trị thực tế quan sát được sau hành động.
- **Công thức:**
  $$
  \text{TD Error} = \text{Reward} + \gamma \cdot V(s') - V(s)
  $$
  - Reward: phần thưởng nhận được sau khi chuyển sang trạng thái tiếp theo.
  - $\gamma$: hệ số chiết khấu.
  - $V(s')$: giá trị ước lượng của trạng thái tiếp theo.
  - $V(s)$: giá trị ước lượng của trạng thái hiện tại.

## Kết luận

- TD Learning có tốc độ hội tụ nhanh hơn và đạt sai số cuối cùng thấp hơn Monte Carlo trong ví dụ này.
- TD error là yếu tố then chốt giúp cập nhật giá trị trạng thái trong TD Learning, cho phép tác tử học hiệu quả từ từng trải nghiệm.
