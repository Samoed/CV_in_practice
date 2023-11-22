import gradio as gr
import pandas as pd
from ultralytics import YOLO

model = YOLO("models/best.pt")  # Make sure this is the correct path to your model


def predict(img):
    results = model(img)[0]
    pred = {"scores": [], "classes": []}
    for box in results.boxes:
        pred["scores"].append(box.conf[0].cpu().item())
        pred["classes"].append(model.names[box.cls[0].cpu().item()])
    return pd.DataFrame(pred)


def webcam_interface() -> gr.Blocks:
    with gr.Blocks() as demo:
        with gr.Row():
            image = gr.Image(sources=["webcam"], label="Input")

            table = gr.DataFrame()
        image.stream(predict, image, table)
        # image.upload(predict, image, table)
    return demo


def video_result(img):
    results = model(img)[0]
    print(results.render())
    return results.render()


def video_interface() -> gr.Interface:
    return gr.Interface(fn=predict, inputs="video", outputs="video")


webcam_interface().queue().launch()
# video_interface().launch()
