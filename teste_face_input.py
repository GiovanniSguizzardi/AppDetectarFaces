import cv2
#Nome biblioteca: opencv-contrib-python

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

foto = cv2.imread("Pessoas.png")
foto2 = cv2.imread("Messi.png")
foto3 = cv2.imread("ElonMusk.png")

foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza)

for x, y, l, a in faces_detectadas:
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a) )
#print(faces_detectadas)

x = int(input("Digite sua opção: "))

if x == 1:
    foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    faces_detectadas = detector.detectMultiScale(foto_cinza)
    cv2.imshow("Imagem: Pessoas.png", foto)
    cv2.waitKey()

elif x == 2:
    foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    faces_detectadas = detector.detectMultiScale(foto_cinza)
    cv2.imshow("Imagem: Messi.png", foto2)
    cv2.waitKey()

elif x == 3:
    foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    faces_detectadas = detector.detectMultiScale(foto_cinza)
    cv2.imshow("Imagem: ElonMusk.png", foto3)
    cv2.waitKey()
