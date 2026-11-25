from ultralytics import YOLO
model = YOLO(r"D:\Desktop\traffic_project\runs\uadetrac_y11s_640\weights\best.pt")
model.export(format='onnx',imgsz=640)