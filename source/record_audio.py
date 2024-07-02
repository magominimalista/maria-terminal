import sounddevice as sd
import numpy as np
import base64
import os
from scipy.io.wavfile import write

def record_and_save_audio(seconds, filename):
    # Configurações de gravação
    sample_rate = 44100  # taxa de amostragem
    duration = seconds   # duração da gravação em segundos

    # Gravação de áudio
    print(f"Gravando áudio por {duration} segundos...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
    sd.wait()  # Aguarda até que a gravação esteja completa

    # Salva o áudio em um arquivo WAV
    wav_filename = os.path.join(os.getcwd(), filename)
    write(wav_filename, sample_rate, audio)  # Salva o áudio no arquivo WAV
    print(f"Áudio salvo como {wav_filename}")

    # Converte o áudio para base64
    with open(wav_filename, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

    return audio_base64
