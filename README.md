# Galería de imagenes 

Aplicación de galería de imágenes desarrollado por Briant Arango, Elías Samudio y Julio Montenegro.

## Resumen del proyecto
Los usuarios pueden subir imágenes a un perfil, etiquetarlas y organizarlas en álbumes. Los visitantes pueden ver las galerías. 

![Captura de Pantalla que muestra la página de inicio de la aplicación de galería de imagenes](<Captura de pantalla 2024-11-27 101259.png>)

## Prerequisitos para ejecutar el servidor localmente
- Clone el repositorio en un directorio
- Creé un entorno virtual en donde instalará las librerías que utiliza este proyecto.
- Después de crear el entorno virtual, escriba en la terminal pip install -r requirements.txt
- Haga las migraciones antes de ejecutar el servidor, escriba en la terminal "python manage.py makemigrations" y luego "python manage.py migrate"

## ¿Cómo funciona la aplicación?
- Cuando se entra a la página web sin tener una cuenta registrada, aparecerán imágenes subidas por usuarios que hayan creado una cuenta.
    - Una vez que se haya creado una cuenta, esta iniciara sesión automáticamente.

- Si le hacemos click a las palabras de "Iniciar Sesión" y "Cree una cuenta" nos llevarán a formularios de inicio de sesión y creación de cuenta respectivamente
    - Si le hacemos click a los botones de "Más detalles" de una imagen o si le damos click a la palabra de "Subir imagen" sin estar registrados en la aplicación, nos llevarán al formulario de creación de cuenta.
## ¿Cómo subir una imagen?

![Captura de pantalla de la ventana de "Mi Galería" de la aplicación Web](<Captura de pantalla 2024-11-27 105034.png>)

* Después de crear una cuenta, seremos redirigidos a la ventana de Mi Galería, cómo aún no hemos subido ninguna imagen, la página se mostrará vacía.



![alt text](<Captura de pantalla 2024-11-27 105956.png>)

* Este es el formulario de subida de imágenes, en el cual tenemos los campos de Nombre, Etiquetas e Imagen para llenar, desde el campo de Imagen podemos seleccionar cualquier imagen que está en nuestra máquina para subirla
    *El campo de imagen es obligatorio de llenar

![Captura de pantalla de la ventana de "Mi Galería" de la aplicación Web](<Captura de pantalla 2024-11-27 111951.png>)
* En el botón de "Más Detalles" podremos ver más información sobre la imagen que está en nuestra galería.

![Captura de pantalla de la ventana de "Mas Detalles" de la aplicación Web](<Captura de pantalla 2024-11-27 113738.png>)

* Si ya no tenemos nada más por hacer, podemos cerrar sesión

![Captura de pantalla de la página principal de la aplicación Web que contiene la imagen que acabamos de subir](<Captura de pantalla 2024-11-27 114212.png>)

* Y la imagen que acabamos de subir se muestrá en la página principal!
