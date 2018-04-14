# -*- coding: utf-8 -*-

# 识别图片中的人脸
import face_recognition
chen_image=face_recognition.load_image_file('images/chenguanghai1.jpg')
liao_image=face_recognition.load_image_file('images/liao.jpg')
unknown_image=face_recognition.load_image_file('images/liaochen.jpg')

chen_encoding=face_recognition.face_encodings(chen_image)[0]
liao_encoding=face_recognition.face_encodings(liao_image)[0]
unknown_encoding=face_recognition.face_encodings(unknown_image)[0]

results=face_recognition.compare_faces([chen_encoding,liao_encoding],unknown_encoding)
labels=['chen','liao']

print 'results'+str(results)

for i in range(0,len(results)):
    if results[i] == True:
        print 'The person is:'+labels[i]