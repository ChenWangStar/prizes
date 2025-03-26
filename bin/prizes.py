import json
import os.path
import time
import tkinter as tk
from tkinter import messagebox
import random
from change_the_prizes_list import run_mainloop
from PIL import Image, ImageTk


class Box:
    index = 0  # 类变量，用于记录按钮的索引
    row = 1  # 类变量，用于记录当前行
    column = 1  # 类变量，用于记录当前列

    def __init__(self, box_info: str, window: tk.Tk):
        global photo
        """
        :param box_info: 盒子内部显示信息
        :param window: 窗口
        """
        self.info = box_info  # 按钮的文本信息
        self.window = window  # 主窗口
        self.photo = None  # 用于保存图片引用，防止被垃圾回收
        self.button = None  # 用于保存按钮引用
        self.label = None  # 用于保存标签引用

        self.image = photo

    def get_index(self) -> int:
        return self.index

    def registered_box(self):
        Box.index += 1
        self.index = Box.index  # 按钮的索引
        self.photo = self.image

        self.button = tk.Button(
            self.window,
            image=self.photo,
            compound=tk.TOP,
            command=self.on_button_click  # 绑定点击事件
        )
        self.button.grid(row=Box.row, column=Box.column, padx=10, pady=10)

        # 显示 self.info
        self.label = tk.Label(self.window, text="")
        self.label.grid(row=Box.row + 1, column=Box.column)

        # 更新列和行的逻辑
        Box.column += 1
        if Box.column > 14:
            Box.column = 1
            Box.row += 2

    def on_button_click(self):
        """按钮点击事件处理"""
        self.button.config(state=tk.DISABLED)
        self.label.config(text=self.info)
        messagebox.showinfo(f'箱子{self.index}', self.info)


def show_error_info(error_info: str):
    """显示错误信息"""
    print(f'[Error] {error_info}')
    messagebox.showerror('Error', error_info)


if __name__ == '__main__':
    try:
        while True:
            if os.path.exists('../data/prizes.json'):
                with open('../data/prizes.json', 'r') as f:
                    prize_list = json.load(f)
                prize_list = [f'奖品{x}' for x in range(60)]
                if len(prize_list) == 0:
                    if messagebox.askquestion('提示', '未检测到存在奖品信息，请问需要添加吗?（否即退出）') == 'yes':
                        run_mainloop()
                    else:
                        exit(0)
                else:
                    break
            else:
                with open('../data/prizes.json', 'w') as f:
                    f.write('[]')

        random.shuffle(prize_list)

        root = tk.Tk()
        root.title("抽奖")
        root.geometry('1920x1080')
        root.resizable(False, False)

        # Load image (box_closed.png)
        image = Image.open('../resource/box_closed.png')
        resized_image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)

        # 创建并注册按钮
        boxes = []  # 用于保存所实例化对象
        t = time.time()
        for info in prize_list:
            box = Box(info, root)
            boxes.append(box)
            box.registered_box()  # 注册按钮并显示
        print(time.time() - t)
        root.mainloop()
    except Exception as e:
        show_error_info(f'遇到错误\n{str(e)}')
