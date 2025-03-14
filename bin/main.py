import json
import random
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageTk


class Box:
    index = 0  # 类变量，用于记录按钮的索引
    row = 1  # 类变量，用于记录当前行
    column = 1  # 类变量，用于记录当前列

    def __init__(self, box_info: str, window: tk.Tk):
        """
        :param box_info: 盒子内部显示信息
        :param window: 窗口
        """
        self.info = box_info  # 按钮的文本信息
        self.window = window  # 主窗口
        self.photo = None  # 用于保存图片引用，防止被垃圾回收
        self.button = None  # 用于保存按钮引用
        self.label = None  # 用于保存标签引用

    def get_index(self) -> int:
        return self.index

    def load_and_resize_image(self, path: str, size: tuple):
        """加载并缩放图片"""
        image = Image.open(path)
        resized_image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def registered_box(self):
        Box.index += 1
        self.index = Box.index  # 按钮的索引

        self.photo = self.load_and_resize_image("../img/box_closed.png", (100, 100))

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
        if Box.column > 6:
            Box.column = 1
            Box.row += 2

    def on_button_click(self):
        """按钮点击事件处理"""
        self.button.config(state=tk.DISABLED)
        self.label.config(text=self.info)
        showinfo(f'箱子{self.index}', self.info)


def show_error_info(error_info: str):
    """显示错误信息"""
    print(f'[Error] {error_info}')
    showerror('Error', error_info)


if __name__ == '__main__':
    try:
        # Example data
        # prize_list = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10',
        #               'test11', 'test12']
        # Use prizes.json file's data
        with open('../data/prizes.json', 'r') as f:
            prize_list = json.load(f)
        random.shuffle(prize_list)

        root = tk.Tk()
        root.title("抽奖")
        root.geometry('800x600')
        root.resizable(False, False)

        # 创建并注册按钮
        boxes = []  # 用于保存所实例化对象
        for info in prize_list:
            box = Box(info, root)
            boxes.append(box)
            box.registered_box()  # 注册按钮并显示
        root.mainloop()
    except Exception as e:
        show_error_info(f'遇到错误\n{str(e)}')
