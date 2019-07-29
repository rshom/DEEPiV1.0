import io
import time
#import picamera
from base_camera import BaseCamera
from deepi import DEEPi

class Camera(BaseCamera,DEEPi):

    def __init__(self):
        BaseCamera.__init__(self)
        DEEPi.__init__(self)

    @staticmethod
    def frames():
        stream = io.BytesIO()
        for _ in DEEPi.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
            # return current frame
            stream.seek(0)
            yield stream.read()
        
            # reset stream for next frame
            stream.seek(0)
            stream.truncate()
