import os
import source.gptkey
from source.record_audio import record_and_save_audio
from source.transcribe_audio import transcribe_audio
from source.openai_integration import generate_openai_response
from source.synthesize_audio import synthesize_and_play_audio

if __name__ == "__main__":
    filename = "input.wav"
    seconds_to_record = 5

    # Grava e codifica o áudio
    audio_base64 = record_and_save_audio(seconds_to_record, filename)
    print("Áudio gravado e codificado em base64.")

    # Transcreve o áudio
    wav_filename = os.path.join(os.getcwd(), filename)
    transcription = transcribe_audio(wav_filename)
    print("Você disse:", transcription)

    # Gera a resposta usando OpenAI
    chatgpt_response = generate_openai_response(transcription)
    print("Resposta:", chatgpt_response)

    # Sintetiza e reproduz a resposta em áudio
    synthesize_and_play_audio(chatgpt_response)
