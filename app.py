#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

# import camera driver
'''
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
'''
# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
import controller
from inspect import getmembers, isfunction

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    functions_list = [o[0] for o in getmembers(controller) if isfunction(o[1])]
    return render_template('index.html', commands=functions_list)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    camera.stream()
    return Response(gen(camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/<cmd>')
def cmd(cmd=None):
    try:
        response = eval("controller.{}()".format(cmd))
    except:
        raise
    
    return "{}: success".format(cmd), 200, {'Content-Type': 'text/plain'}

if __name__=='__main__':
    camera = Camera()
    app.run(host='0.0.0.0', threaded=True, port=5000)
    camera.shutdown()
