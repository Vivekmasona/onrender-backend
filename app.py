from flask import Flask, request, jsonify
from pytube import YouTube
import json

app = Flask(__name__)

@app.route('/audio/', methods=['GET'])
def download_audio():
    link = request.args.get('link')

    if not link:
        return jsonify({'error': 'Invalid or missing "link" parameter'}), 400

    try:
        utube = YouTube(link)
        Title = utube.title
        Thumbnail = utube.thumbnail_url

        ados = utube.streams.filter(only_audio=True)
        resolution_list = [ado.abr for ado in ados]
        itag_list = [ado.itag for ado in ados]

        dwnld_link_list = [ados.get_by_itag(i).url for i in itag_list]

        data_set = {
            'audio_title': Title,
            'audio_thumbnail': Thumbnail,
            'audio_resolution_list': resolution_list,
            'audio_download_link_list': dwnld_link_list
        }

        return jsonify(data_set)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
