import cv2
import os
import openface
from tqdm import *
fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')

align = openface.AlignDlib(os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))

def bbox_generator(anno, img_root, expand_scale=0.3):
    split = anno.split()
    img_name = split[0]
    full_img = cv2.imread(os.path.join(img_root, img_name))
    full_h, full_w = full_img.shape[:2]

    x_min, y_min, w, h = [int(x) for x in split[1:]]

    # center_crop
    if w > h:
        dx = (w - h) / 2
        x_min += dx
        w = h
    else:
        dy = (h - w) / 2
        y_min += dy
        h = w

    expand_x = int(w * expand_scale / 2)
    expand_y = int(h * expand_scale / 2)
    new_x_min = max(0, int(x_min - expand_x))
    new_y_min = max(0, int(y_min - expand_y))
    x_max = min(int(new_x_min + w + 2 * expand_x), full_w)
    y_max = min(int(new_y_min + h + 2 * expand_y), full_h)
    return img_name, full_img[new_y_min:y_max, new_x_min:x_max]

def detect_keypoints_in_image(image_path, output_folder):
    # 读取图片
    img = cv2.imread(image_path)
    if img is None:
        print("图片未找到，请检查路径是否正确。")
        return

    # 获取图片中所有脸部的边界框
    rects = align.getAllFaceBoundingBoxes(img)
    if len(rects) > 0:
        # 生成边界框
        anno = os.path.basename(image_path) + " " + " ".join(map(str, [rects[0].left(), rects[0].top(), rects[0].right() - rects[0].left(), rects[0].bottom() - rects[0].top()]))

        img_name, cropped_img = bbox_generator(anno, os.path.dirname(image_path))

        # 调整裁剪后的图像大小为128x128
        resized_img = cv2.resize(cropped_img, (128, 128))

        # 输出文件的路径
        output_path = os.path.join(output_folder, os.path.basename(image_path))

        # 保存裁剪后的图片
        cv2.imwrite(output_path, resized_img)

        # print(f"裁剪后的图片已保存至：{output_path}")

if __name__ == "__main__":
    # 输入文件夹和输出文件夹路径
    input_folder = "helen"
    output_folder = "outputs"

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图像文件
    for filename in tqdm(os.listdir(input_folder)):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            # print("Processing image:", image_path)
            detect_keypoints_in_image(image_path, output_folder)





