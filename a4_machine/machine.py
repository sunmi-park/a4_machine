import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
imgs = cv2.imread('media/zidane.jpg') # batch of images
 # a4_machine/img/donut.jpg

##cv2의 channel이 BRG로 되어있어 사진이 파란색으로 보임, 그래서 RGB로 바꾸는 작업
image_rgb = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
###

results = model(image_rgb)
results.save()
result = results.pandas().xyxy[0].to_numpy()
result = [item for item in result if item[6]=='donut']
print(result)


for x in range(len(result)):
    cv2.rectangle(imgs, (int(result[x][0]), int(result[x][1]), int(result[x][2]), int(result[x][3])), (255,255,0))
cv2.imwrite('result.png', imgs)
