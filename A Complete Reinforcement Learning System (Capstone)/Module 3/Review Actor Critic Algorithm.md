# Tổng quan về thuật toán Actor-Critic trong học tăng cường

Bài viết này trình bày về Actor-Critic, một thuật toán nổi bật kết hợp giữa hai hướng tiếp cận: học chính sách (policy gradient) và học giá trị (value function) trong reinforcement learning.

## Cấu trúc của Actor-Critic

Thuật toán Actor-Critic bao gồm hai bộ phận chính:
- **Actor**: Đảm nhận vai trò xây dựng chính sách, quyết định lựa chọn hành động dựa trên trạng thái hiện tại. Actor điều chỉnh các tham số của chính sách thông qua các phương pháp gradient để nâng cao chất lượng quyết định.
- **Critic**: Đánh giá hiệu quả của các hành động do actor thực hiện bằng cách ước lượng giá trị trạng thái hoặc giá trị hành động. Critic sử dụng sai số TD (temporal difference error) để phản hồi cho actor về mức độ tốt/xấu của hành động vừa chọn.

## Cách thức hoạt động

- **Tương tác với môi trường**: Actor lựa chọn hành động dựa trên chính sách hiện tại và thực hiện hành động đó trong môi trường.
- **Đánh giá và cập nhật**: Critic tính toán TD error dựa trên phần thưởng nhận được và giá trị trạng thái, sau đó cập nhật hàm giá trị. Actor sử dụng thông tin này để điều chỉnh chính sách, tăng xác suất chọn các hành động tốt.

## Lợi ích của Actor-Critic

- Kết hợp ưu điểm của hai hướng tiếp cận: vừa học trực tiếp chính sách, vừa tận dụng thông tin giá trị để giảm phương sai khi cập nhật.
- Việc sử dụng baseline (giá trị tham chiếu) giúp cập nhật chính sách ổn định và nhanh hơn.
- Phù hợp với các môi trường liên tục hoặc không gian hành động lớn nhờ khả năng tổng quát hóa tốt.

## Quy trình Actor-Critic với phần thưởng trung bình (Average Reward)

1. **Khởi tạo**:
   - Đặt tham số cho actor (chính sách) và critic (hàm giá trị).
   - Khởi tạo giá trị trung bình phần thưởng (average reward) bằng 0.
   - Chọn các hệ số học phù hợp cho từng thành phần.

2. **Lặp lại cho từng bước**:
   - Actor chọn hành động dựa trên chính sách hiện tại.
   - Nhận phần thưởng và trạng thái mới từ môi trường.
   - Critic tính toán sai số TD dựa trên phần thưởng chênh lệch và giá trị trạng thái.
   - Cập nhật ước lượng average reward.
   - Critic cập nhật hàm giá trị.
   - Actor điều chỉnh tham số chính sách dựa trên TD error.

3. **Lặp liên tục**: Thuật toán phù hợp cho các bài toán không có điểm dừng rõ ràng, cho phép cải thiện chính sách liên tục theo thời gian.

## Tổng kết

Actor-Critic là giải pháp hiệu quả để học chính sách tối ưu nhờ sự phối hợp giữa cập nhật giá trị và điều chỉnh chính sách. Việc sử dụng baseline giúp giảm biến động trong quá trình học, đồng thời thích hợp với các môi trường phức tạp và không gian hành động rộng lớn.
