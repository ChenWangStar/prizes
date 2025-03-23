import os
import tkinter as tk
import webbrowser
from tkinter import messagebox
from datetime import datetime


def main_loop():
    file_path = os.path.abspath('.')
    output_directory_path = os.path.abspath('../output/')
    template_path = os.path.join(file_path, '../attendance/new_evening.html')

    root = tk.Tk()
    # component
    tk.Label(root, text='班级总人数').pack()
    number_of_class = tk.Entry(root, width=10)
    number_of_class.pack()

    tk.Label(root, text='签到终止时间(小时)').pack()
    time_hour = tk.Entry(root, width=10)
    time_hour.pack()

    tk.Label(root, text='签到终止时间(分钟)').pack()
    time_min = tk.Entry(root, width=10)
    time_min.pack()

    def on_click():
        try:
            number = int(number_of_class.get())
            time_h = int(time_hour.get())
            time_m = int(time_min.get())
            if not (0 <= time_h < 24 and 0 <= time_m < 60):
                raise ValueError("时间输入无效：小时应在 0-23 之间，分钟应在 0-59 之间")
            if number <= 0:
                raise ValueError("班级人数必须大于 0")

            with open(template_path, 'r', encoding='utf-8') as f:
                template = f.read().split('\n')
            for i, line in enumerate(template):
                if '到的同学请点击自己的学号进行签到' in line:
                    template[i] = f'<h2 class="title">在{time_h}:{time_m}前到的同学请点击自己的学号进行签到</h2>'
                if 'const userList' in line:
                    template[i] = f'    const userList = {[i + 1 for i in range(number)]}'
                if 'todayEndTime.setHours' in line:
                    template[i] = f'    todayEndTime.setHours({time_h})'
                if 'todayEndTime.setMinutes' in line:
                    template[i] = f'    todayEndTime.setMinutes({time_m})'
            output_file_path = os.path.join(output_directory_path, f'{number}_{time_h}_{time_m}.html').replace('\\',
                                                                                                               '//')
            print(output_file_path)
            with open(output_file_path, 'w',
                      encoding='utf-8') as f:
                f.write('\n'.join(template))
            if tk.messagebox.askyesno('提示', '生成成功,是否打开签到页面?'):
                webbrowser.open(f'file://{output_directory_path}')
            else:
                exit(0)

        except Exception as e:
            messagebox.showerror('错误', str(e))

    tk.Button(root, text='生成', command=on_click).pack()
    root.title('签到生成')
    root.geometry('300x200')
    root.mainloop()


if __name__ == '__main__':
    main_loop()
