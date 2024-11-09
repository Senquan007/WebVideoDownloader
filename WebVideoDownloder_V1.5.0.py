import subprocess
import os
import re
import glob
import danmaku2ass


# 定义yt-dlp命令和相关参数
video_url = input("请输入视频链接:")  # 替换成实际的视频URL

# 构建yt-dlp命令来获取视频标题
title_command = [
    "yt-dlp",
    "--cookies", "cookies.txt",
    "--print", "title",
    "--no-download",  # 不下载视频，只获取信息
    video_url
]

# 运行命令获取视频标题
try:
    title_result = subprocess.run(title_command, capture_output=True, text=True, check=True)
    video_title = title_result.stdout.strip()  # 获取视频标题并去除首尾空白
    # 清理标题中的非法字符
    video_title = re.sub(r'[\\/:"*?<>|\']', '_', video_title)
except subprocess.CalledProcessError as e:
    print("获取视频标题失败:", e)
    exit(1)

# 构造输出文件夹的路径
output_folder_path = video_title

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)
print(f"输出文件夹路径为：{output_folder_path}")

# 构建yt-dlp命令来下载视频
download_command = [
    "yt-dlp",
    "--cookies", "cookies.txt",
    "--write-subs",
    # "--embed-subs",
    "--embed-chapters",
    "--write-thumbnail",
    "--embed-thumbnail",
    "--add-metadata",
    "--merge-output-format", "mp4",
    "--output", os.path.join(output_folder_path, "%(title)s.%(ext)s"),  # 指定视频输出模板
    video_url
]

# 运行命令下载视频
try:
    subprocess.run(download_command, check=True)
    print("视频下载完成并保存到指定文件夹！")
except subprocess.CalledProcessError as e:
    print("视频下载失败:", e)

# 构建yt-dlp命令来获取视频简介和时长
description_command = [
    "yt-dlp",
    "--cookies", "cookies.txt",
    "--print", "description",
    "--print", "duration_string",
    video_url
]

# 使用subprocess运行yt-dlp命令并捕获输出
result = subprocess.run(description_command, capture_output=True, text=True)

# 检查命令是否成功执行
if result.returncode != 0:
    print("yt-dlp命令执行失败（获取简介和时长）")
    # 这里不再退出，因为我们希望代码能运行到最后一行

# 获取视频简介和时长（这里假设简介和时长是连续输出的，且时长在简介之后）
output = result.stdout
if output:
    description, duration_string = output.strip().rsplit('\n', 1)
    # 将视频简介保存为TXT文件到指定文件夹内
    description_file_path = os.path.join(output_folder_path, "video_description.txt")
    with open(description_file_path, "w", encoding="utf-8") as file:
        file.write(description)
    # 打印成功消息
    print(f"视频简介已保存为{description_file_path}，时长为：{duration_string}")
else:
    print("未能获取到视频简介和时长。")

# 指定目录路径
directory_path = output_folder_path
# 搜索目录下的 XML 文件
xml_files = glob.glob(os.path.join(directory_path, '*.xml'))

# 检查是否找到 XML 文件
if not xml_files:
    print("No XML files found in the specified directory.")
else:
    # 假设只处理一个 XML 文件（根据需求，只针对单个文件）
    input_file = xml_files[0]

    # 提取文件名（不带扩展名）
    file_name = os.path.splitext(os.path.basename(input_file))[0]

    # 设置输出文件路径
    output_file = os.path.join(directory_path, f'{file_name}.ass')

    try:
        # 调用 Danmaku2ASS 函数进行转换
        danmaku2ass.Danmaku2ASS(
            input_files=input_file,
            input_format='autodetect',
            output_file=output_file,
            stage_width=1920,
            stage_height=1080,
            font_size=35.0,
            text_opacity=0.8,
            duration_marquee=10.0,
            duration_still=5.0,
            reserve_blank=0,
            font_face='黑体'
        )
        print(f"Successfully converted {input_file} to {output_file}")

        # 转换成功后删除 XML 文件
        os.remove(input_file)
        print(f"Deleted the original XML file: {input_file}")

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        # 如果转换失败，可以选择不删除 XML 文件，或者根据需要进行其他处理