import os
import sys
import cv2


def image_resize(source_path,target_path):
    source_image = os.listdir(source_path)
    source_image = sorted(source_image)
    for name in source_image:
        img_path = os.path.join(source_path,name)
        img = cv2.imread(img_path)
        new_img = cv2.resize(img,(672,504),interpolation=cv2.INTER_LINEAR)
        new_img_path = os.path.join(target_path,name)
        cv2.imwrite(new_img_path,new_img)




if __name__ == "__main__":
    source_path = "/home/dzt/data/06203130_hugelivingroom/images"
    target_path = "/home/dzt/data/06203130_hugelivingroom/image_resized"
    os.makedirs(target_path,exist_ok=True)
    image_resize(source_path,target_path)