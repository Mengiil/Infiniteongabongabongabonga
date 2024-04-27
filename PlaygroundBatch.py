import gradio as gr

# Angenommene Funktionen, stellen Sie sicher, dass diese vorhanden und korrekt implementiert sind
def generate_reply(prompt, state):
    # Diese Funktion sollte durch Ihre eigene Logik ersetzt werden
    return "Generierte Antwort basierend auf: " + prompt

def input_modifier(text, state):
    # Diese Funktion modifiziert den eingegebenen Text vor der Generierung
    return text

class BatchGenerationExtension:
    def __init__(self):
        self.display_name = "Playground Batch Extension"
        self.is_tab = True  # Setzen Sie True, wenn diese Extension als eigener Tab angezeigt werden soll

    def generate_batch(self, text, iterations):
        outputs = []
        state = {}  # ersetzen Sie dies durch den korrekten Status, falls nötig
        for _ in range(iterations):
            modified_text = input_modifier(text, state)
            output = generate_reply(modified_text, state)
            outputs.append(output)
        return '<hr>'.join(outputs)

    def ui(self):
        with gr.Blocks() as demo:
            with gr.Row():
                text_input = gr.Textbox(label="Enter text for batch generation", lines=5)
                iterations = gr.Slider(minimum=1, maximum=5, step=1, label='Iterations')
                batch_button = gr.Button("Generate Batch")
                output_area = gr.HTML(label="Batch Outputs")

            batch_button.click(
                func=self.generate_batch,
                inputs=[text_input, iterations],
                outputs=output_area
            )

        return demo

# Die Extension wird kreiert und geladen, wenn die Datei importiert wird
extension = BatchGenerationExtension()

# Nur, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    extension.ui().launch()
