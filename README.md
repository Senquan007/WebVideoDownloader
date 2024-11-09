# WebVideoDownloader
借助于yt-dlp以及danmaku2ass项目,主要针对bilibili以及youtube 下载优化的脚本，免去每次输入参数的繁琐。
## 本脚本说明
**语言：**
`Python`
使用项目：
`yt-dlp` `danmaku2ass`
**使用范围：**
参考  `yt-dlp` 里面提供可下载的范围，主要针对 `Bilibili` `Youtube` 下载进行优化
**脚本特点：**
- 搭配cookies，可下载你能观看到最高清晰度的视频
- 充分保留哔哩哔哩视频特色，将弹幕文件下载并保存为ass文件，搭配 `potplayer` 可以达到与在线观看相近的观看体验
- 下载略缩图，并内嵌至MP4文件中，防止内嵌图像无法读取，另外保存略缩图
- 保留视频介绍

**脚本使用说明：**
1. 将文件解压
2. 打开WebDownloader.exe
3. 按要求输入下载目录，以及下载网址

>对于exe文件病毒报错的说明：
>该exe文件直接由pyinstaller转译得到，报错系正常。
