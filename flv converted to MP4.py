import subprocess
import os

# FFmpeg的绝对路径（根据你的安装路径进行修改）
ffmpeg_path = r'C:\ffmpeg\bin\ffmpeg.exe'

def convert_flv_to_mp4(input_file, output_file):
    if not os.path.isfile(input_file):
        print(f'错误：找不到输入文件 {input_file}')
        return False
    
    try:
        # 使用subprocess调用FFmpeg命令行工具进行转换
        cmd = [ffmpeg_path, '-i', input_file, '-c', 'copy', output_file]
        subprocess.run(cmd, check=True)
        print(f'文件 {input_file} 转换为 {output_file} 成功！')
        return True
    except subprocess.CalledProcessError as e:
        print(f'转换失败：{e}')
        return False

# 输入FLV文件和输出MP4文件的目录
input_directory = r'C:\培训视频\Exchange 2016'
output_directory = r'C:\培训视频\Exchange 2016\mp4'

# 如果输出目录不存在，创建输出目录
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 获取输入目录下所有FLV文件
flv_files = [f for f in os.listdir(input_directory) if f.endswith('.flv')]

# 遍历FLV文件并进行转换
for flv_file in flv_files:
    input_path = os.path.join(input_directory, flv_file)
    output_file = os.path.join(output_directory, os.path.splitext(flv_file)[0] + '.mp4')
    convert_flv_to_mp4(input_path, output_file)
