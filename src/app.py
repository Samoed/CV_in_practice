import gradio as gr
import cv2
from ultralytics import YOLO
from PIL import Image

# import imageAI
# import opencv-python
# import Pillow
# Load the YOLO model
model = YOLO('../models/best.pt')  # Make sure this is the correct path to your model

def predict(img):
    # Convert Gradio Image component to OpenCV format
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    iter = 0
    # Perform inference
    results = model(frame)
    print(results)
    print(results[0])
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.show()  # show image
        im.save(f'results{iter}.jpg') 
        iter+=1
        return im
    # print(results.boxes[0])

    # Print intermediate results for debugging
    # print("Results:", results)

    # Extract relevant information from the results (modify this based on your model's output)
    # For demonstration purposes, let's assume the model returns a list of detected traffic signs
    # detected_signs = [result[0] for result in results.xyxy[0].tolist()]

    # Convert the list of detected signs to a formatted string
    # result_text = "\n".join(detected_signs)
    # return str(results)

# Define the Gradio Interface
iface = gr.Interface(
    fn=predict,
    # inputs=gr.Image(),  # Use Image component for input
    inputs=gr.Image(sources=["webcam"], streaming=True),  # Use Image component for input
    outputs="image",     # Output the detected signs as text
    live=True            # Enable live updates for the webcam stream
)

# Launch the Gradio app
iface.launch()
