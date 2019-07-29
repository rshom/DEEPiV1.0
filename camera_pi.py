import io
import time
from picamera import PiCamera
from base_camera import BaseCamera
import controller


camera = controller.cam

class Camera(BaseCamera):
    def __init__(self):
        BaseCamera.__init__(self)
        # let camera warm up
        time.sleep(2)
    def __enter__(self):
        self.__init__(self)
        return self

    def shutdown(self):
        camera.close()

    def __exit__(self):
        self.shutdown()

    @staticmethod
    def frames():
        stream = io.BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg',
                                           use_video_port=True,
                                           resize=(720,480),
                                           splitter_port=3):
                                           
            # return current frame
            stream.seek(0)
            yield stream.read()
            
            # reset stream for next frame
            stream.seek(0)
            stream.truncate()
            
