
import os
import datetime
import picamera

print("Starting Camera")
camera = picamera.PiCamera(stereo_mode="side-by-side")

print("Setting up dive folder")
currentDate = datetime.datetime.utcnow().isoformat()[:-10]
diveFolder = currentDate.replace('-','').replace(':','')

try:
    workingDirectory = 'home/pi'
    path = '{}/{}/'.format(workingDirectory,diveFolder)
    os.mkdir(path)
except:
    workingDirectory = os.getcwd()
    path = '{}/{}/'.format(workingDirectory,diveFolder)
    os.mkdir(path)
    print("Using already existing directory")


def genName():
    while True:
        timeStamp = datetime.datetime.utcnow().isoformat()
        yield timeStamp[:-7].replace('-','').replace(':','')

name = genName()

def deploy(splitTime = 600, camera=camera, path=path):
    print("Recording first video")
    camera.start_recording( path+next(name)+'.h264' )
    while True:
        camera.wait_recording(splitTime)
        print("Splitting recording")
        camera.split_recording( path+next(name)+'.h264' )


def capture(camera=camera,path=path):
    print("Taking picture")
    camera.capture( path+next(name)+'.jpeg', use_video_port=True)
    print("Picture taken")
    
def record(camera=camera, path=path):
    print("Recording")
    camera.start_record( path+next(name)+'.h264')
    print("Recording finished")

if __name__=='__main__':
    deploy(splitTime=6)

    
