from PIL import Image

HR = Image.open(path/to/HR)
LR = HR.resize(lr_shape, resample=Image.BICUBIC)