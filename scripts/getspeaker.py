from TTS.api import TTS

def list_speakers(model_name):
    tts = TTS(model_name=model_name, progress_bar=False)
    return tts.speakers

if __name__ == "__main__":
    model_name = "tts_models/en/vctk/vits"
    speakers = list_speakers(model_name)
    print("Available speakers:", speakers)
