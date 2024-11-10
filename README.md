# 🎉 **Web Video Downloader 项目介绍** 🎉

💻 **编程语言**：Python

🌟 **使用的开源项目**：

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) 📥 - 一个强大的视频下载工具，支持从多个网站下载视频。
- [danmaku2ass](https://github.com/m13253/danmaku2ass) 📝 - 一个Python库，用于将Bilibili的弹幕XML文件转换为ASS字幕文件。

📚 **yt-dlp 使用说明**：

可以参考这个详细的教程视频：[yt-dlp 使用教程](https://www.bilibili.com/video/BV1A2DVY2EC5/?spm_id_from=333.999.0.0) 🎥

💡 **我的使用场景**：

我主要使用`yt-dlp`来下载Bilibili和Youtube的视频。虽然基本的下载需求只需在终端输入简单的命令，但处理下载后的文件（如合并音视频、重命名等）却相对繁琐。因此，我编写了这个Python脚本来简化这些步骤。

📝 **Python 脚本功能**：

1. 📥 下载网站最高清视频（支持使用cookies）
2. 📜 自动下载并内嵌简单字幕
3. 💬 自动处理Bilibili弹幕XML文件，转换为ASS字幕文件，模拟网页端弹幕效果
4. 🖼️ 下载视频缩略图并内嵌
5. 📝 下载视频介绍信息
6. 📁 自动新建文件夹管理下载内容（同名文件自动归并）
7. 📍 自定义下载路径

📊 **有无脚本的下载对比**：
![image](https://github.com/user-attachments/assets/e8cd2b51-9228-439d-b78c-e6b2bfa7fb37)

![图片1](https://github.com/user-attachments/assets/ae3b2998-2b3e-47f8-81f6-ec207731d33b)

📚 **使用说明**：

- 📥 源码和打包好的exe文件可在我的[Github仓库](https://github.com/Senquan007/WebVideoDownloader/releases/)中获取。
- 📝 Python源码提供了更高的定制自由度，exe文件则开箱即用，无需配置。

🔍 **获取`cookies`**：

- 安装Chrome插件[Get Cookies Locally](https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?hl=en) 🌐
- 导出`cookies.txt`文件，并将其移至Python脚本或exe文件的同一目录下。

📥 **安装`yt-dlp`和`ffmpeg`**：

- 这两个文件是脚本运行的核心，不可删除。
- 可以选择不安装，直接保留在脚本同一目录下；或者安装后将其移至`Windows\System32`文件夹下，或配置环境变量。

🔗 **URL输入**：

- 输入URL时，请确保不包含任何中文，并避免链接过长或包含不必要的参数。
- 建议直接在网站的搜索栏内复制URL，并删除不必要的参数。

📁 **压缩包内文件说明**：

| 文件/文件夹 | 说明 |
| --- | --- |
| yt-dlp | 核心文件，用于解析网址并下载视频及其余文件。 |
| ffmpeg | 核心文件，被`yt-dlp`调用，用于合并下载的视频和音频。 |
| danmaku2ass | Python库，用于将Bilibili的弹幕XML文件转换为ASS字幕文件。 |
| Web Video Downloader | 运行程序，打开后可根据提示下载视频。 |

>对于exe文件病毒报错的说明：
>该exe文件直接由pyinstaller转译得到，报错系正常。
