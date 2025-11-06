🧠 Medico AI – Whisper Speech-to-Text Assistant
🎯 Overview

Medico AI is a real-time speech-to-text and medical assistance application built using OpenAI Whisper, Python, and Gradio.
It converts spoken input into accurate text and provides intelligent responses, enabling smooth human–AI interaction for healthcare or general use.

🚀 Features

🎙️ Real-time speech-to-text using OpenAI Whisper

🤖 AI-powered medical assistance through natural language interaction

🌐 Web interface built with HTML, CSS, and Gradio

⚙️ Configurable via .env file for API keys and environment variables

📊 Lightweight and easy to deploy

## ⚠️ Troubleshooting

- **Microphone not working**:
  - Check if another application is using the microphone
  - Verify PyAudio is installed correctly
  - Try adjusting the energy threshold in the code if having trouble with detection

- **Model download issues**:
  - Check your internet connection
  - The first run will take longer as it downloads the model
  - Models are cached in your home directory under `.cache/huggingface`

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Google's Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/)
