import threading
from scripts.scriptgen import generate_script
from TTS.api import TTS

def print_stream(generator):
    script = []
    for word in generator:
        print(word, end='', flush=True)
        script.append(word)
    return ''.join(script)

def generate_audio(script_text, output_file, speaker):
    tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False)
    tts.to('cuda')
    tts.tts_to_file(text=script_text, file_path=output_file, speaker=speaker)

def main():
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

    speaker = "p225"
    generate_audio(script_text, output_file, speaker)
    print("\nStream completed. Audio saved to:", output_file)

if __name__ == "__main__":
    main()
