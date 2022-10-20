import torch
import cv2
from user.models import User, ImageModel

def find_something(request, img_name):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    imgs = cv2.imread(f'{img_name[1:]}') # batch of images

    ##cv2의 channel이 BRG로 되어있어 사진이 파란색으로 보임, 그래서 RGB로 바꾸는 작업
    image_rgb = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    ###

    results = model(image_rgb)
    results.save()
    result = results.pandas().xyxy[0].to_numpy()
    result = [item for item in result if item[6]=='donut']

    for x in range(len(result)):
        cv2.rectangle(imgs, (int(result[x][0]), int(result[x][1]), int(result[x][2]), int(result[x][3])), (255,255,255))
    cv2.imwrite('result.png', imgs)
