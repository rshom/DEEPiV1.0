'''PiCamera implementation for deep sea applications'''

# TODO: impliment logging as necessary

import io
import os
import threading
import socket
import datetime
import time
import struct

from picamera import PiCamera as Camera



class DEEPi(Camera):
    '''
    PiCamera implementation for deep sea applications.
    '''

    def __init__(self, diveFolder=None):

        if diveFolder==None:
            currentDate = datetime.datetime.utcnow().isoformat()[:-10]
            diveFolder = currentDate.replace('-','').replace(':','')
        
        self.path = '{}/{}/'.format(os.getcwd(),diveFolder)
        try:
            os.mkdir(self.path)
        except:
            print("Unable to create divefolder")
            self.path = ''

        print("Saving files at: {}".format(self.path))
        Camera.__init__(self)
        time.sleep(2) # Allow camera to initiate


    def close(self):
        '''Release all resources'''
        Camera.close()
        # TODO: check for threads and terminate/join them <>


    def capture(self, output=None, use_video_port=True):
        '''Capture image using default settings and save to timestamp.

        See capture for more options
        '''
        if output==None:
            output = datetime.datetime.utcnow().isoformat()[:-7] + '.jpeg'
        print(self.path+output)
        Camera.capture( self, self.path+output, use_video_port=use_video_port)


    def start_recording( self, output=None):
        '''Record and save split video files to dive folder'''
        if output==None:
            output = datetime.datetime.utcnow().isoformat()[:-7] + '.H264'
        print(self.path+output)
        Camera.start_recording( self, self.path+output )

    def split_recording( self, output=None):
        '''Record and save split video files to dive folder'''
        if output==None:
            output = datetime.datetime.utcnow().isoformat()[:-7] + '.H264'
        print(self.path+output)
        Camera.split_recording( self, self.path+output )

    def __enter__(self):
        '''Called whenever instance is opened using a with statement'''
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Close out anything necessary'''
        self.close()


