# CapstoneProject G06
## Título 
  Verificación de firmas fuera de línea con Redes Neuronales Convolucionales

## Integrantes
- Patricia Flor Coronación Mendoza
- Mishely Licel Loyola Sebastián 

# Profesor
- Pedro Shiguihara Juarez

# Requisitos técnicos
Gestor de entorno miniconda
Python 3.11.3 
Jupyter notebook

# Pasos

1. Descargar o clonar el proyecto.
3. Activar el ambiente ejecutando el .yml
```
conda env create -f envfirmasfinal.yml
```
4. Ejecutar el archivo ModeloVerificacion.py y ModeloVGG19DutchFinal.ipynb 

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
