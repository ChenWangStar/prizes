import tkinter as tk
from PIL import Image, ImageTk
import random
import os, json
from tkinter import messagebox

# 奖品列表
prizes = []

if os.path.exists('../data/prizes.json'):
    try:
        with open('../data/prizes.json', 'r') as f:
            prizes = json.load(f)
    except Exception as e:
        print('Failed to load prizes.json:', e)
        messagebox.showerror('Error', f'Failed to load prizes.json:\n{e}')
        exit()
else:
    print('prizes.json file is not exists.')
    messagebox.showerror('Error', 'prize.json file is not exists.')
    exit()

if len(prizes) == 0:
    print('prizes list is empty.')
    messagebox.showerror('Error', 'prizes list is empty.')
    exit()


def wrap_text_based_on_pixel_width(text, font, max_width):
    words = text
    wrapped_text = ""
    line_width = 0

    for word in words:
        # 创建一个临时的Tkinter标签来测量单词宽度
        temp_label = tk.Label(root, text=word, font=font)
        temp_label.grid(row=0, column=0)  # 使用grid来布局标签
        root.update_idletasks()  # 更新root以获取标签的尺寸
        word_width = temp_label.winfo_width()  # 获取标签的宽度
        temp_label.grid_forget()  # 从grid中移除临时标签

        if line_width + word_width > max_width:
            wrapped_text += "\n" + word  # 如果单词超过了最大宽度，则换行
            line_width = word_width
        else:
            if wrapped_text:
                wrapped_text += " " + word  # 在单词之间添加空格
            else:
                wrapped_text = word  # 开始新的一行
            line_width += word_width

    return wrapped_text

    return wrapped_text


# 随机打乱奖品列表
random.shuffle(prizes)

# 创建主窗口
root = tk.Tk()
root.title('抽奖')
root.geometry('1920x1080')

# 加载背景GIF图
background_image = Image.open('../img/background.gif')
background_photo = ImageTk.PhotoImage(background_image)

# 创建背景Label
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)


# 定义点击礼盒的函数
def open_box(box, prize_label):
    if box['state'] != 'disabled':
        prize = box.prize
        font = ('Arial', 31)  # 定义字体和大小
        max_width = 190  # 礼盒的最大宽度，以字符数为单位
        wrapped_prize = wrap_text_based_on_pixel_width(prize, font, max_width)

        # 如果奖品尚未被抽走，则分配奖品
        prize_label.config(text=wrapped_prize, bg='white', font=('Arial', 31))
        prize_label.place(x=box.winfo_x(), y=box.winfo_y(), anchor='nw')

        box['state'] = 'disabled'  # 禁用按钮，防止重复抽奖
        box.prize = None  # 清空奖品，防止重复分配


# 创建与奖品数量相等的礼盒
desired_size = (200, 200)  # 设置您希望显示的图像大小
boxes = []
prize_labels = []
row, col = 0, 0  # 当前行和列
max_boxes_per_row = 8  # 每行的最大礼盒数量

for prize in prizes:
    # 加载礼盒图片
    box_image = Image.open('../img/box_closed.png')  # 礼盒图片路径
    box_image = box_image.resize(desired_size, Image.Resampling.LANCZOS)  # 调整图像大小
    box_photo = ImageTk.PhotoImage(box_image)

    # 创建按钮
    box = tk.Button(root, image=box_photo, borderwidth=0, highlightthickness=0)
    box.image = box_photo  # 保持对图片的引用
    box.grid(row=row, column=col, padx=10, pady=10)
    box.prize = prize  # 将奖品关联到按钮上
    boxes.append(box)

    # 创建奖品Label
    prize_label = tk.Label(root, text='', font=('Helvetica', 18), bg='white', fg='black')
    prize_label.place_forget()  # 初始时隐藏奖品标签
    prize_labels.append(prize_label)

    # 设置按钮的命令
    box.config(command=lambda b=box, pl=prize_label: open_box(b, pl))

    col += 1  # 移动到下一列
    if col >= max_boxes_per_row:  # 如果达到最大列数
        col = 0  # 重置列数
        row += 1  # 移动到下一行

# 运行主循环
root.mainloop()
