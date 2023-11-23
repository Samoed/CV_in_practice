import gradio as gr
import numpy as np
import pandas as pd
from numpy import typing as npt
from ultralytics import YOLO

model = YOLO("models/best.pt")  # Make sure this is the correct path to your model


def predict(
    img: npt.NDArray[float]
) -> tuple[pd.DataFrame, tuple[npt.NDArray[np.float64], list[tuple[tuple[int], str]]]]:
    results = model(img)[0]
    pred = {"scores": [], "classes": []}
    annotation = []
    for box in results.boxes:
        pred["scores"].append(box.conf[0].cpu().item())
        pred["classes"].append(model.names[box.cls[0].cpu().item()])
        annotation.append((tuple(map(int, box.xyxy.cpu().tolist()[0])), model.names[box.cls[0].cpu().item()]))
    return pd.DataFrame(pred), (img, annotation)


def image_interface() -> gr.Blocks:
    with gr.Blocks() as demo:
        with gr.Row():
            image = gr.Image(sources=["upload"], label="Input")
            with gr.Column():
                table = gr.DataFrame()
                ann_image = gr.AnnotatedImage()
        image.upload(predict, image, [table, ann_image])
    return demo


image_interface().queue().launch()
