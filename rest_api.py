import requests
import sounddevice as sd
import soundfile as sf
import requests

url = 'http://34.127.85.46:5000/upload'  # Replace with your Flask server URL

file_path = 'test.mp3'  # Path to the file you want to upload
duration = 3  # Duration of the recording in seconds

# Record audio
print('Recording started...')
recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
sd.wait()
print('Recording finished!')

# Save recording to an mp3 file
output_file = 'test2.wav'
sf.write(output_file, recording, 44100)

file_path = output_file

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print(response.text)
    print('File uploaded successfully!')
else:
    print('Failed to upload file:', response.text)