import tkinter as tk

def disable_button():
    button.config(state=tk.DISABLED)  # 禁用按钮

def enable_button():
    button.config(state=tk.NORMAL)  # 启用按钮

# 创建主窗口
root = tk.Tk()
root.title("禁用按钮示例")

# 创建按钮
button = tk.Button(root, text="点击我", command=lambda: print("按钮被点击了！"))
button.pack(pady=20)

# 创建禁用按钮
disable_btn = tk.Button(root, text="禁用按钮", command=disable_button)
disable_btn.pack(pady=10)

# 创建启用按钮
enable_btn = tk.Button(root, text="启用按钮", command=enable_button)
enable_btn.pack(pady=10)

# 运行主循环
root.mainloop()