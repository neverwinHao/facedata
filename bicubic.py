from PIL import Image
import os
from tqdm import *
def generate_LR(HR_path, LR_path):
    # 打开高分辨率图像
    HR = Image.open(HR_path)
    
    # 将高分辨率图像缩小到32x32像素大小，使用双三次插值法（BICUBIC）
    LR = HR.resize((32, 32), resample=Image.BICUBIC)
    
    # 保存低分辨率图像
    LR.save(LR_path)

if __name__ == "__main__":
    # 输入HR图像文件夹和输出LR图像文件夹路径
    input_folder = "outputs"
    output_folder = "LR_outputs"
    
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的所有图像文件
    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            HR_path = os.path.join(input_folder, filename)
            LR_path = os.path.join(output_folder, filename)
            # print("Generating LR image for:", HR_path)
            generate_LR(HR_path, LR_path)
