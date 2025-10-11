# multilingual_medical_bot.py

import os
import json
import gradio as gr
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# ------------------------------
# Step 1: Setup API Key
# ------------------------------
load_dotenv()
client = OpenAI()

# ------------------------------
# Step 2: Whisper Speech-to-Text (Multilingual)
# ------------------------------
def transcribe_audio(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",  # Multilingual model
            file=audio_file
        )
    return getattr(transcript, "text", "")

# ------------------------------
# Step 3: Detect Language + Generate Response
# ------------------------------
def generate_response(prompt_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # You can switch to "gpt-4-turbo" if you want
        messages=[
            {"role": "system", "content": (
                "You are a multilingual medical assistant. "
                "Detect the user's language and reply in the same language. "
                "Provide safe, evidence-based, and reliable health information. "
                "If the user asks for medical advice beyond your capability, "
                "suggest consulting a certified doctor."
            )},
            {"role": "user", "content": prompt_text}
        ],
        temperature=0.2,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()

# ------------------------------
# Step 4: Combined Function for Audio or Text
# ------------------------------
def multilingual_medical_bot(audio=None, text_input=None):
    if audio:
        user_input = transcribe_audio(audio)
    else:
        user_input = text_input
    
    if not user_input:
        return "Please provide your question by speaking or typing."
    
    bot_reply = generate_response(user_input)
    return f"🗣 You said: {user_input}\n\n💬 Bot reply:\n{bot_reply}"

# ------------------------------
# Step 5: Gradio UI
# ------------------------------
# Step 5: Gradio UI
# ------------------------------
iface = gr.Interface(
    fn=multilingual_medical_bot,
    inputs=[
        gr.Audio(sources=["microphone", "upload"], type="filepath", label="🎤 Speak your question (any language)"),
        gr.Textbox(lines=2, placeholder="Or type your medical question here", label="💬 Text input")
    ],
    outputs="text",
    title="🌍 Welcome to Medical Remedy Bot",
    description=(
        "Ask your medical questions in any language (e.g., English, Tamil, Hindi, etc.) — "
        "the bot will understand and reply in the same language. "
    )
)

if __name__ == "__main__":
    # Azure provides the port in the PORT env var; bind to all interfaces
    port = int(os.environ.get("PORT", 7860))
    iface.launch(
        server_name="0.0.0.0",
        server_port=port,
        debug=False,
        show_error=True,
        inbrowser=False
    )
