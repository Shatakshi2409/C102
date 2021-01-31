import cv2
import dropbox
import time
import random

startTime=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        print(ret)
        imgname='img'+str(number)+'.png'
        cv2.imwrite(imgname,frame)
        startTime=time.time
        result=False
    return imgname
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgname):
    access_token='sl.AqWnjnVqtpy5U1baMAbzbKmy-GvzfHnyrBzq9aFfE9KvWqDraInd1Lmq9Dk5BbqG-0WC1TJVCx8sXvoFcGvy3ioRRtDuR1-6lyKuqYxkPcjulde_gGkxxIOEmij7LNU6NqxleAM1'
    file=img_counter
    filefrom=file
    fileto='/newFolder1/'+imgname
    dbx=dropbox.Dropbox(access_token)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

def main():
    while(True):
        if((time.time()-startTime)>=100):
            name=takeSnapshot()
            uploadFile(name)
main()
