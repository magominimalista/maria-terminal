import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def synthesize_and_play_audio(chatgpt_response, speed=1.0):
    # Sintetiza a resposta em voz
    audio_file_path = os.path.join(os.getcwd(), "output.mp3")
    tts = gTTS(chatgpt_response, lang='pt-BR', slow=False)
    tts.save(audio_file_path)

    # Reproduz o áudio usando pydub
    audio = AudioSegment.from_file(audio_file_path, format="mp3")
    
    # Ajusta a velocidade do áudio e taxa de amostragem
    adjusted_speed = 1.4  # Defina a velocidade desejada aqui
    modified_audio = audio._spawn(audio.raw_data, overrides={
        "frame_rate": int(audio.frame_rate * adjusted_speed),
    })

    # Ajusta a largura de amostra, se necessário (mantém a largura padrão de 2 bytes para MP3)
    if audio.sample_width != 2:
        modified_audio = modified_audio.set_sample_width(2)

    modified_audio = modified_audio.set_frame_rate(int(audio.frame_rate * adjusted_speed))

    # Reproduz o áudio usando pydub
    play(modified_audio)