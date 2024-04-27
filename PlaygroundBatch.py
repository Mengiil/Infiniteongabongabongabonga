import gradio as gr

def batch_generate(question, state, iterations):
    results = []
    summary = ""  # Dies sollte vom aktuellen UI-State oder einer entsprechenden Funktion geholt werden.
    for _ in range(iterations):
        prompt = generate_prompt(question, summary)
        for reply in generate_reply(prompt, state, stopping_strings=None, is_chat=False):
            results.append(reply)
    return "<br/><hr/>".join(results)  # Ergebnisse getrennt durch horizontale Linien

def update_iterations(x):
    global batch_iterations
    batch_iterations = x

def generate_batch(question, state):
    return batch_generate(question, state, batch_iterations)

def ui():
    global batch_iterations
    batch_iterations = 1  # Standardwert für die Anzahl der Durchläufe

    with gr.Row():
        with gr.Column():
            with gr.Tab('Playground'):
                text_box = gr.Textbox(lines=20, label='Playground')
                generate_btn = gr.Button('Generate')
                batch_btn = gr.Button('Generate Batch')
                iterations_slider = gr.Slider(minimum=1, maximum=3, step=1, label='Number of Iterations')
                iterations_slider.change(update_iterations, iterations_slider, None)
                
                with gr.Tab('Batch Output'):
                    batch_output = gr.HTML()

                generate_btn.click(generate_reply_wrapperMY, [text_box, shared.gradio['interface_state']], text_box)
                batch_btn.click(generate_batch, [text_box, shared.gradio['interface_state']], batch_output)

ui()
