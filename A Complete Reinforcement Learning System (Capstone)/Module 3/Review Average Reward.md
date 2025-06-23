# Tổng quan về Average Reward trong học tăng cường

Bài viết này đề cập đến phương pháp tối ưu hóa phần thưởng trung bình (average reward) trong reinforcement learning, đặc biệt phù hợp với các bài toán liên tục không có điểm kết thúc rõ ràng.

## Khái niệm Average Reward

Average reward là một tiêu chí giúp đánh giá hiệu quả lâu dài của tác tử mà không cần sử dụng hệ số chiết khấu. Thay vì tập trung vào phần thưởng gần, phương pháp này quan tâm đến tốc độ nhận thưởng trung bình trên toàn bộ quá trình tác tử hoạt động.

Giá trị average reward của một chính sách (ký hiệu $R_\pi$) được xác định dựa trên kỳ vọng phần thưởng ở mỗi trạng thái, có xét đến tần suất xuất hiện của các trạng thái đó khi tác tử làm theo chính sách.

## Minh họa với Nearsighted MDP

Giả sử có một MDP gồm hai vòng lặp, mỗi vòng có phần thưởng khác nhau tại một số vị trí. Nếu dùng discount factor, việc chọn chính sách tối ưu sẽ phụ thuộc mạnh vào giá trị gamma. Ngược lại, average reward giúp tác tử ưu tiên chính sách mang lại tổng phần thưởng trung bình cao nhất, không bị ảnh hưởng bởi gamma.

## Differential Return và Value Function

Trong bối cảnh average reward, giá trị trả về (return) được xác định là phần thưởng nhận được trừ đi average reward, gọi là differential return. Điều này cho phép so sánh hiệu quả của các hành động trong cùng một chính sách.

Hàm giá trị (value function) phản ánh kỳ vọng của differential return, cho phép áp dụng các phương trình Bellman mà không cần discount, giúp chuyển đổi các thuật toán truyền thống sang dạng average reward dễ dàng hơn.

## Thuật toán Differential Sarsa cho Average Reward

Một thuật toán phổ biến là Differential Sarsa, với các bước chính như sau:

1. **Khởi tạo:**
   - Đặt giá trị ước lượng average reward $R$ ban đầu bằng 0.
   - Khởi tạo hàm giá trị hành động $Q(s, a)$.
   - Chọn trạng thái và hành động xuất phát.

2. **Lặp lại cho từng bước:**
   - Thực hiện hành động $a$, nhận phần thưởng $r$ và trạng thái mới $s'$.
   - Tính differential return: $r - R$.
   - Cập nhật $Q(s, a)$:  
     $Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (r - R)$
   - Cập nhật average reward:  
     $R \leftarrow R + \beta \cdot (r - R)$
   - Chuyển sang trạng thái mới và chọn hành động tiếp theo.

3. **Chính sách:** Có thể sử dụng epsilon-greedy hoặc softmax dựa trên $Q$.

## Kết luận

Average reward là một hướng tiếp cận hiệu quả cho các bài toán liên tục, giúp tác tử tối ưu hóa hiệu suất dài hạn mà không cần quan tâm đến discount factor. Các thuật toán như Differential Sarsa cho phép vừa học giá trị hành động vừa cập nhật average reward, mở rộng phạm vi ứng dụng của RL trong thực tế.
