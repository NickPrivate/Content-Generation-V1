import threading

import torch

from scripts.audiogen import generate_audio
from scripts.render import render_vid
from scripts.scriptgen import generate_script

print("Initializing Modlels...")
from TTS.api import TTS


def print_stream(generator):
    script = []
    for word in generator:
        print(word, end="", flush=True)
        script.append(word)
    return "".join(script)


def main():
    device_type = "cuda" if torch.cuda.is_available() else "cpu"
    if device_type == "cuda":
        print("GPU Detected, GPU Will be utilized for Faster Rendering")
    else:
        print("No GPU Detected, Opting for CPU Rendering")
    word_count = input("Enter word count: ")
    prompt = input("Enter prompt: ")
    our_prompt = f"{prompt} in {word_count} words"
    response_generator = generate_script(our_prompt)

    script_text_list = []

    def stream_and_capture():
        script_text = print_stream(response_generator)
        script_text_list.append(script_text)

    stream_thread = threading.Thread(target=stream_and_capture)
    stream_thread.start()
    stream_thread.join()

    print("\nConverting script to audio...\n")

    script_text = script_text_list[0] if script_text_list else ""
    output_file = "output.wav"
    speaker = "p226"

    generate_audio(script_text, output_file, speaker, device_type)
    print("\nStream completed. Audio saved to:", output_file)

    print("\nNow onto rendering the video")

    render_vid()
    print("\nVideo Successfully rendered")
    print("\nUse vlc final_video.mp4 to view")


if __name__ == "__main__":
    main()
