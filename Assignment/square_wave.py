#######################################################################
# Bản quyền (C)                                                       #
# 2016-2018 Shangtong Zhang(zhangshangtong.cpp@gmail.com)             #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Cho phép chỉnh sửa code miễn là giữ lại phần khai báo này ở đầu      #
#######################################################################

# Import các thư viện cần thiết
import numpy as np                    # Thư viện tính toán số học
import matplotlib                     # Thư viện vẽ biểu đồ
matplotlib.use('Agg')                # Sử dụng backend Agg để render hình ảnh
import matplotlib.pyplot as plt       # Module pyplot để vẽ biểu đồ
from tqdm import tqdm                 # Thư viện hiển thị thanh tiến trình

# Lớp wrapper cho một khoảng (interval)
# Tính dễ đọc quan trọng hơn hiệu suất, nên không sử dụng nhiều thủ thuật
class Interval:
    # [@left, @right) - khoảng từ left đến right (không bao gồm right)
    def __init__(self, left, right):
        self.left = left              # Điểm bắt đầu của khoảng
        self.right = right            # Điểm kết thúc của khoảng

    # Kiểm tra xem một điểm có nằm trong khoảng này không
    def contain(self, x):
        return self.left <= x < self.right    # Trả về True nếu x nằm trong [left, right)

    # Độ dài của khoảng này
    def size(self):
        return self.right - self.left         # Tính kích thước khoảng

# Miền của sóng vuông, [0, 2)
DOMAIN = Interval(0.0, 2.0)

# Hàm sóng vuông
def square_wave(x):
    if 0.5 < x < 1.5:                # Nếu x nằm trong khoảng (0.5, 1.5)
        return 1                     # Trả về 1
    return 0                         # Ngược lại trả về 0

# Lấy @n mẫu ngẫu nhiên từ sóng vuông
def sample(n):
    samples = []                     # Danh sách chứa các mẫu
    for i in range(0, n):           # Lặp n lần
        x = np.random.uniform(DOMAIN.left, DOMAIN.right)  # Tạo x ngẫu nhiên trong miền
        y = square_wave(x)           # Tính giá trị y tương ứng
        samples.append([x, y])       # Thêm cặp [x, y] vào danh sách mẫu
    return samples                   # Trả về danh sách mẫu

# Lớp wrapper cho hàm giá trị (value function)
class ValueFunction:
    # @domain: miền của hàm này, một instance của Interval
    # @alpha: bước cơ bản cho một lần cập nhật
    def __init__(self, feature_width, domain=DOMAIN, alpha=0.2, num_of_features=50):
        self.feature_width = feature_width      # Độ rộng của mỗi feature window
        self.num_of_featrues = num_of_features  # Số lượng features (lỗi typo: featrues)
        self.features = []                      # Danh sách các feature windows
        self.alpha = alpha                      # Tốc độ học (learning rate)
        self.domain = domain                    # Miền của hàm

        # Có nhiều cách để đặt các feature windows,
        # dưới đây chỉ là một cách có thể
        step = (domain.size() - feature_width) / (num_of_features - 1)  # Bước nhảy giữa các features
        left = domain.left                      # Điểm bắt đầu
        for i in range(0, num_of_features - 1): # Tạo các feature windows
            self.features.append(Interval(left, left + feature_width))  # Thêm feature window
            left += step                        # Dịch chuyển điểm bắt đầu
        self.features.append(Interval(left, domain.right))  # Feature cuối cùng

        # Khởi tạo trọng số cho mỗi feature
        self.weights = np.zeros(num_of_features)    # Mảng trọng số ban đầu = 0

    # Với điểm @x, trả về chỉ số của các feature windows tương ứng
    def get_active_features(self, x):
        active_features = []                    # Danh sách các features hoạt động
        for i in range(0, len(self.features)):  # Duyệt qua tất cả features
            if self.features[i].contain(x):     # Nếu x nằm trong feature i
                active_features.append(i)       # Thêm chỉ số i vào danh sách
        return active_features                  # Trả về danh sách features hoạt động

    # Ước lượng giá trị cho điểm @x
    def value(self, x):
        active_features = self.get_active_features(x)   # Lấy các features hoạt động
        return np.sum(self.weights[active_features])    # Tổng trọng số của các features hoạt động

    # Cập nhật trọng số dựa trên mẫu tại điểm @x
    # @delta: y - x (sai số)
    def update(self, delta, x):
        active_features = self.get_active_features(x)   # Lấy các features hoạt động
        delta *= self.alpha / len(active_features)      # Điều chỉnh delta theo learning rate
        for index in active_features:                   # Với mỗi feature hoạt động
            self.weights[index] += delta                # Cập nhật trọng số

# Huấn luyện @value_function với tập mẫu @samples
def approximate(samples, value_function):
    for x, y in samples:                        # Với mỗi cặp mẫu (x, y)
        delta = y - value_function.value(x)     # Tính sai số
        value_function.update(delta, x)         # Cập nhật hàm giá trị

# Hình 9.8
def figure_9_8():
    num_of_samples = [10, 40, 160, 640, 2560, 10240]   # Các số lượng mẫu khác nhau
    feature_widths = [0.2, 0.4, 1.0]                   # Các độ rộng feature khác nhau
    plt.figure(figsize=(30, 20))                        # Tạo figure với kích thước lớn
    axis_x = np.arange(DOMAIN.left, DOMAIN.right, 0.02) # Trục x để vẽ biểu đồ
    for index, num_of_sample in enumerate(num_of_samples): # Với mỗi số lượng mẫu
        print(num_of_sample, 'samples')                 # In số lượng mẫu hiện tại
        samples = sample(num_of_sample)                 # Tạo mẫu ngẫu nhiên
        value_functions = [ValueFunction(feature_width) for feature_width in feature_widths] # Tạo các hàm giá trị
        plt.subplot(2, 3, index + 1)                    # Tạo subplot
        plt.title('%d samples' % (num_of_sample))       # Đặt tiêu đề cho subplot
        for value_function in value_functions:          # Với mỗi hàm giá trị
            approximate(samples, value_function)        # Huấn luyện hàm giá trị
            values = [value_function.value(x) for x in axis_x] # Tính giá trị cho tất cả điểm x
            plt.plot(axis_x, values, label='feature width %.01f' % (value_function.feature_width)) # Vẽ đường
        plt.legend()                                    # Hiển thị chú thích

    plt.savefig(r'D:\reinforcement-learning-an-introduction\images.png') # Lưu hình ảnh
    plt.close()                                         # Đóng figure

if __name__ == '__main__':                             # Nếu chạy file này trực tiếp
    figure_9_8()                                        # Gọi hàm vẽ hình 9.8