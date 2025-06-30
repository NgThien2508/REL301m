import customtkinter as ctk  # Thư viện giao diện hiện đại dựa trên tkinter
from tkinter import messagebox  # Hộp thoại thông báo

class TicTacToe:
    def __init__(self, root):
        self.root = root  # Cửa sổ chính
        self.root.title('Tic Tac Toe')  # Tiêu đề cửa sổ
        self.root.geometry('500x600')  # Kích thước cửa sổ
        self.root.resizable(False, False)  # Không cho thay đổi kích thước
        ctk.set_appearance_mode("System")  # Chế độ giao diện (tối/sáng/hệ thống)
        ctk.set_default_color_theme("blue")  # Chủ đề màu sắc
        self.size = 3  # Kích thước bàn cờ mặc định
        self.win_length = 3  # Số lượng ký tự liên tiếp để thắng
        self.current_player = 'X'  # Người chơi bắt đầu
        self.board = []  # Ma trận lưu trạng thái bàn cờ
        self.buttons = []  # Ma trận các nút giao diện
        self.create_widgets()  # Tạo giao diện

    def create_widgets(self):
        # Xóa toàn bộ widget cũ trước khi tạo mới
        for widget in self.root.winfo_children():
            widget.destroy()
        # Tiêu đề
        self.title_label = ctk.CTkLabel(self.root, text='Tic Tac Toe', font=('Arial', 28, 'bold'))
        self.title_label.pack(pady=12)
        # Khung chọn chế độ
        self.mode_frame = ctk.CTkFrame(self.root)
        self.mode_frame.pack(pady=8)
        self.mode_label = ctk.CTkLabel(self.mode_frame, text="Chọn chế độ:", font=('Arial', 14))
        self.mode_label.pack(side='left', padx=5)
        # Combobox chọn kích thước bàn cờ
        self.mode_combo = ctk.CTkComboBox(self.mode_frame, values=["3x3", "5x5", "7x7"], width=80, command=self.change_mode)
        self.mode_combo.set("3x3")
        self.mode_combo.pack(side='left', padx=5)
        # Nút bắt đầu
        self.start_button = ctk.CTkButton(self.mode_frame, text="Bắt đầu", command=self.start_game, fg_color='#0d6efd', text_color='white', hover_color='#2563eb', corner_radius=12)
        self.start_button.pack(side='left', padx=10)
        # Nhãn trạng thái
        self.status_label = ctk.CTkLabel(self.root, text="Chọn chế độ và nhấn Bắt đầu", font=('Arial', 16))
        self.status_label.pack(pady=10)
        # Nút chuyển đổi chế độ tối/sáng
        self.theme_switch = ctk.CTkSwitch(self.root, text="Chế độ tối", command=self.toggle_theme)
        self.theme_switch.pack(pady=2)
        self.frame = None  # Khung chứa các nút bàn cờ
        self.reset_button = None  # Nút chơi lại

    def change_mode(self, value):
        # Thay đổi kích thước bàn cờ và số ký tự cần để thắng dựa vào lựa chọn
        if value == "3x3":
            self.size = 3
            self.win_length = 3
        else:
            self.size = int(value[0])  # Lấy số đầu tiên trong chuỗi (5 hoặc 7)
            self.win_length = 5

    def start_game(self):
        # Khởi tạo lại trạng thái game khi bắt đầu mới
        self.current_player = 'X'
        self.board = [['' for _ in range(self.size)] for _ in range(self.size)]  # Ma trận rỗng
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]  # Ma trận nút
        if self.frame:
            self.frame.destroy()  # Xóa khung cũ nếu có
        if self.reset_button:
            self.reset_button.destroy()  # Xóa nút chơi lại cũ nếu có
        self.frame = ctk.CTkFrame(self.root)  # Tạo khung mới
        self.frame.pack(pady=5)
        # Tạo các nút cho từng ô trên bàn cờ
        for i in range(self.size):
            for j in range(self.size):
                btn = ctk.CTkButton(
                    self.frame,
                    text='',
                    font=('Arial', 36 if self.size==3 else 20, 'bold'),
                    width=90 if self.size==3 else 50,
                    height=90 if self.size==3 else 50,
                    fg_color="#f8fafc",
                    text_color="#22223b",
                    corner_radius=16,
                    hover_color="#b6ccfe",
                    command=lambda row=i, col=j: self.on_click(row, col)  # Gán sự kiện click
                )
                btn.grid(row=i, column=j, padx=4, pady=4)  # Đặt vị trí nút
                self.buttons[i][j] = btn
        self.status_label.configure(text="Lượt của người chơi: X")  # Cập nhật trạng thái
        # Nút chơi lại
        self.reset_button = ctk.CTkButton(self.root, text='Chơi lại', font=('Arial', 14, 'bold'), command=self.reset_game, fg_color='#0d6efd', text_color='white', hover_color='#2563eb', corner_radius=12)
        self.reset_button.pack(pady=8)

    def toggle_theme(self):
        # Chuyển đổi giữa chế độ tối và sáng
        if self.theme_switch.get():
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def on_click(self, row, col):
        # Xử lý khi người chơi click vào một ô
        if self.buttons[row][col].cget('text') == '' and not self.check_winner():  # Nếu ô trống và chưa có người thắng
            # Đặt màu chữ: X màu đỏ, O màu xanh
            color = "#e63946" if self.current_player == "X" else "#1976d2"
            self.buttons[row][col].configure(text=self.current_player, text_color=color)  # Hiển thị ký tự người chơi với màu
            self.board[row][col] = self.current_player  # Lưu vào ma trận
            winner = self.check_winner()  # Kiểm tra thắng
            if winner:
                self.status_label.configure(text=f'Người chơi {winner} thắng!')
                messagebox.showinfo('Kết thúc', f'Người chơi {winner} đã thắng!')  # Thông báo thắng
            elif self.is_draw():
                self.status_label.configure(text='Hòa!')
                messagebox.showinfo('Kết thúc', 'Trò chơi hòa!')  # Thông báo hòa
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Đổi lượt
                self.status_label.configure(text=f"Lượt của người chơi: {self.current_player}")

    def check_winner(self):
        # Kiểm tra xem có ai thắng chưa (ngang, dọc, chéo chính, chéo phụ)
        n = self.size  # Kích thước bàn cờ
        k = self.win_length  # Số ký tự liên tiếp cần để thắng
        b = self.board  # Ma trận bàn cờ
        for i in range(n):
            for j in range(n):
                if b[i][j] == '':
                    continue  # Bỏ qua ô trống
                # Kiểm tra ngang
                if j + k <= n and all(b[i][j+x] == b[i][j] for x in range(k)):
                    return b[i][j]
                # Kiểm tra dọc
                if i + k <= n and all(b[i+x][j] == b[i][j] for x in range(k)):
                    return b[i][j]
                # Kiểm tra chéo chính
                if i + k <= n and j + k <= n and all(b[i+x][j+x] == b[i][j] for x in range(k)):
                    return b[i][j]
                # Kiểm tra chéo phụ
                if i + k <= n and j - k + 1 >= 0 and all(b[i+x][j-x] == b[i][j] for x in range(k)):
                    return b[i][j]
        return None  # Không có ai thắng

    def is_draw(self):
        # Kiểm tra hòa (không còn ô trống và không ai thắng)
        for row in self.board:
            if '' in row:
                return False
        return self.check_winner() is None

    def reset_game(self):
        # Chơi lại: tạo lại giao diện ban đầu
        self.create_widgets()

if __name__ == '__main__':
    root = ctk.CTk()  # Tạo cửa sổ chính
    app = TicTacToe(root)  # Khởi tạo game
    root.mainloop()  # Chạy vòng lặp giao diện 