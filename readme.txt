Preparación del ambiente para gesbod:
a. Opcional, actualizar gestores de paquetes y librerias base del entorno.
actualizar conda:
conda update conda --yes

actualizar pip:
python -m pip install --upgrade pip


Cargar librerias base (autopep y flake8)
cargar linters y formateadores.
pip install -r base-requirements.txt


b. crear el ambiente virtual.
conda create --name gesbod python=3.7 --yes

c. activar el ambiente virtual.
conda activate gesbod

d. Cargar las librerías necesarias, se debe estar dentro del ambiente virtual.
pip install -r requirements.txt

e. desactivar el ambiente virtual.
conda deactivate

f. Eliminar el ambiente virtual, primero debe desactivar el ambiente virtual antes de eliminarlo.
conda remove --yes --name gesbod --all


para instalar el cliente de oracle:
python -m pip install cx_Oracle
