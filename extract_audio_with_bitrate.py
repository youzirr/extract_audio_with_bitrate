import os
import subprocess
import re

def get_audio_bitrate(input_file):
    """使用ffprobe获取音频流码率（单位：kbps）"""
    try:
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'a:0',
            '-show_entries', 'stream=bit_rate',
            '-of', 'default=noprint_wrappers=1:nokey=1',
            input_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        bitrate_bps = result.stdout.strip()
        
        if not bitrate_bps.isdigit():
            return None
        
        bitrate_kbps = int(bitrate_bps) // 1000
        return f"{bitrate_kbps}k"
    except subprocess.CalledProcessError:
        return None

def extract_audio(input_file, output_file):
    """使用ffmpeg提取音频流"""
    try:
        subprocess.run([
            'ffmpeg',
            '-i', input_file,
            '-vn',          # 禁用视频流
            '-acodec', 'copy', # 直接复制音频流（保持原始编码）
            '-y',          # 覆盖已存在文件
            output_file
        ], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"错误：处理文件 {input_file} 失败 - {str(e)}")
        return False

def main():
    # 支持处理的视频格式
    video_extensions = ['.mp4', '.mkv', '.mov', '.avi', '.flv']
    
    for filename in os.listdir('.'):
        # 跳过非视频文件
        if not os.path.isfile(filename):
            continue
        base, ext = os.path.splitext(filename)
        if ext.lower() not in video_extensions:
            continue
            
        # 获取音频码率
        bitrate = get_audio_bitrate(filename)
        if not bitrate:
            print(f"警告：{filename} 未检测到音频流或获取码率失败，已跳过")
            continue
            
        # 构建输出文件名（保留原文件名+码率）
        output_filename = f"{base}_{bitrate}.m4a"  # 默认使用原始容器格式
        
        # 执行音频提取
        print(f"正在处理：{filename} → {output_filename}")
        if extract_audio(filename, output_filename):
            print(f"成功生成：{output_filename}\n")

if __name__ == "__main__":
    # 检查前置依赖
    try:
        subprocess.run(['ffprobe', '-version'], check=True, capture_output=True)
        subprocess.run(['ffmpeg', '-version'], check=True, capture_output=True)
    except FileNotFoundError:
        print("错误：请先安装 FFmpeg 并确保 ffprobe 和 ffmpeg 在系统路径中")
        exit(1)
        
    main()