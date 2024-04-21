import os

folder_B = "./outputs"

def change_extension(folder_path, old_ext, new_ext):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件的后缀是否为旧后缀
        if filename.endswith(old_ext):
            # 构建新的文件名
            old_file_path = os.path.join(folder_path, filename)
            new_filename = os.path.splitext(filename)[0] + new_ext
            new_file_path = os.path.join(folder_path, new_filename)
            
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"文件 {filename} 已更改为 {new_filename}")

if __name__ == "__main__":
    change_extension(folder_B, ".jpg", ".png")
