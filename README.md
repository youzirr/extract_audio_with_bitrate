
# FFmpeg音频提取工具

一个基于Python和FFmpeg的批量音频提取工具，自动将视频中的音频转换为MP3格式，并在文件名中添加原始音频码率信息。

## 🚀 主要功能

- **格式转换**：支持MP4/MKV/MOV/AVI/FLV/WMV → MP3
- **智能命名**：自动在输出文件名中添加检测到的音频码率（如`_192k.mp3`）
- **特殊字符处理**：自动清理文件名中的非法字符（支持中文/空格/特殊符号）
- **批量处理**：自动处理目录下的所有视频文件
- **质量保障**：使用`libmp3lame`编码器保持最佳音质

## 🛠️ 系统要求

- **操作系统**：Windows 10/11 | macOS 10.15+ | Linux（Ubuntu 20.04+测试通过）
- **Python**：3.6+
- **依赖工具**：[FFmpeg](https://ffmpeg.org/) 必须已安装并加入系统PATH

## 📥 安装步骤

1. 安装FFmpeg：
   - **Windows**：使用[winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/)安装：
     ```powershell
     winget install Gyan.FFmpeg
     ```
   - **macOS**：使用Homebrew安装：
     ```bash
     brew install ffmpeg
     ```

2. 下载脚本：
   ```bash
   git clone https://github.com/youzirr/extract_audio_with_bitrate.git
   cd audio-extractor
   ```

## 🎯 使用方法

1. 将需要转换的视频文件放入脚本所在目录
2. 运行脚本：
   ```bash
   python audio_extractor.py
   ```
3. 查看生成的MP3文件（文件名格式：`原文件名_audio_码率.mp3`）

**高级选项**：
- 处理子目录（需取消注释脚本中的`os.walk`部分）
- 自定义输出目录（修改`output_path`变量）

## 📝 输出示例

输入文件结构：
```
📁 videos/
    ├── 音乐会现场版.mp4 (音频码率256kbps)
    └── tutorial.mkv (音频码率128kbps)
```

运行脚本后：
```
📁 videos/
    ├── 音乐会现场版.mp4
    ├── 音乐会现场版_audio_256k.mp3
    ├── tutorial.mkv
    └── tutorial_audio_128k.mp3
```

## ❓ 常见问题

**Q1：出现`UnicodeDecodeError`错误怎么办？**  
A：请确保：
- 使用最新修复版脚本
- 文件路径不含非常用特殊符号（如`#[]`）
- 在PowerShell而非CMD中运行

**Q2：为什么有些文件提示"未检测到音频流"？**  
A：可能原因：
- 视频文件本身不含音频轨道
- 音频编码格式不被FFmpeg支持
- 使用`ffprobe 原始文件名`手动检测

**Q3：如何调整输出音质？**  
A：修改脚本中的以下参数：
```python
'-q:a', '2'  # 范围0-9（0=最佳质量，9=最小体积）
```

## 📜 许可证

本项目基于 [GNU GPLv3](LICENSE) 许可证发布，包含的FFmpeg组件使用 [LGPL](https://www.gnu.org/licenses/lgpl-3.0.html) 许可证。

---

> 遇到问题请提交Issue | 更新日期：2024-01-20
``` 

将此文件保存为`README.md`，与Python脚本放置在同一目录即可。
