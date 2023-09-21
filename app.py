from flask import Flask, request, send_file
import youtube_dl

app = Flask(__name__)

@app.route('/audio', methods=['POST'])
def download_audio():
    url = request.form.get('url')

    if not url:
        return "Please provide a valid URL."

    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save the file with its title
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
  
