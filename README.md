# YOLOv8 Deployment with TorchServe and Docker

This guide explains how to serve a YOLOv8 model as a REST API using TorchServe and Docker. Follow the steps below to set up and deploy the model locally.

## Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- A pre-trained YOLOv8 model (either from the [Ultralytics GitHub repository](https://github.com/ultralytics/ultralytics) or a custom-trained model).
- Save the custom model.pt file in  model-store directory.

## Steps to Serve YOLOv8 as a REST API

### 1. Set Up Project Directory

1. Create a project directory:
   ```bash
   mkdir yolov8-torchserve
   cd yolov8-torchserve
   
2. Inside the project folder, ensure you have the following files:
   * `Dockerfile`
   * `config.properties`
   * `yolov8_handler.py`
   * A `model-store` directory containing the YOLOv8 model (e.g., `yolov8l.pt`).

3. Build the Docker image using the provided `Dockerfile`:

   ```bash
   docker build -t yolov8-torchserve .
   
4. Run the Docker Container
	Start the container and map the necessary ports:
	```bash docker run -d --name yolov8-torchserve -p 8080:8080 -p 8081:8081 -p 8082:8082 yolov8-torchserve```
	
5. Model Registration (Optional)
	You can skip this step by ensuring the following lines are in your config.properties:
	``` disable_token_authorization=true```
		```load_models=all ```
Alternatively, manually register the model:
	```bash curl -X POST "http://localhost:8081/models?url=yolov8.mar&initial_workers=1&synchronous=true"```
	
6. Test the Model API
	Send an image to the API for inference and save the output to output.json:
	``` curl -X POST http://localhost:8080/predictions/yolov8 -H "Content-Type: image/jpeg" --data-binary @test2.jpg > output.json ```
	
7. It will output the results in output.json
	