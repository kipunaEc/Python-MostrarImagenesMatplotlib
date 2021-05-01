import os
import cv2
import matplotlib.pyplot as plt

dirCarpeta = '/home/noemi/Escritorio/matplotlib_Img/Imagenes_Ecuador/'
archivos = os.listdir(dirCarpeta)

img_array = []
titulos_array = []

for x in range (0,len(archivos)):
    dirArchivo = dirCarpeta + archivos[x]
    imgBGR = cv2.imread(dirArchivo)
    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    img_array.append(imgRGB)

    img_ext = archivos[x]
    nomImagen = img_ext[:-4]
    titulos_array.append(nomImagen)
    print(titulos_array)
    
    plt.subplot(3,3,x+1)
    plt.xticks([]), plt.yticks([])
    plt.xlabel(titulos_array[x])
    plt.imshow(img_array[x])

plt.suptitle('Lugares del Ecuador')
plt.savefig('lugaresEcuador.jpg')
plt.show()
