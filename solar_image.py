import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("solar_system!",img)

cv2.waitKey(0)

cv2.putText(img, "Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Mercury",(30,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Venus",(40,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Earth",(50,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Mars",(60,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Jupitar",(70,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Saturn",(80,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Uranus",(90,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img, "Neptune",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imWrite('Solar_System_Names.jpg',img)