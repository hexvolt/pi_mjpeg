from flask import render_template, Response

from pi_mjpeg import app
from services import http_frame_generator


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mjpeg_stream')
def mjpeg_stream():

    stream_response = Response(
        http_frame_generator(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

    return stream_response
