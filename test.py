import tkinter as tk
from PIL import Image, ImageTk

# 创建主窗口
root = tk.Tk()
root.title("缩放图片示例")

# 打开图片并缩放
image = Image.open("img/box_closed.png")
resized_image = image.resize((100, 100), Image.LANCZOS)  # 缩放到 100x100
photo = ImageTk.PhotoImage(resized_image)

# 创建按钮并添加缩放后的图片
button = tk.Button(root, image=photo, command=lambda: print("按钮被点击了！"))
button.pack(pady=20)

# 运行主循环
root.mainloop()