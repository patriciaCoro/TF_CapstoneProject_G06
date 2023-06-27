# CapstoneProject G06
## Título 
  Verificación de firmas fuera de línea con Redes Neuronales Convolucionales

## Integrantes
- Patricia Flor Coronación Mendoza
- Mishely Licel Loyola Sebastián 

# Profesor
- Pedro Shiguihara Juarez

# Requisitos técnicos
- Gestor de entorno miniconda
- Python 3.11.3 
- Jupyter notebook

# Pasos

1. Descargar o clonar el proyecto.
2. Activar el ambiente ejecutando el .yml
  ```
  conda env create -f envfirmasfinal.yml
  ```
Cabe resaltar que en este entorno envfirmasfinal ya se encuentran instaladas los siguientes librerías: 
  ```
  pip install jupyter notebook
  pip install numpy
  pip install torch
  pip install pandas
  pip install matplotlib
  pip install ipykernel
  pip install opencv-python
  pip install keras
  pip install tensorflow
  pip install scikit-learn
  pip install keras_preprocessing
  ```
3. Crear el kernel asociado al entorno

  ```
  python -m ipykernel install --user --name envfirmasfinal --display-name "envfirmasfinal"
  ```
4. Ejecutar el archivo ModeloVerificacion.py y ModeloVGG19DutchFinal.ipynb seleccionado el kernel creado.

5. Ejecutar el archivo Verificar.py enviando el parámetro de la ruta de la imagen
  ```
  python Verificar.py -i [ruta] -m [modelo]
  ``` 

# Dataset
  El dataset utilizado SigWiComp2011(ICDAR2011) se encuentra disponible para su descarga en la siguiente link:
  TC11
  http://www.iapr-tc11.org/mediawiki/index.php/ICDAR_2011_Signature_Verification_Competition_(SigComp2011)
  Kaggle
  https://www.kaggle.com/datasets/robinreni/signature-verification-dataset
