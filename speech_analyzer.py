import gradio as gr
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv
import os

load_dotenv()

# Speech-to-text pipeline (Whisper)
s2t_pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# Text generation pipeline (Llama2 or fallback)
# Try to use Llama2, fallback to distilgpt2 if not available
try:
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    text_gen_pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
except Exception:
    tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
    model = AutoModelForCausalLM.from_pretrained("distilgpt2")
    text_gen_pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

PROMPT_TEMPLATE = """
List the key points with details from the context below:\n{context}\nKey points:
"""

def transcript_audio(audio_file):
    transcript_txt = s2t_pipe(audio_file, batch_size=8)["text"]
    prompt = PROMPT_TEMPLATE.format(context=transcript_txt)
    result = text_gen_pipe(prompt, max_new_tokens=200, temperature=0.1)
    return result[0]["generated_text"]

audio_input = gr.Audio(sources=["upload"], type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(fn=transcript_audio,
                    inputs=audio_input, outputs=output_text,
                    title="Audio Transcription App",
                    description="Upload the audio file")
iface.launch(server_name="0.0.0.0", server_port=7860)