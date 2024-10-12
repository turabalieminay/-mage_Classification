import cv2
import numpy as np
from ultralytics import YOLO

# Resim yolunu belirtin
img_path = "inference/predict12.jpeg"

# Resmi yükle ve boyutlandır
img = cv2.imread(img_path)
img = cv2.resize(img, (640, 480))  # Genişlik ve yükseklik ayarı

# YOLO modelini yükle
model_path = "C:/path_to_your_model/yolov8l-cls.pt"
model = YOLO(model_path)

# Resmi sınıflandır
results = model(img_path)

# Sınıf isimlerini ve olasılıkları al
class_dict = results[0].names
top5_classes = results[0].probs.top5
top5_confs = results[0].probs.top5conf

# Resim üzerine ilk 5 sonucu ekleyelim
for i, (cls, conf) in enumerate(zip(top5_classes, top5_confs)):
    label = f"{class_dict[cls]}: {conf:.2f}"
    # Her sonuç bir satır aşağı yazılacak
    cv2.putText(img, label, (20, 40 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

# OpenCV ile resmi göster (Spyder ortamında)
cv2.imshow("Sonuç", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sonuçları yazdır
print("Sınıflar:", class_dict)
print("Top 5 sınıflar ve olasılıklar:")
for i, (cls, conf) in enumerate(zip(top5_classes, top5_confs)):
    print(f"Sınıf {i+1}: {class_dict[cls]} ile olasılık {conf}")
