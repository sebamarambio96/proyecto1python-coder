## Apuntes Django

## Link Video 
Video en el cual se detallan las funcionalidades del proyecto:

https://www.loom.com/share/f5f0f3105d68490a855146caa44ec566

--------------------
SuperUsuario: admin
pass: admin123

## Instalar dependencias

pip install -r requirements.txt

## Iniciar entorno virtual

entorno-virtual\Scripts\activate 

## Iniciar servidor

python manage.py runserver   

## Test

Se escribio un test que revisa que las noticias se agreguen correctamente a la base de datos:

python manage.py test

## Detalles

Reemplacé el boton "Leer más" por un link asociado al título de la noticia por fines meramente estéticos.

Pára verificar el ingreso de los datos a la bbdd debe ir a listar noticias y usuarios, o tambien puede entrar en:
# http://localhost:8000/admin/

Utilice las credenciales indicadas al inicio del documento
