import gradio as gr

params = {
    "display_name": "Playground Batch Extension",
    "is_tab": True
}

def generate_batch(text, iterations):
    outputs = []
    for i in range(iterations):
        outputs.append("Sample Output " + str(i+1) + ": " + text)
    return '<hr>'.join(outputs)

def ui():
    with gr.Blocks() as demo:
        with gr.Row():
            text_input = gr.Textbox(label="Enter text for batch generation", lines=5, placeholder="Type something here...")
            iterations = gr.Slider(minimum=1, maximum=5, step=1, label='Iterations')
            batch_button = gr.Button("Generate Batch")
            output_area = gr.HTML(label="Batch Outputs")

        batch_button.click(
            func=generate_batch,
            inputs=[text_input, iterations],
            outputs=output_area
        )
    demo.launch()

def setup():
    """
    Gets executed only once, when the extension is imported.
    This can be used to initialize settings or perform setup operations.
    """
    print("Playground Batch Extension has been loaded.")

if __name__ == "__main__":
    ui()
