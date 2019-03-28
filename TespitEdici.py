import cv2


recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'

cam = cv2.VideoCapture(0)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        if(tahminEdilenKisi==2):
             tahminEdilenKisi= 'Sumeyye OZKAN'
        elif (tahminEdilenKisi == 1):
            tahminEdilenKisi = 'Beliz KORKUT'
        elif (tahminEdilenKisi == 3):
            tahminEdilenKisi = 'Feyza GOZUTOK'
        else:
            tahminEdilenKisi= "Bilinmeyen kişi"
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        cv2.putText(im, str(tahminEdilenKisi), (x, y + h), fontFace, fontScale, fontColor)
        cv2.imshow('im',im)
        cv2.waitKey(10)