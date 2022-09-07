* crear py env

py -m venv venv

-m llamar a un modulo (por convencion la arpeta del entorno se llama venv)

* activar entorno virtual

 - linux/mac
 source venv/bin/activate

 - windows
 .\venv\Scripts\activate

* desactivar entorno virtual

 - deactivate

* alias para activar entorno virtual

- alias avenv=.\venv\Scripts\activate


* pip install "paquete"

* para ver las dependencias o modulos de tu proyecto 
 - pip freeze

* para crear requirements.txt con las dependencias de tu proyecto
 - pip freeze > requirements.txt

* para cargar modulos de requirements
 - pip install -r requirements.txt


 