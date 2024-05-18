import numpy as np
import torch
import os
import os.path as osp
import cv2
from PIL import Image
import torchvision.transforms as transforms
from model import BiSeNet

def binary_face_mask(parsing, face_class=1):
    """
    Generate binary mask for face region.
    Args:
        parsing: numpy array, parsing map
        face_class: int, class index for face region
    Returns:
        face_mask: numpy array, binary mask for face region
    """
    face_mask = (parsing == face_class).astype(np.uint8) * 255
    return face_mask

def vis_parsing_maps(im, parsing_anno, stride, save_im=False, save_path='vis_results/parsing_map_on_im.jpg'):
    im = np.array(im)
    vis_im = im.copy().astype(np.uint8)
    vis_parsing_anno = parsing_anno.copy().astype(np.uint8)
    vis_parsing_anno = cv2.resize(vis_parsing_anno, None, fx=stride, fy=stride, interpolation=cv2.INTER_NEAREST)

    # Generate binary mask for face
    face_mask = binary_face_mask(vis_parsing_anno)

    # Ensure face mask is 3-channel
    face_mask_3c = cv2.cvtColor(face_mask, cv2.COLOR_GRAY2BGR)

    # Combine original image and face mask
    vis_im = cv2.bitwise_and(vis_im, face_mask_3c)

    # Save result or not
    if save_im:
        cv2.imwrite(save_path[:-4] + '_binary.png', face_mask)
        cv2.imwrite(save_path, vis_im, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

def evaluate(respth='./res/test_res', dspth='./data', cp='model_final_diss.pth'):
    if not os.path.exists(respth):
        os.makedirs(respth)

    n_classes = 19
    net = BiSeNet(n_classes=n_classes)
    net.cuda()
    save_pth = osp.join('res/cp', cp)
    net.load_state_dict(torch.load(save_pth))
    net.eval()

    to_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    with torch.no_grad():
        for image_path in os.listdir(dspth):
            img = Image.open(osp.join(dspth, image_path))
            image = img.resize((512, 512), Image.BILINEAR)
            img = to_tensor(image)
            img = torch.unsqueeze(img, 0)
            img = img.cuda()
            out = net(img)[0]
            parsing = out.squeeze(0).cpu().numpy().argmax(0)

            vis_parsing_maps(image, parsing, stride=1, save_im=True, save_path=osp.join(respth, image_path))

if __name__ == "__main__":
    evaluate(dspth='./realword', cp='79999_iter.pth')
