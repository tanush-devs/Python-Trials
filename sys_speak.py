import os
import platform


def speak(text):
    if platform.system() == "Darwin": # Mac
        os.system(f'say "{text}"')
    elif platform.system() == "Windows": # Windows
        os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

speak("System breach detected. Self destruct sequence initialized.")