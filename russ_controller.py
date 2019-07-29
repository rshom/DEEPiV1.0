
import os
import datetime
import picamera

try:
    cam = picamera.PiCamera(stereo_mode="side-by-side")
except:
    cam = picamera.PiCamera()

currentDate = datetime.datetime.utcnow().isoformat()[:-10]
diveFolder = currentDate.replace('-','').replace(':','')

path = '{}/{}/'.format(os.getcwd(),diveFolder)
try:
    os.mkdir(path)
except FileExistsError:
    print("Using already existing directory")

def capture(cam=cam,path=path):
    output = datetime.datetime.utcnow().isoformat()[:-7].replace('-','').replace(':','') + '.jpeg'

    cam.capture( path+output, use_video_port=True)
    print("Picture taken")
    


def record(cam=cam, path=path):
    output = datetime.datetime.utcnow().isoformat()[:-7].replace('-','').replace(':','') + '.jpeg'
    cam.start_record( path+output )

#def deploy():
    

if __name__=='__main__':
    try:
        cam = picamera.PiCamera()
        cam.start_preview()
        currentDate = datetime.datetime.utcnow().isoformat()[:-10]
        diveFolder = currentDate.replace('-','').replace(':','')
        
        path = '{}/{}/'.format(os.getcwd(),diveFolder)
        os.mkdir(path)

        capture(cam,path)
        
    finally:
        cam.stop_preview()
        cam.close()

    
