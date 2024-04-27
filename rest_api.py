import requests

url = 'http://34.127.85.46:5000/upload'  # Replace with your Flask server URL

file_path = 'file.txt'  # Path to the file you want to upload

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

if response.status_code == 200:
    print(response)
    print('File uploaded successfully!')
else:
    print('Failed to upload file:', response.text)