import torch
from TTS.api import TTS


def generate_audio(script_text, output_file, speaker, devicetype):
    use_gpu = True if devicetype == "cuda" else False
    tts = TTS(
        model_name="tts_models/en/vctk/vits",
        progress_bar=True,
        gpu=use_gpu,
    )
    tts.to(devicetype)
    tts.tts_to_file(text=script_text, file_path=output_file, speaker=speaker)


if __name__ == "__main__":
    script_text = "Here is a sample script to be converted into speech."
    output_file = "output.wav"
    devicetype = "cuda" if torch.cuda.is_available() else "cpu"
    speaker = "p226"
    generate_audio(script_text, output_file, speaker, devicetype)
