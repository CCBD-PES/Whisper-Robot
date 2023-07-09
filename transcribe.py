import whisper
import subprocess
model = whisper.load_model("base")
input = "C:/Users/Anshul Ranjan/Downloads/CCBD/Alice_Arnold_voice.wav"

def transcribe(audio_file):
    command = ["ffmpeg", "-i", audio_file, "-ac", "1", "-ar", "16000", "-y", "temp.wav"]
    subprocess.call(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    input = "temp.wav"
    result = model.transcribe(input)
    print(result["text"])
    return result["text"]

result = transcribe(input)
print(result["text"])
