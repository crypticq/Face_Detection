import cv2

#
#Coded By Eng Yazeed
#

def cehck_image(jpg):

	img = cv2.imread(jpg)
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(img, 1.1, 4)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 45, 33), 3)
		status = cv2.imwrite('faces_detected.jpg', img)
		print("[INFO] Image faces_detected.jpg written to filesystem: ", status)



if __name__ == '__main__':
	image = input('Enter your image Name : ')
	cehck_image(image)


