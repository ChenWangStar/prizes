import tkinter as tk
import subprocess


def run_script(script_name):
    # 使用subprocess模块运行指定的Python脚本
    subprocess.Popen(['python', script_name], shell=True)


# 创建主窗口
root = tk.Tk()
root.title("启动器")

# 设置窗口大小
root.geometry("400x200")

# 创建抽奖按钮
btn_draw = tk.Button(root, text="抽奖", command=lambda: run_script('main.py'))
btn_draw.pack(pady=10)

# 创建抽号按钮
btn_random_number = tk.Button(root, text="抽号", command=lambda: run_script('random_number.py'))
btn_random_number.pack(pady=10)

btn_generated_attendance = tk.Button(root, text='签到', command=lambda: run_script('generated_attendance.py'))
btn_generated_attendance.pack(pady=10)

# 启动主循环
root.mainloop()
