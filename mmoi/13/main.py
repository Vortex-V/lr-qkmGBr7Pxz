from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "retinanet.pth"))
detector.loadModel()
detections = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path, "source.jpg"),
    output_image_path=os.path.join(execution_path, "result.jpg"),
    minimum_percentage_probability=30
)
