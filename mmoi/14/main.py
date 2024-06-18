from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path, "yolov3.pt"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    input_file_path=os.path.join(execution_path, "source.mp4"),
    output_file_path=os.path.join(execution_path, "result.mp4"),
    frames_per_second=20,
    log_progress=True
)

print(video_path)