import cv2
import numpy as np

# 读取图片
image = cv2.imread('./21680/021680.png')

# 显示图片
cv2.imshow('image', image)

# 定义鼠标回调函数
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("坐标 (x, y):", x, y)

# 设置鼠标回调函数
cv2.setMouseCallback('image', get_coordinates)

# 等待按下任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()


###读取到x,y坐标后，以此为中心点裁剪矩形框
from PIL import Image

def crop_square_around_point(input_image, output_image, center_point, size):
    """
    input_image: 输入图像的路径
    output_image: 输出图像的路径
    center_point: 中心点的坐标，形如 (x, y)
    size: 输出图像的大小，形如 (width, height)
    """
    # 打开图像
    img = Image.open(input_image)
    
    # 计算裁剪框的左上角和右下角坐标
    left = center_point[0] - size[0] // 2
    top = center_point[1] - size[1] // 2
    right = center_point[0] + size[0] // 2
    bottom = center_point[1] + size[1] // 2
    
    # 裁剪图像
    cropped_img = img.crop((left, top, right, bottom))
    
    # 保存图像
    cropped_img.save(output_image)

# 例子
input_image = "./21680/021680.png"
output_image = "./21680/output1.png"
center_point = (81, 48)  # 中心点坐标
size = (40, 40)  # 输出图像大小为 30x30

crop_square_around_point(input_image, output_image, center_point, size)

