import os
import speech_recognition as sr

def transcribe_audio(wav_filename):
    r = sr.Recognizer()
    transcription = ""

    # Transcreve o áudio
    with sr.AudioFile(wav_filename) as source:
        audio = r.record(source)
        transcription = r.recognize_google(audio, language='pt-BR')

    return transcription
