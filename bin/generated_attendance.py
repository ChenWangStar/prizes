import os


def generate_html(template_path, end_time, num_people):
    """
    根据模板文件生成一个动态调整结束时间和人数的签到 HTML 文件。

    :param template_path: 模板文件的路径。
    :param end_time: 签到结束时间，格式为 "HH:MM"（例如 "18:50"）。
    :param num_people: 签到人数。
    """
    # 读取模板文件
    with open(template_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # 替换模板中的结束时间和人数
    html_content = html_content.replace("在18:50前到的同学请点击自己的学号进行签到",
                                        f"在{end_time}前到的同学请点击自己的学号进行签到")

    # 生成动态人数的用户列表
    user_list = list(range(1, num_people + 1))
    html_content = html_content.replace(
        "const userList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59];",
        f"const userList = {user_list};"
    )

    # 提取用户输入的小时和分钟
    end_hour = int(end_time.split(":")[0])
    end_minute = int(end_time.split(":")[1])

    # 替换计时器逻辑中的结束时间
    # 查找并替换 todayEndTime.setHours 和 todayEndTime.setMinutes
    target_line_hours = "todayEndTime.setHours(18);"
    target_line_minutes = "todayEndTime.setMinutes(50);"
    new_line_hours = f"todayEndTime.setHours({end_hour});"
    new_line_minutes = f"todayEndTime.setMinutes({end_minute});"

    html_content = html_content.replace(target_line_hours, new_line_hours)
    html_content = html_content.replace(target_line_minutes, new_line_minutes)

    # 保存生成的 HTML 文件
    output_file = f"evening_signin_{end_time.replace(':', '')}_{num_people}people.html"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"已生成文件: {output_file}")


if __name__ == "__main__":
    # 模板文件路径
    template_path = "../attendance/new_evening.html"

    # 检查模板文件是否存在
    if not os.path.exists(template_path):
        print(f"错误：模板文件 '{template_path}' 不存在！")
        exit(1)

    # 用户输入结束时间和人数
    end_time = input("请输入签到结束时间（格式为 HH:MM，例如 18:50）：")
    num_people = int(input("请输入签到人数："))

    # 生成 HTML 文件
    generate_html(template_path, end_time, num_people)