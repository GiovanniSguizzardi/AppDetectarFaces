import cv2
#Nome biblioteca: opencv-contrib-python

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

#Path da imagem a ser lida
foto = cv2.imread("Pessoas.png")

foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza, scaleFactor=1.03)

for x, y, l, a in faces_detectadas:
    #arquivo_img, ponto_incial, ponto_final, cor
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a), (0,0,255), 3)

print(faces_detectadas)
print("Pessoas encontradas: ", len(faces_detectadas))
cv2.imshow("[ Imagem: Pessoas.png ]", foto)
cv2.waitKey()
