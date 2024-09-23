FROM pytorch/torchserve:0.11.1-gpu

USER root
RUN pip3 install ultralytics torch-model-archiver

# Copy necessary files
COPY model-store /home/model-server/model-store
COPY config.properties /home/model-server/config.properties
COPY yolov8_handler.py /home/model-server/yolov8_handler.py

# Create model archive
RUN torch-model-archiver --model-name yolov8 --version 1.0 \
    --model-file /home/model-server/yolov8_handler.py \
    --serialized-file /home/model-server/model-store/best.pt \
    --handler /home/model-server/yolov8_handler.py \
    --export-path /home/model-server/model-store

USER model-server

CMD ["torchserve", "--start", "--ts-config", "/home/model-server/config.properties"]