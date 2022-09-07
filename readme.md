crear py env

> λ py -m venv venv

-m llamar a un modulo (por convencion la arpeta del entorno se llama venv)

activar entorno virtual

 - linux/mac
 
 > λ source venv/bin/activate

 - windows
 
 > λ .\venv\Scripts\activate

* desactivar entorno virtual

 > λ deactivate

* alias para activar entorno virtual

> λ alias avenv=.\venv\Scripts\activate


* pip install "paquete"

* para ver las dependencias o modulos de tu proyecto 
 > λ  pip freeze

* crear requirements.txt con las dependencias de tu proyecto
 > λ  pip freeze > requirements.txt

* cargar modulos de requirements
 > λ  pip install -r requirements.txt


 