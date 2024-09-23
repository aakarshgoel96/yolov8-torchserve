import io
import torch
from PIL import Image
from ts.torch_handler.base_handler import BaseHandler
from ultralytics import YOLO

class YOLOv8Handler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.model = None

    def initialize(self, context):
        self.manifest = context.manifest
        properties = context.system_properties
        model_dir = properties.get("model_dir")
        self.model = YOLO(f"{model_dir}/best.pt")

    def preprocess(self, data):
        images = []
        for row in data:
            image = row.get("data") or row.get("body")
            if isinstance(image, bytearray):
                image = Image.open(io.BytesIO(image)).convert("RGB")
            images.append(image)
        return images

    def inference(self, data):
        results = self.model(data)
        return results

    def postprocess(self, inference_output):
        return [result.boxes.data.tolist() for result in inference_output]