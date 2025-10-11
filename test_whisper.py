"""
test_whisper.py
Usage:
  python -u test_whisper.py [optional_audio_path]

If no path is provided, it will try these in order:
  1) munbbe_va.mp4
  2) munbe_va.mp4
  3) First match among *.mp3, *.wav, *.m4a, *.mp4 in current directory
"""

import os
import sys
from glob import glob
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIConnectionError, APIStatusError, BadRequestError, AuthenticationError


def pick_audio_path(arg_path: Optional[str]) -> Optional[str]:
    if arg_path:
        return arg_path if os.path.exists(arg_path) else None
    # common local names
    for candidate in ["munbbe_va.mp4", "munbe_va.mp4"]:
        if os.path.exists(candidate):
            return candidate
    # fallback: first audio-like file
    for pattern in ("*.mp3", "*.wav", "*.m4a", "*.mp4"):
        matches = sorted(glob(pattern))
        if matches:
            return matches[0]
    return None


def main():
    # Load API key from environment
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    audio_arg = sys.argv[1] if len(sys.argv) > 1 else None
    audio_path = pick_audio_path(audio_arg)

    print("=== Whisper Transcription Test ===")
    if audio_path:
        print(f"Audio file: {audio_path}")
    else:
        print("No audio file found. Place an audio file in this folder or pass a path.")
        sys.exit(1)

    if not api_key:
        print("OPENAI_API_KEY not set. Add it to .env or environment and rerun.")
        sys.exit(1)

    client = OpenAI()

    try:
        print("Transcribing with Whisper (model=whisper-1)...")
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
            )
        print("\n=== Transcription Result ===")
        print(getattr(transcript, "text", "<no text field>"))
    except AuthenticationError as e:
        print("Authentication failed:", e)
        print("Ensure your OPENAI_API_KEY is valid.")
        sys.exit(1)
    except (APIConnectionError, APIStatusError, BadRequestError) as e:
        print("API error:", e)
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {audio_path}")
        sys.exit(1)
    except Exception as e:
        print("Unexpected error:", repr(e))
        sys.exit(1)


if __name__ == "__main__":
    main()

