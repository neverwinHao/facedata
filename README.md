# facedata
结合Openface与关键点对数据集重新处理(W-Net处理数据集官方来源)

可以根据人脸68个关键点位置重塑人脸为128*128(可根据需要修改)

# Example
<div style="display: flex; justify-content: center;">
    <img src="./img/image.png" width="200"/>
    <img src="./img/image_with_bb.png" width="200"/>
    <img src="./img/image_cropped.png" width="200"/>
</div>

需要自己预先安装openface(https://github.com/cmusatyalab/openface)
## OpenFace 安装指南

要使用 OpenFace，需要预先安装它。请按照以下步骤进行设置：

## 克隆 OpenFace 仓库

```sh
git clone https://github.com/cmusatyalab/openface.git
cd openface
```

## 安装 Python 依赖

```sh
sudo pip install -r requirements.txt
```

## 安装其他系统依赖

以 Ubuntu 为例，运行以下命令安装其他依赖项：

```sh
sudo apt-get install -y cmake python-pip python-dev ipython
sudo apt-get install -y libopencv-dev python-opencv
sudo apt-get install -y dlib
```

## 构建 OpenFace

```sh
sudo python setup.py install
```

## 下载预训练模型

```sh
./models/get-models.sh
```

## 验证安装

确保 OpenFace 安装正确，运行以下命令检查版本：

```sh
./util/align-dlib.py
```

更多详细信息和故障排除，请参考 [OpenFace GitHub 仓库](https://github.com/cmusatyalab/openface)。




## Explain
| File            | Description                       |
|-----------------|-----------------------------------|
| bicubic.py      | 双三次下采样                      |
| keypoint.py     | 检测并保存人脸关键点              |
| key_distance.py | 检测两个文件夹关键点并计算欧氏距离 |
| data.py         | 检测两个文件夹剔除相同的文件        |
| face_cut_xy.py  | 生成W-Net种可视化放大细节图       |
| process.py      | 数据集处理方式                   |
| pic_xiaorong.py | 消融实验画图代码                   |
| gen_binaryMASK.py | 生成二值化解析图，使用BiseNet                   |
| plot.m | 使用MATLAB画图                  |



## Usage

```bash
cd openface
pip install -r requirements.txt

python process.py
#修改input和output
```

