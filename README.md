# facedata
结合Openface与关键点对数据集重新处理

可以根据人脸68个关键点位置重塑人脸为128*128(可根据需要修改)

# Example
<div style="display: flex; justify-content: center;">
    <img src="./img/image.png" width="200"/>
    <img src="./img/image_with_bb.png" width="200"/>
    <img src="./img/image_cropped.png" width="200"/>
</div>

## Explain
|bicubic.py|双三次下采样|
|keypoint.py|检测并保存人脸关键点|
|key_distance.py|检测两个文件夹关键点并计算欧氏距离|




## Usage

```bash
cd openface
pip install -r requirements.txt

python process.py
#修改input和output
```

