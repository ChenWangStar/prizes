import time
import webbrowser

# 定义时间段和对应的网页
time_periods = [
    {
        'start_hour': 0, 'start_minute': 0,
        'end_hour': 7, 'end_minute': 10,
        'url': "file:///D:/attendance/new_morning_monday.html"
    },
    {
        'start_hour': 17, 'start_minute': 6,
        'end_hour': 18, 'end_minute': 50,
        'url': "file:///D:/attendance/new_evening.html"
    }
]


# 检查当前时间是否在任何一个时间段内，并在是的情况下打开对应的网页
def check_time_and_open_urls(time_periods, test=False, test_hour: int = 0, test_min: int = 0):
    if test:
        current_hour = test_hour
        current_minute = test_min
    else:
        current_hour = time.localtime().tm_hour
        current_minute = time.localtime().tm_min

    for period in time_periods:
        start_hour = period['start_hour']
        start_minute = period['start_minute']
        end_hour = period['end_hour']
        end_minute = period['end_minute']
        url = period['url']

        # 检查当前时间是否在时间段内
        if (start_hour <= current_hour < end_hour) or \
                (start_hour == current_hour and current_minute >= start_minute) or \
                (end_hour == current_hour and current_minute < end_minute):
            # 打开网页
            webbrowser.open(url)
            break  # 如果已经打开了网页，就不需要继续检查其他时间段


# 检查时间并打开网页
check_time_and_open_urls(time_periods)
