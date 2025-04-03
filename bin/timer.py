import tkinter as tk
import time

hour = 0
minute = 0
second = 0
milliseconds = 0
start_time = 0
running = False

root = tk.Tk()
control_frame = tk.Frame(root)
root.geometry('500x150')
root.title('计时器')

control_button = tk.Button(control_frame, text='开始')
clean_button = tk.Button(control_frame, text='清零')

# time
hour_text = tk.Label(control_frame, text=f'{hour:02d}', font=('', 20, 'bold'))
minute_text = tk.Label(control_frame, text=f'{minute:02d}', font=('', 20, 'bold'))
second_text = tk.Label(control_frame, text=f'{second:02d}', font=('', 20, 'bold'))
milliseconds_text = tk.Label(control_frame, text=f'{milliseconds:03d}', font=('', 20, 'bold'))


def toggle_timer():
    global running, start_time
    running = not running
    control_button.config(text='暂停' if running else '开始')
    if running:
        start_time = time.perf_counter() - (hour * 3600 + minute * 60 + second + milliseconds / 1000)
        update_time()


def clean():
    global running, hour, minute, second, milliseconds
    running = False
    hour = minute = second = milliseconds = 0
    hour_text.config(text='00')
    minute_text.config(text='00')
    second_text.config(text='00')
    milliseconds_text.config(text='000')
    control_button.config(text='开始')


control_button.config(command=toggle_timer)
clean_button.config(command=clean)


def update_time():
    if running:
        elapsed = time.perf_counter() - start_time
        global hour, minute, second, milliseconds

        # 计算各时间单位
        hour = int(elapsed // 3600)
        remaining = elapsed % 3600
        minute = int(remaining // 60)
        remaining = remaining % 60
        second = int(remaining)
        milliseconds = int((remaining - second) * 1000)

        hour_text.config(text=f'{hour:02d}')
        minute_text.config(text=f'{minute:02d}')
        second_text.config(text=f'{second:02d}')
        milliseconds_text.config(text=f'{milliseconds:03d}')

        root.after(10, update_time)


if __name__ == '__main__':
    control_frame.pack(pady=10)
    hour_text.grid(row=0, column=0)

    separated_text1 = tk.Label(control_frame, text=':', font=('', 20, 'bold'))
    separated_text1.grid(row=0, column=1)

    minute_text.grid(row=0, column=2)
    separated_text2 = tk.Label(control_frame, text=':', font=('', 20, 'bold'))
    separated_text2.grid(row=0, column=3)

    second_text.grid(row=0, column=4)
    separated_text3 = tk.Label(control_frame, text=':', font=('', 20, 'bold'))
    separated_text3.grid(row=0, column=5)

    milliseconds_text.grid(row=0, column=6)

    control_button.grid(row=1, column=2)
    clean_button.grid(row=2, column=2)
    root.mainloop()
