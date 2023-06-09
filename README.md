# [TutoUN](http://fguerrerot.pythonanywhere.com/)
*Ultima actualización 02-06-2023 con las mejoras del informe 6*

Plataforma enfocada a la búsqueda de tutores dentro de la comunidad de la universidad nacional de Colombia
sede Medellin.

## Tabla de contenido
- Desarrolladores
- Descripción
- Trabajando en el proyecto
- Guía de instalación
- Guías de contribución
- Licencia

## Desarrolladores
- Federico Guerrero Trejos
- Juan Jose Ospina Erazo

## Estructura de las Carpetas
**TutoUN**: Es la carpeta principal del proyecto, aquí encontrarás los archivos de configuración del proyecto Django como settings.py, urls.py y wsgi.py. settings.py contiene todas las configuraciones del proyecto, urls.py contiene las rutas del proyecto y wsgi.py sirve como punto de entrada para servidores web compatibles con WSGI.

**Core**: esta carpeta se utiliza para los archivos del proyecto que son esenciales, como las configuraciones personalizadas, utilidades y funciones comunes utilizadas en todo el proyecto, aqui encontraremos la plantilla base de la pagina en la cual podemos encontrar tanto el header como el footer de la pagina.

***templates\core: ***
***base.html:*** Aqui encontraremos el archivo modelo del proyecto, el header y el footer por defecto asi como el estilo base
***home.html*** Aqui encontraremos lo correspondiente a la pagina inicial de la aplicación, el home

**Favoritos**: Esta carpeta contiene todo lo relacionado con la funcionalidad de marcar tutores favoritos por parte de los estudiantes.

**Mensajes**: Esta carpeta maneja la funcionalidad de los mensajes entre tutores y estudiantes. Esto incluye los modelos para los mensajes, las vistas para enviar y recibir mensajes y las plantillas para mostrar los mensajes.

**Perfiles**: Esta carpeta contiene los modelos, vistas y plantillas relacionados con los perfiles de los usuarios, ya sean tutores o estudiantes.

**Static**: Carpeta que se utiliza para almacenar archivos estáticos como CSS, JavaScript e imágenes.

**Tutorias**: En esta carpeta, se maneja todo lo relacionado con las tutorías, incluyendo los modelos para las tutorías, las vistas para crear, ver y editar tutorías y las plantillas para mostrar la información de las tutorías.

**Users**: Aquí se tiene la funcionalidad para manejar los usuarios de la aplicación. incluyendo los modelos de usuario, las vistas para el registro e inicio de sesión, y las plantillas para el registro e inicio de sesión.

**Versiones**: Contiene las diferentes versiones del proyecto, registros de cambios, segun los informes presentados

## Descripción
 Este aplicativo provee una conectividad entre tutores y estudiantes para la Universidad Nacional de Colombia, que permita a los estudiantes 
 buscar e interactuar con tutores particulares para recibir asesoría en diferentes materias y habilidades. 
 
 La aplicación también permitirá a los tutores crear perfiles detallados con información sobre su metodología de enseñanza, experiencia y 
 tarifas, y a los estudiantes calificar y dar comentarios sobre la calidad de la enseñanza recibida. 
 El objetivo final es diversificar el acceso a alternativas que apoyen y complementen el aprendizaje y el desarrollo académico de los 
 estudiantes dentro de la institución

## Uso de la herramienta
Para poder usar la herramienta simplemente debe ingresar al enlace de la pagina web ubicado al inicio de este documento, allí podrá interactuar con las diferentes funcionalidades que ofrece TutoUN.

## Guía de instalación
Para poder instalar y manipular el código del proyecto en su maquina local, debe tener instalado python 3.8.5 o superior, ademas de tener instalado el gestor de paquetes pip.
Se recomienda ademas el uso de virtualenv para poder crear un entorno virtual y poder trabajar de forma mas organizada.
Instalación de dependencias:

"python -m pip install -r requirements.txt"

## Guías de contribución
Si se esta interesado en aportar en el proyecto por favor tener en cuenta:

- Realizar sus aportes un una rama nueva, sin afectar la principal. 
- Realizar commits cortos que permitan hacer un seguimiento fácil del código.
- Describir a detalle que se hace en cada commit y ademas, comentar debidamente el código.

## Licencia
GPL Vs3
