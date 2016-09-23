import io

import picamera

import settings


def http_frame_generator():

    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = settings.CAMERA_RESOLUTION

        for each_frame in camera.capture_continuous(stream, 'jpeg', quality=50, use_video_port=True):

            # image is in the stream now, so rewinding to the very beginning to read it:
            stream.seek(0)
            frame = stream.read()

            http_frame_body = b'--frame\r\n' \
                              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

            yield http_frame_body

            # reset stream for next frame
            stream.seek(0)
            stream.truncate()
