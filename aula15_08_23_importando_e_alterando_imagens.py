
import numpy as np
import cv2
#from google.colab.patches import cv2_imshow

# importando uma imagem do disco para o colab
#from google.colab import files
#uploaded = files.upload()

#ler e exibir uma imagem
img = cv2.imread("mario.jpg")

#imprimindo a imagem
cv2.imshow("Imagem", img)

#dimensões da imagem
print(img.shape)

#acessando um pixel
b, g, r = img[125, 45]
print(f'b=', b)
print(f'g=', g)
print(f'r=', r)

#dividindo os canais da imagem
azul, verme, verde = cv2.split(img)
cv2.imshow("Azil", azul)
cv2.imshow("Verme", verme)
cv2.imshow("Verde", verde)

#alterando pixels diretamente na imagem
for i in range (324):
  img[10, i] = [255, 255, 255]
cv2.imshow("Imagem", img)

#alterando a intensidade do canal específico
for i in range (img.shape[0]):
  for j in range (img.shape[1]):
    img.itemset((i, j, 2), 0)
cv2.imshow("Imagem", img)

"""exercício 1

leia uma nova imagem e processe-a, de modo que a imagem resultante preserve apenas os pixels que apresentem maior predominância do canal vermelho. Os demais pixels serão alterados para a cor branca

exercício 2

usando a função cvtColor, transforme a imagem original exebindo-a em HSV e em tons de cinza.
"""

# ler e exibir uma imagem
mario = cv2.imread("mario.jpg")
#img_2b = cv2.imread("hsv cube.png")

#imprimindo a imagem
cv2.imshow("Mario", mario)
#cv2_imshow(img_2b)

#exercicio 1

img = cv2.imread("hsv cube.png")

#todos os valores
cv2.imshow("Imagem", img)
#print("Apenas valores próximos do vermelho")

#valores aproximados de vermelho - resto preenchido com brando
for i in range(img.shape[0]):
  for j in range (img.shape[1]):
    b, g, r = img[i, j]
    if(r < g or r < b):
      img[i, j] = [255, 255, 255]

cv2.imshow("Valores vermelhos", img)

#exercicio 2

#Imprimindo HSV
hsv = cv2.cvtColor(mario, cv2.COLOR_BGR2HSV )
cv2.imshow("HSV", hsv)

#Imprimindo apenas tons de cinza
cinza = cv2.cvtColor(mario, cv2.COLOR_BGR2GRAY )
cv2.imshow("Cinza", cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()