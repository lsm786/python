import random
from collections import Counter
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'AppleGothic'  # 맥 한글폰트
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 깨짐 방지

# 🎯 로또 게임 클래스 (객체지향)
class LottoGame:
    def __init__(self):
        self.history = []

    def generate_numbers(self):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        self.history.append(numbers)
        return numbers

    def get_statistics(self):
        flat_numbers = [num for game in self.history for num in game]
        counter = Counter(flat_numbers)
        return counter.most_common(6)
    
    def generate_1000(self):
        for _ in range(1000):
            self.generate_numbers()


# 🎯 객체 생성
game = LottoGame()


# 🎯 버튼 기능
def generate():
    numbers = game.generate_numbers()
    result_label.config(text=f"🎰 {numbers}")

def show_graph():
    if not game.history:
        messagebox.showinfo("그래프", "먼저 번호를 생성하세요.")
        return

    from collections import Counter

    flat_numbers = [num for game in game.history for num in game]
    counter = Counter(flat_numbers)

    top_13 = counter.most_common(13)

    numbers = [num for num, count in top_13]
    counts = [count for num, count in top_13]

    # ⭐ 막대 위치를 0~12로 고정
    x_positions = range(len(numbers))

    plt.figure()
    plt.bar(x_positions, counts)

    plt.xticks(x_positions, numbers)  # 실제 숫자는 라벨로 표시
    plt.xlabel("번호")
    plt.ylabel("출현 횟수")
    plt.title("로또 번호 출현 상위 13개 통계")

    plt.grid(axis='y', linestyle='--', alpha=0.5)

    plt.show()
    
def show_stats():
    if not game.history:
        messagebox.showinfo("통계", "먼저 번호를 생성하세요.")
        return

    stats = game.get_statistics()
    text = "\n".join([f"{num}번 : {count}회" for num, count in stats])
    messagebox.showinfo("통계 결과", text)

def auto_generate_1000():
    game.generate_1000()
    messagebox.showinfo("완료", "1000회 자동 생성 완료!")


# 🎯 GUI 설정
root = tk.Tk()
root.title("로또 프로젝트")

generate_btn = tk.Button(root, text="번호 생성", command=generate)
generate_btn.pack(pady=10)

stats_btn = tk.Button(root, text="통계 보기", command=show_stats)
stats_btn.pack(pady=10)

graph_btn = tk.Button(root, text="그래프 보기", command=show_graph)
graph_btn.pack(pady=10)

result_label = tk.Label(root, text="번호가 여기에 표시됩니다")
result_label.pack(pady=20)

auto_btn = tk.Button(root, text="1000회 자동 생성", command=auto_generate_1000)
auto_btn.pack(pady=10)

root.mainloop()
