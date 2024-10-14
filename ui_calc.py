import gradio as gr
import requests

def perform_operation(operation, x, y):
    url = f"http://127.0.0.1:8000/{operation}"
    response = requests.get(url, params={"x": x, "y": y})
    if response.status_code == 200:
        return response.json()["result"]
    else:
        return response.json()["detail"]

iface = gr.Interface(
    fn=perform_operation,
    inputs=[gr.Radio(["add", "subtract", "multiply", "divide"], label="Operation"), gr.Number(label="x"), gr.Number(label="y")],
    outputs="text",
    description="Enter two numbers and select an operation to perform."
)

iface.launch()