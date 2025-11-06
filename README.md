🧠 Medico AI – Whisper Speech-to-Text Assistant
🎯 Overview

Medico AI is a real-time speech-to-text and medical assistance application built using OpenAI Whisper, Python, and Gradio.
It converts spoken input into accurate text and provides intelligent, context-aware medical responses—enabling smooth, natural human–AI interaction for healthcare consultations and general conversation.

🚀 Features

🎙️ Real-time Speech-to-Text using OpenAI Whisper

🌍 Multilingual Support – Users can speak in any native language, and the system will provide answers in the same language

🤖 AI-powered Medical Assistance with natural language conversation

🎨 User-friendly Web Interface built using HTML, CSS, and Gradio

🔧 Configurable via .env for environment variables/API keys

📦 Easy to Deploy with minimal dependencies

📚 Dataset Released on Hugging Face for open research and model improvement 

⚠️ Troubleshooting / Notes

Ensure your microphone permissions are enabled.

If the accuracy of transcription drops, check your audio input quality (background noise, mic distance, etc.).

The multilingual responses rely on Whisper + LLM model capabilities.
If answers are not returning in your language, verify language auto-detection or manually set your output language parameter.

Make sure your .env file contains a valid OpenAI API Key.



## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Google's Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/)
