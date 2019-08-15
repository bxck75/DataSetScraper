import cv2
import sys,imutils, argparse,face_recognition

# info : https://www.programcreek.com/python/example/84097/cv2.circle
# for i in `ls /root/terra_1TB/data/boefjes/front`;do p capture_all_faces.py -i /root/terra_1TB/data/boefjes/front/$i -s 5000; done
import uuid
unique_key = uuid.uuid4()
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", default='shape_predictor_81_face_landmarks.dat',
	help = "path to facial landmark predictor")
ap.add_argument("-i", "--image", required = True,
	help = "path to input image")
ap.add_argument("-s", "--size", default=1024,
	help = "path to input image")
args = vars(ap.parse_args())

imagePath = args['image']
imageReSize= int(args['size'])
image = cv2.imread(imagePath)
h,w,c = image.shape
imageOrgWidth = w
image = imutils.resize(image, width = imageReSize)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(gray)

number_of_faces = len(face_landmarks_list)
print("I found {} object(s) in this photograph.".format(number_of_faces))
print(imagePath)
pre = cv2.imread(imagePath)
pre = imutils.resize(pre, width = 400)
cv2.imshow("To",pre)
cv2.waitKey(300)


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(100, 100)
)
# print(dir(faceCascade.detectMultiScale))
print("[INFO] Found {0} Faces.".format(len(faces)))
count=1
for (x, y, w, h) in faces:
    unique_key = uuid.uuid4()
    roi_color = image[y:y + h-1, x:x + w-1]
    print("[INFO] Object found. Saving locally."+'output/'+str(unique_key)+str(w) +'_'+ str(h)+'_'+str(count) + '_faces.jpg')
    cv2.imwrite('output/'+str(unique_key)+str(w) +'_'+ str(h)+'_'+str(count) + '_faces.jpg', roi_color)
    # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
    count += 1
# image = imutils.resize(image, width = imageOrgWidth)
# status = cv2.imwrite(str(unique_key)+'_faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)