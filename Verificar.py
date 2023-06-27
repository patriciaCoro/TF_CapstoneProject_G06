import argparse
import sys
import cv2
from keras.models import load_model
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--imagen', required = True, help='Ingresa la ruta de la imagen')
    ap.add_argument('-m', '--modelo', required = True, help='Elige el modelo a utilizar: cnnBase o cnnVGG19')
    args = vars(ap.parse_args())
    sys.stdout.write(str(verificar(args)))
    

def cambio_formato(imagen,tipo):
    if tipo == 'vgg19':
        ruta = imagen
        archivo = []
        SIZE = 224 
        img = cv2.imread(ruta)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (SIZE,SIZE))
        archivo.append([img])
        archivo = np.array(archivo)/255.0
        a=archivo.reshape(-1, SIZE,SIZE, 3)
        return a
    else:
        size= 200
        ruta = imagen
        archivo = []
        img = cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (size, size))
        archivo.append([img])
        archivo = np.array(archivo)/255.0
        a=archivo.reshape(-1, size,size, 1)
        return a

def verificar(args):
    if args['modelo'] == 'cnnBase':
        model2 = load_model('modeloNetwork.h5')
        ruta_imagen = args['imagen']
        input = cambio_formato(ruta_imagen,'cnnBase')
        result = model2.predict(input)
        resultado_final= np.argmax(result,axis=1)
        if resultado_final == 0:
            print("La firma ingresada es auténtica")
        else:
            print("La firma ingresada es una falsificación")

    elif args['modelo'] == 'cnnVGG19':
        model = load_model('modeloVGG19D.h5')
        ruta_imagen = args['imagen']
        input = cambio_formato(ruta_imagen,'vgg19')
        result = model.predict(input)
        resultado_final= np.argmax(result,axis=1)
        if resultado_final == 0:
            print("La firma ingresada es auténtica")
        else:
            print("La firma ingresada es una falsificación")



if __name__=='__main__':
    main()
