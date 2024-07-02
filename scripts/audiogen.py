from TTS.api import TTS

def generate_audio(script_text, output_file):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    tts.tts_to_file(text=script_text, file_path=output_file)

if __name__ == "__main__":
    script_text = "Here is a sample script to be converted into speech."
    output_file = "output.wav"
    generate_audio(script_text, output_file)
