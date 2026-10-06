import gradio as gr

def cumprimentar(nome):
    return f"Olá, {nome}! Seja bem-vindo(a)!"

app = gr.Interface(
    fn=cumprimentar,
    inputs="text",
    outputs="text",
    title="Meu primeiro projeto com Gradio",
    description="Digite seu nome abaixo:"
)

app.launch()