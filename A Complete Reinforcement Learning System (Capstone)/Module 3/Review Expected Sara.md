# Tổng quan về Expected Sarsa trong học tăng cường

Bài viết này trình bày về Expected Sarsa, một thuật toán thuộc nhóm TD control, nổi bật nhờ cách cập nhật dựa trên kỳ vọng thay vì lấy mẫu đơn lẻ.

## Bản chất của Expected Sarsa

Expected Sarsa là phương pháp cập nhật giá trị hành động bằng cách tính trung bình có trọng số các giá trị hành động tiếp theo, dựa trên xác suất của từng hành động theo chính sách hiện tại. Điều này khác với Sarsa truyền thống, vốn chỉ sử dụng giá trị của một hành động được chọn ngẫu nhiên.

Thay vì lấy mẫu một hành động tiếp theo, Expected Sarsa tính toán tổng các giá trị hành động ở trạng thái tiếp theo, mỗi giá trị được nhân với xác suất chọn hành động đó.

## Cách cập nhật trong Expected Sarsa

Quy tắc cập nhật của Expected Sarsa:
$$Q(s_t, a_t) \leftarrow Q(s_t, a_t) + \alpha \left[ R_{t+1} + \gamma \sum_a \pi(a|s_{t+1})Q(s_{t+1}, a) - Q(s_t, a_t) \right]$$

Việc sử dụng kỳ vọng giúp mục tiêu cập nhật ổn định hơn, giảm phương sai so với Sarsa, từ đó giúp quá trình học hội tụ tốt hơn.

## Ưu điểm và hạn chế

### Ưu điểm
- Giảm biến động trong mục tiêu cập nhật, giúp ước lượng giá trị chính xác hơn.
- Thường hội tụ nhanh và ổn định hơn Sarsa truyền thống.

### Hạn chế
- Việc tính toán trung bình qua tất cả các hành động có thể tốn kém về mặt tính toán, đặc biệt khi không gian hành động lớn.
- Cần lưu trữ và cập nhật xác suất chính sách cho từng hành động.
