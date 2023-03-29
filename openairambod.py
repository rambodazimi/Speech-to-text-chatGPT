import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "Answer questions which are only in persian language" + " Don't answer in english" +
    " Always write in persian" + " Your name is Rambod" + " You are 23 years old" + " Your girl friend is Sara Daneshi" + " Sara Daneshi lives in Montreal, Canada"},
]

def chatbot(input):
    history = []
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        history.append((input, reply))
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot Rambod", description="Ask anything you want", theme="compact").launch(share=True)