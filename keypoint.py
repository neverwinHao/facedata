import cv2
import os
import openface

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')

align = openface.AlignDlib(os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))

def detect_keypoints_in_image(image):
    # 获取图片中所有脸部的边界框
    rects = align.getAllFaceBoundingBoxes(image)
    if len(rects) > 0:
        # 找到68个人脸关键点
        bb = align.findLandmarks(image, rects[0])

        for pt in bb:
            cv2.circle(image, pt, 3, [0, 0, 255], thickness=-1)

        return image

def process_images_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # 读取图片
            img = cv2.imread(input_path)
            if img is None:
                print(f"未能读取图片：{input_path}")
                continue

            # 检测关键点并保存图片
            result_img = detect_keypoints_in_image(img)
            if result_img is not None:
                cv2.imwrite(output_path, result_img)
                print(f"已处理并保存图片至：{output_path}")
            else:
                print(f"未检测到人脸关键点：{input_path}")

if __name__ == "__main__":
    input_folder = "./CelebA"  # 输入文件夹的路径
    output_folder = "./B"  # 输出文件夹的路径
    process_images_in_folder(input_folder, output_folder)
