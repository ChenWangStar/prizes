def run_mainloop():
    import json
    import os
    import re

    # 定义一个函数来添加prize

    # 定义一个函数来检查字符串是否包含单引号
    import tkinter as tk
    from tkinter import messagebox

    # 定义两个函数来检查字符串是否包含单引号或空值
    def contains_single_quote(s):
        return re.search(r"'", s) is not None

    def is_empty(s):
        return not s

    # 定义一个函数来添加prize
    def add_prize():
        prize = prize_entry.get()
        if is_empty(prize):
            messagebox.showerror('Error', '奖品名称不得为空')
        elif contains_single_quote(prize):
            messagebox.showerror('Error', '奖品名不得包含单引号')
        else:
            prizes.append(prize)
            prize_listbox.insert(tk.END, prize)
            prize_entry.delete(0, tk.END)

    # 定义一个函数来删除prize
    def delete_prize():
        selected_indices = prize_listbox.curselection()
        for index in selected_indices:
            prize = prize_listbox.get(index)
            prizes.remove(prize)
            prize_listbox.delete(index)

    # 定义一个函数来加载prizes列表
    def load_prizes():
        global prizes
        prizes = load_prizes_from_json(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/prizes.json'))
        prize_listbox.delete(0, tk.END)
        for prize in prizes:
            prize_listbox.insert(tk.END, prize)

    # 定义一个函数来保存prizes列表
    def save_prizes():
        save_prizes_to_json(prizes, os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/prizes.json'))
        messagebox.showinfo("保存成功", "奖品已成功保存")

    # 定义一个函数来从JSON文件中读取prizes列表
    def load_prizes_from_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                prizes = json.load(f)
            return prizes
        else:
            return []

    # 定义一个函数来将prizes列表转换为JSON格式
    def save_prizes_to_json(prizes, file_path):
        with open(file_path, 'w') as f:
            json.dump(prizes, f)

    # 创建主窗口
    root = tk.Tk()
    root.title('Prize Manager')

    # 创建一个列表框来显示prizes
    prize_listbox = tk.Listbox(root, height=6, width=35, border=0)
    prize_listbox.pack(pady=10)

    # 创建一个文本框来输入prize
    prize_entry = tk.Entry(root, width=35)
    prize_entry.pack(pady=10)

    # 创建一个按钮来添加prize
    add_button = tk.Button(root, text='添加', command=add_prize)
    add_button.pack(pady=10)

    # 创建一个按钮来删除prize
    delete_button = tk.Button(root, text='删除', command=delete_prize)
    delete_button.pack(pady=10)

    # 创建一个按钮来加载prizes列表
    load_button = tk.Button(root, text='加载', command=load_prizes)
    load_button.pack(pady=10)

    # 创建一个按钮来保存prizes列表
    save_button = tk.Button(root, text='保存', command=save_prizes)
    save_button.pack(pady=10)

    # 定义一个全局变量来存储prizes列表
    prizes = []

    # 加载prizes列表
    load_prizes()

    root.mainloop()


if __name__ == '__main__':
    run_mainloop()
