import os

# 文件夹A的路径
folder_A = "./outputs"
# 文件夹B的路径
folder_B = "./HR"

def remove_files_from_A(folder_A, folder_B):
    # 获取文件夹B中的所有文件名
    files_B = os.listdir(folder_B)
    
    # 遍历文件夹A中的所有文件
    for filename in os.listdir(folder_A):
        # 如果文件名在文件夹B中也存在，则删除文件夹A中对应的文件
        if filename in files_B:
            file_path = os.path.join(folder_A, filename)
            os.remove(file_path)
            print(f"文件夹A中的文件 {filename} 已被删除")

if __name__ == "__main__":
    remove_files_from_A(folder_A, folder_B)
