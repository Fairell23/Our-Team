import os
import sys
import json
import pyaudio
from vosk import Model, KaldiRecognizer


# Загрузка модели
model_path = "model"  # Укажите путь к папке с русской моделью
if not os.path.exists(model_path):
    print(f"Модель не найдена в {model_path}. Скачайте её с https://alphacephei.com/vosk/models и распакуйте.")
    sys.exit(1)

model = Model(model_path)

# Инициализация аудио
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Говорите что-то...")

# Основной цикл для распознавания
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        print(f"Распознанный текст: {result['text']}")
        abc = [result]
        print(abc)
abc = [result]
print(abc)
# Завершение работы
stream.stop_stream()
stream.close()
mic.terminate()




