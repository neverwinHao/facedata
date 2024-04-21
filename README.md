# facedata
结合Openface与关键点对数据集重新处理

可以根据人脸68个关键点位置重塑人脸为128*128(可根据需要修改)

# Example
# 并排显示三张图片

<div style="display: flex; justify-content: center;">
    <figure>
        <img src="./img/image.png" width="200"/>
        <p align="center">input(any size)</p>
    </figure>
    <figure>
        <img src="./img/image_with_bb.png" width="200"/>
        <p align="center">keypoint</p>
    </figure>
    <figure>
        <img src="./img/image_cropped.png" width="200"/>
        <p align="center">output(128*128)</p>
    </figure>
</div>






## Usage

```python
cd openface
pip install -r requirements.txt

python process.py
#修改input和output
```

