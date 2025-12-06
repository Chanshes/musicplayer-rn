import os
import shutil

# 定义源文件夹和目标文件夹的路径
download_folder = './download'
music_folder = './music'
lrc_folder = './lrc'

# 确保目标文件夹存在
os.makedirs(music_folder, exist_ok=True)
os.makedirs(lrc_folder, exist_ok=True)

# 遍历下载文件夹中的所有文件
for filename in os.listdir(download_folder):
    # 构建完整的文件路径
    file_path = os.path.join(download_folder, filename)
    
    # 检查是否是文件
    if os.path.isfile(file_path):
        # 获取文件扩展名
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # 转换为小写以确保匹配
        
        # 根据扩展名移动文件
        if ext == '.mp3':
            # 移动到music文件夹
            shutil.move(file_path, os.path.join(music_folder, filename))
            print(f'已移动MP3文件: {filename}')
        elif ext == '.lrc':
            # 移动到lrc文件夹
            shutil.move(file_path, os.path.join(lrc_folder, filename))
            print(f'已移动LRC文件: {filename}')
        else:
            print(f'跳过非MP3/LRC文件: {filename}')

print('\n所有文件移动完成！')

# 调用load.py脚本更新歌曲列表
import subprocess
import sys

print('\n开始调用load.py更新歌曲列表...')
subprocess.run([sys.executable, 'load.py'], cwd=os.path.dirname(os.path.abspath(__file__)))
print('歌曲列表更新完成！')