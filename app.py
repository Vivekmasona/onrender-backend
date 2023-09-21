from flask import Flask, request, render_template
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    
    # Get the title and size of the video
    title = yt.title
    size = yt.streams.get_audio_only().filesize
    
    # Download the audio
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path='downloads', filename='audio')
    
    return f'Title: {title}<br>Size: {size} bytes<br><a href="/downloads/audio.mp4" download>Download Audio</a>'

if __name__ == '__main__':
    app.run(debug=True)
