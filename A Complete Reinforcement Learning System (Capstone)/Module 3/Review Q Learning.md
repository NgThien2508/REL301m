# Tổng quan về Q-Learning trong học tăng cường

Bài viết này trình bày về Q-learning, một thuật toán học tăng cường nổi bật, đóng vai trò nền tảng cho nhiều ứng dụng thực tế như trò chơi điện tử và điều khiển tự động.

## Khái quát về Q-Learning

Q-learning là một phương pháp học tăng cường không dựa vào mô hình (model-free) và thuộc nhóm off-policy. Ra đời từ năm 1989, thuật toán này đã được ứng dụng rộng rãi trong nhiều lĩnh vực nhờ khả năng học chính sách tối ưu mà không cần biết trước động lực môi trường.

Mục tiêu của Q-learning là tìm ra hàm giá trị hành động tối ưu $Q^*$, bất kể chính sách hiện tại của tác tử là gì. Để đạt được điều này, Q-learning sử dụng một dạng cập nhật dựa trên phương trình tối ưu Bellman.

## Cách cập nhật giá trị trong Q-Learning

Điểm then chốt của Q-learning là cách cập nhật giá trị Q cho từng cặp trạng thái-hành động. Thay vì dựa vào hành động tiếp theo thực sự được chọn (như Sarsa), Q-learning sử dụng giá trị lớn nhất trong các hành động khả dĩ ở trạng thái tiếp theo.

Công thức cập nhật:
$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \right]$$

- **Mục tiêu cập nhật:** $R_{t+1} + \gamma \max_{a'} Q(s_{t+1}, a')$
- Việc sử dụng toán tử $\max$ cho phép thuật toán giả định rằng tác tử luôn chọn hành động tốt nhất ở trạng thái tiếp theo.

## So sánh Q-Learning và Sarsa

- **Sarsa (On-policy):** Giá trị Q được cập nhật dựa trên hành động mà tác tử thực sự thực hiện, phản ánh chính sách hiện tại (bao gồm cả thăm dò).
- **Q-learning (Off-policy):** Giá trị Q được cập nhật dựa trên hành động tối ưu ở trạng thái tiếp theo, cho phép học chính sách tối ưu ngay cả khi tác tử đang thăm dò.

Nhờ sử dụng phương trình tối ưu Bellman, Q-learning liên tục cải thiện hàm giá trị và có thể hội tụ về $Q^*$ nếu mọi cặp trạng thái-hành động đều được khám phá đủ.
