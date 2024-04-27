import gradio as gr

def generate_batch(text, state, iterations):
    outputs = []
    for _ in range(iterations):
        modified_text = input_modifier(text, state)
        output = generate_reply(modified_text, state)
        outputs.append(output)
    return '<hr>'.join(outputs)

def ui():
    with gr.Blocks() as demo:
        with gr.Row():
            text_input = gr.Textbox(label="Enter text", lines=5)
            iterations = gr.Slider(minimum=1, maximum=5, step=1, label='Iterations')
            batch_button = gr.Button("Generate Batch")
            output_area = gr.HTML(label="Batch Outputs")

        batch_button.click(
            func=generate_batch,
            inputs=[text_input, gr.State(extended=True), iterations],
            outputs=output_area
        )

    demo.launch()
