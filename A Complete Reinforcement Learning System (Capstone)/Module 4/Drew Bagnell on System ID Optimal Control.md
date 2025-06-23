# Tổng quan về bài giảng Drew Bagnell: Nhận diện hệ thống và điều khiển tối ưu

Bài viết này đề cập đến quá trình xây dựng mô hình trong reinforcement learning dựa trên mô hình, nhấn mạnh các phương pháp thực tiễn và khái niệm học không hối tiếc (No-Regret learning).

## Quá trình xây dựng mô hình trong RL

- Bài giảng lấy ví dụ về điều khiển trực thăng tự động để minh họa cho việc học mô hình động lực môi trường.
- Phương pháp truyền thống (system identification) là một dạng học có giám sát, thu thập dữ liệu từ các chính sách thăm dò và xây dựng mô hình dựa trên dữ liệu đó.
- Tuy nhiên, các kỹ sư thực tế thường áp dụng phương pháp lặp lại: liên tục thu thập dữ liệu mới, cập nhật mô hình và tối ưu hóa chính sách qua nhiều vòng.

## Thách thức và giải pháp tương tác

- Việc xây dựng mô hình chính xác gặp khó khăn khi dữ liệu ở các trạng thái ít xuất hiện bị thiếu, dẫn đến mô hình không phản ánh đúng thực tế và chính sách tối ưu hóa trên mô hình này có thể thất bại khi áp dụng thật.
- Để khắc phục, cần tiếp cận theo hướng tương tác: vừa thu thập dữ liệu từ chính sách hiện tại, vừa kết hợp với dữ liệu thăm dò, liên tục cập nhật mô hình và chính sách.
- Cách làm này giúp mô hình và chính sách ngày càng phù hợp hơn với thực tế, giống với quy trình của các kỹ sư chuyên nghiệp.

## Học không hối tiếc (No-Regret Learning)

- No-Regret learning là nhóm thuật toán đảm bảo rằng hiệu suất trung bình của tác tử sẽ tiệm cận hiệu suất của chiến lược tốt nhất trong quá khứ khi số lần lặp tăng lên.
- Đặc trưng:
  - **Ổn định**: Không bị ảnh hưởng nhiều bởi các thay đổi nhỏ trong dữ liệu huấn luyện.
  - **Hiệu quả lâu dài**: Càng nhiều dữ liệu, hiệu suất càng tốt.
  - **Khả năng thích nghi**: Điều chỉnh chiến lược dựa trên kết quả thực tế.
- No-Regret learning giúp hệ thống RL vận hành ổn định và hiệu quả hơn trong môi trường thực tế.

## Tổng kết

- Quá trình học mô hình trong RL nên được thực hiện theo cách lặp lại, liên tục cập nhật dữ liệu và tối ưu hóa chính sách.
- Áp dụng các thuật toán No-Regret giúp đảm bảo hiệu suất ổn định, thích nghi tốt với môi trường thực tế.
- Phương pháp này đã được kiểm chứng hiệu quả qua các ví dụ thực tiễn như điều khiển trực thăng tự động.
