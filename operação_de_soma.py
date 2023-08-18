# importando bibliotecas e autorizando o imshow
import numpy as np
import cv2
#from google.colab.patches import cv2_imshow

# importando uma imagem do disco para o colab
#from google.colab import files
#uploaded = files.upload()

#ler e exibir uma imagem
img = cv2.imread("charmander.png")
#yae = cv2.imread("yae.png")

#imprimindo a imagem
cv2.imshow("Charmander", img)
#cv2_imshow(yae)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
cv2.imshow("Cinza", cinza)

valor = 50
cinza_com_valor = cinza

for i in range(cinza_com_valor.shape[0]):
  for j in range(cinza_com_valor.shape[1]):
    if(cinza_com_valor[i, j] + valor <= 255):
      cinza_com_valor[i, j] += valor

cv2.imshow("Cinza com valor", cinza_com_valor)

limear = 70

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

for i in range(cinza.shape[0]):
  for j in range(cinza.shape[1]):
    if(cinza[i, j] > limear):
      cinza[i, j] =+ limear
    else:
      cinza[i, j] = 0

cv2.imshow("Cinza 1", cinza)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

for i in range(cinza.shape[0]):
  for j in range(cinza.shape[1]):
    if(cinza[i, j] > limear):
      cinza[i, j] = 255
    else:
      cinza[i, j] =+ limear

cv2.imshow("Cinza 2", cinza)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

for i in range(cinza.shape[0]):
  for j in range(cinza.shape[1]):
    if(cinza[i, j] > limear):
      cinza[i, j] = 255
    else:
      cinza[i, j] = 0

cv2.imshow("Cinza 3", cinza)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

for i in range(cinza.shape[0]):
  for j in range(cinza.shape[1]):
    if(cinza[i, j] > limear):
      cinza[i, j] = 0
    else:
      cinza[i, j] = 255

cv2.imshow("Cinza 4", cinza)

img_blur = img
img_blur = cv2.blur(img, (50, 50))

cv2.imshow("Blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()