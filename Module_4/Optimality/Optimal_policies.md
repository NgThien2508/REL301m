# Chính Sách Tối Ưu (Optimal Policies) Trong RL

## 1. Khái Niệm Về Chính Sách (Policy)

### 1.1. Định Nghĩa Cơ Bản
Chính sách (π) là một quy tắc quyết định:
- Xác định hành vi của agent
- Ánh xạ từ trạng thái đến hành động
- Có thể là định tính hoặc xác suất

### 1.2. Vai Trò Của Chính Sách
- Hướng dẫn agent trong quá trình ra quyết định
- Quyết định hiệu suất của agent
- Cơ sở để tính toán hàm giá trị

## 2. So Sánh Giữa Các Chính Sách

### 2.1. Tiêu Chí So Sánh
Chính sách π₁ tốt hơn hoặc bằng π₂ khi và chỉ khi:
$$V^{\pi_1}(s) \geq V^{\pi_2}(s), \forall s \in S$$

#### Ý nghĩa:
- So sánh dựa trên giá trị trạng thái
- Phải tốt hơn ở MỌI trạng thái
- Không chỉ tốt hơn ở một số trạng thái

### 2.2. Ví Dụ Minh Họa
```python
# Giả sử có hai chính sách trong môi trường grid world
π₁ = {
    's1': 'RIGHT',  # V(s1) = 10
    's2': 'UP',     # V(s2) = 8
    's3': 'LEFT'    # V(s3) = 12
}

π₂ = {
    's1': 'DOWN',   # V(s1) = 8
    's2': 'RIGHT',  # V(s2) = 7
    's3': 'UP'      # V(s3) = 10
}

# π₁ tốt hơn π₂ vì V^π₁(s) > V^π₂(s) với mọi s
```

## 3. Chính Sách Tối Ưu (π*)

### 3.1. Định Nghĩa
Chính sách tối ưu là chính sách tốt hơn hoặc bằng mọi chính sách khác:
$$\pi^* = \arg\max_\pi V^\pi(s), \forall s \in S$$

### 3.2. Đặc Điểm
- Luôn tồn tại ít nhất một chính sách tối ưu
- Có thể có nhiều chính sách tối ưu
- Có thể là chính sách định tính

## 4. Ví Dụ Chi Tiết: Two-Choice MDP

### 4.1. Mô Tả Môi Trường
```
[State X]
   /    \
A1(+1)  A2(0)
   |     |
[State Y] [State Z]
   |     |
A1(0)   A1(+2)
   \    /
    [X]
```

### 4.2. Phân Tích Với γ = 0
#### Chính sách π₁ (chọn A1 tại X):
```python
V^π₁(X) = 1  # Phần thưởng tức thời
V^π₁(Y) = 0  # Không có phần thưởng
```

#### Chính sách π₂ (chọn A2 tại X):
```python
V^π₂(X) = 0  # Không có phần thưởng tức thời
V^π₂(Z) = 2  # Không được tính vì γ = 0
```

### 4.3. Phân Tích Với γ = 0.9
#### Chính sách π₁:
$$V^{\pi_1}(X) = 1 + 0 + \gamma + 0 + \gamma^2 + ... = \frac{1}{1-\gamma^2} \approx 5.3$$

#### Chính sách π₂:
$$V^{\pi_2}(X) = 0 + 2\gamma + 0 + 2\gamma^3 + ... = \frac{2\gamma}{1-\gamma^2} \approx 9.5$$

## 5. Tại Sao Luôn Tồn Tại Chính Sách Tối Ưu?

### 5.1. Nguyên Lý Kết Hợp
Giả sử có hai chính sách π₁ và π₂:
```python
def combine_policies(π₁, π₂, state):
    if V^π₁(state) > V^π₂(state):
        return π₁(state)
    else:
        return π₂(state)
```

### 5.2. Tính Chất Quan Trọng
- Không có trade-off giữa các trạng thái
- Luôn có thể tạo chính sách tốt hơn bằng cách kết hợp
- Tồn tại điểm bất động trong không gian chính sách

## 6. Thách Thức Trong Tìm Kiếm Chính Sách Tối Ưu

### 6.1. Độ Phức Tạp
Với không gian rời rạc:
- Số chính sách = |A|^|S|
- |A|: số hành động có thể
- |S|: số trạng thái

### 6.2. Ví Dụ Cụ Thể
```python
# Grid world 4x4, 4 hành động
states = 16
actions = 4
total_policies = actions ** states  # = 4^16 ≈ 4.3 tỷ chính sách
```

## 7. Phương Pháp Tìm Kiếm Hiệu Quả

### 7.1. Value Iteration
```python
def find_optimal_policy(states, actions, rewards, transitions, gamma):
    V = initialize_values()
    while not converged:
        for s in states:
            V[s] = max([
                sum([p * (r + gamma * V[s_next])
                    for s_next, r, p in transitions(s, a)])
                for a in actions(s)
            ])
    
    # Extract policy
    policy = {}
    for s in states:
        policy[s] = argmax([
            sum([p * (r + gamma * V[s_next])
                for s_next, r, p in transitions(s, a)])
            for a in actions(s)
        ])
    return policy
```

### 7.2. Policy Iteration
```python
def policy_iteration(states, actions, rewards, transitions, gamma):
    policy = initialize_policy()
    while not converged:
        # Policy evaluation
        V = evaluate_policy(policy)
        
        # Policy improvement
        policy = improve_policy(V)
    return policy
```

## 8. Kết Luận
- Chính sách tối ưu luôn tồn tại
- Có thể có nhiều chính sách tối ưu
- Tìm kiếm trực tiếp không khả thi với không gian lớn
- Cần các phương pháp thông minh như Value/Policy Iteration

-------------------------------------------
##### Cập nhật: 5-22-2025 lúc 3PM
##### Khóa học: Fundamentals of Reinforcement Learning - Module 4
##### Tài liệu: Optimal Policies
##### Học nội dung từ clip: Optimal Policies
