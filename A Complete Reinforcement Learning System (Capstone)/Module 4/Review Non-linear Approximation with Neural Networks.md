# Tổng quan về Phi tuyến hóa với Mạng Nơ-ron trong RL

Bài viết này tập trung vào vai trò của mạng nơ-ron trong việc xây dựng các đặc trưng phi tuyến cho các bài toán học tăng cường.

## Cách mạng nơ-ron tạo đặc trưng

Mạng nơ-ron học cách biểu diễn dữ liệu bằng cách nhân các đầu vào với trọng số, sau đó áp dụng các hàm kích hoạt phi tuyến. Mỗi nút trong mạng sẽ tạo ra một đặc trưng riêng biệt, và tập hợp các đặc trưng này tạo nên một không gian biểu diễn mới cho dữ liệu.

## So sánh với Tile Coding

- Tile coding và mạng nơ-ron đều sử dụng các tham số cố định để tạo đặc trưng, nhưng mạng nơ-ron có thể điều chỉnh các tham số này trong quá trình huấn luyện.
- Nhờ tính phi tuyến, mạng nơ-ron có thể mô hình hóa các mối quan hệ phức tạp hơn nhiều so với các tổ hợp tuyến tính của tile coding.

## Ý nghĩa của trọng số trong mạng nơ-ron

- Mỗi đầu vào được gán một trọng số, xác định mức độ ảnh hưởng của nó lên đầu ra của từng nút.
- Tổng có trọng số được đưa qua hàm kích hoạt phi tuyến để tạo ra đầu ra.
- Trong quá trình huấn luyện, các trọng số này được cập nhật liên tục dựa trên sai số dự đoán, giúp mạng thích nghi tốt hơn với dữ liệu.

## Quy trình huấn luyện mạng nơ-ron

1. **Lan truyền xuôi (Forward Propagation):**
   - Dữ liệu đầu vào đi qua từng lớp của mạng, mỗi nút tính tổng có trọng số và áp dụng hàm kích hoạt.
2. **Tính toán hàm mất mát:**
   - So sánh đầu ra của mạng với giá trị mục tiêu để xác định sai số.
3. **Lan truyền ngược (Backpropagation):**
   - Tính đạo hàm của hàm mất mát theo từng trọng số, truyền ngược sai số qua các lớp.
4. **Cập nhật trọng số:**
   - Sử dụng các thuật toán tối ưu hóa như SGD, Adam để điều chỉnh trọng số dựa trên gradient và learning rate.
5. **Lặp lại:**
   - Quá trình này được lặp lại nhiều lần cho đến khi mạng đạt hiệu suất mong muốn.

## Kết luận

Mạng nơ-ron là công cụ mạnh mẽ để xây dựng các đặc trưng phi tuyến, giúp mô hình hóa các quan hệ phức tạp trong dữ liệu. Khả năng tự động điều chỉnh trọng số trong quá trình học giúp mạng thích nghi tốt hơn so với các phương pháp đặc trưng cố định như tile coding.
