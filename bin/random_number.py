import os.path
import tkinter as tk
from tkinter import messagebox
import webbrowser
import pandas as pd
import random


def main():
    def show_selected():
        # 获取用户选择的性别
        selected_sex = sex_selected_value.get()
        # 获取用户选择的显示方式
        display_type = name_or_number.get()
        # 获取用户输入的抽取个数
        try:
            num_to_select = int(entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return

        # 根据性别筛选学生
        if selected_sex == "随机":
            filtered_students = students  # 不筛选性别
        else:
            filtered_students = [student for student in students if student['性别'] == selected_sex]

        # 检查抽取个数是否超过可抽取的学生数量
        if num_to_select > len(filtered_students):
            messagebox.showerror("错误", f"抽取人数不能超过{len(filtered_students)}")
            return

        # 随机抽取学生
        selected_students = random.sample(filtered_students, num_to_select)

        # 根据显示方式生成结果
        result = []
        for student in selected_students:
            if display_type == '学号':
                result.append(f"学号: {student['学号']}")
            else:
                result.append(f"姓名: {student['姓名']}")

        # 将结果按每行最多 5 个进行换行
        formatted_result = []
        for i in range(0, len(result), 5):  # 每行最多 5 个
            formatted_result.append("  |  ".join(result[i:i + 5]))
        formatted_result = "\n".join(formatted_result)

        # 显示结果
        result_label.config(text=formatted_result, font=("Arial", 20), fg="blue")

    try:
        if os.path.exists('../data/students.xlsx'):
            file_path = '../data/students.xlsx'
            df = pd.read_excel(file_path)
            hard_data = df.columns.to_list()
            if '学号' not in hard_data or '性别' not in hard_data or '姓名' not in hard_data:
                messagebox.showinfo('提示', '花名册已存在，但读取数据时出错，请检查花名册是否符合要求')
                exit(0)
            else:
                # 将学生数据转换为字典列表
                students = df.to_dict('records')

            # GUI
            root = tk.Tk()
            root.title('抽号机')
            root.geometry("1200x400")  # 设置窗口大小

            # 结果显示标签（放在顶部）
            result_label = tk.Label(root, text="", font=("Arial", 20), fg="blue")
            result_label.pack(pady=20)

            # 创建一个 Frame 用于放置筛选条件、输入框和按钮（横向排列）
            control_frame = tk.Frame(root)
            control_frame.pack(pady=10)

            # 性别筛选
            sex_selected_value = tk.StringVar(value="男")
            lable_text1 = tk.Label(control_frame, text='筛选性别:')
            lable_text1.grid(row=0, column=0, padx=5)
            sex_selected_option1 = tk.Radiobutton(control_frame, text="男生", variable=sex_selected_value, value="男")
            sex_selected_option2 = tk.Radiobutton(control_frame, text="女生", variable=sex_selected_value, value="女")
            sex_selected_option3 = tk.Radiobutton(control_frame, text="随机", variable=sex_selected_value, value="随机")
            sex_selected_option1.grid(row=0, column=1, padx=5)
            sex_selected_option2.grid(row=0, column=2, padx=5)
            sex_selected_option3.grid(row=0, column=3, padx=5)

            # 显示方式
            name_or_number = tk.StringVar(value='学号')
            lable_text2 = tk.Label(control_frame, text='显示方式:')
            lable_text2.grid(row=0, column=4, padx=5)
            name_or_number_selected_option1 = tk.Radiobutton(control_frame, text='学号', variable=name_or_number,
                                                             value='学号')
            name_or_number_selected_option2 = tk.Radiobutton(control_frame, text='姓名', variable=name_or_number,
                                                             value='姓名')
            name_or_number_selected_option1.grid(row=0, column=5, padx=5)
            name_or_number_selected_option2.grid(row=0, column=6, padx=5)

            # 抽取个数输入框
            entry_label = tk.Label(control_frame, text="抽取个数:")
            entry_label.grid(row=0, column=7, padx=5)
            entry = tk.Entry(control_frame, width=10)
            entry.grid(row=0, column=8, padx=5)

            # 提交按钮
            button = tk.Button(control_frame, text="抽取", command=show_selected)
            button.grid(row=0, column=9, padx=10)

            # 运行主循环
            root.mainloop()

        else:
            if messagebox.askquestion('提示', '未检测到花名册，是否添加？') == 'yes':
                webbrowser.open(f'file://{os.path.abspath("../web/Example.html")}')
                exit(0)

    except Exception as e:
        messagebox.showerror('Error', f'遇到错误\n{e}')


if __name__ == '__main__':
    main()
