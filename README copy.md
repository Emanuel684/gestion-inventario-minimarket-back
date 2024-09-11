# API REACTORES NUCLEARES
Esta API busca construir una API REST que implemente el patrón repositorio, con
una distribución por capas de la siguiente manera:

- **Controlador Manejo de peticiones y respuestas asociadas a verbos HTTP**
- **Servicio Implementación de las validaciones de las reglas del negocio**
- **Repositorio Ejecución de acciones CRUD asociadas a cada operación**
- **Modelo Clases que definen el estado y comportamiento de las entidades**
- **Contexto Conexión a la base de datos.** 

Los datos utilizados para la implementacion de esta API son de
**Organismo Internacional de Energía Atómica**

## IMPLEMENTACION DEL MODELO DE DATOS
![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqnfoaRmpvY36QiuaivXELcdenP_23yTZ2y9TLJZVY6mzCzdUnAD-D0eY50-GLpta-2CaGJzzk9IkrFeHPWKf7r6DyeH0qIH-9zpeyVGZIr3vJkLW8TVetLvR-Kw0dVfRJuGTYrxyWlQFXg6J3QcG8GQ5-k5LpjqddI004hNoe9SMdZB2gKmE1x_bOxIQ/s769/diagrama_topicos_avanzados.drawio.png)


## ENDPOINTS IMPLEMENTADOS
Inventario de peticiones que se implementa en la API:

### REACTORES
1. Obtener reactores registrados -> GET -> http://127.0.0.1:8000/reactores/reactores-registrados
2. Obtener un reactor por Id -> GET -> http://127.0.0.1:8000/reactores/reactor-identificador/{identificador}
3. Crear un nuevo reactor -> POST -> http://127.0.0.1:8000/reactores/crear-reactor
4. Actualizar un reactor existente -> PUT -> http://127.0.0.1:8000/reactores/actualizar-reactor
5. Eliminar un reactor existente -> DELETE -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}

### TIPO_REACTORES
6. Obtener tipos de reactores registrados -> GET -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}
7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo. -> GET -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}

### UBICACIONES REACTORES
8. Obtener Ubicaciones Registradas -> GET -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}
9. Obtener Ubicación por Id. -> GET -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}
10. Obtener Reactores registrados por Ubicación -> GET -> http://127.0.0.1:8000/reactores/eliminar-reactor/{identificador}


# DOCUMENTACION
Aqui encontraras todo el conocimiento posible para utilizar esta API

## CONEXION CON LA BASE DE DATOS
Esta conexion se encuentra en la carpeta 
> **properties**

Dentro de esta carpetas encontraras el scrip **settings.py**
Aqui encontraras un string de conexion a la base de datos con la siguiente estructura

> **'system/iaea_123@localhost:1523/IAEA'**

## CORRER API
Para poner a correr esta API es necesario seguir los siguientes pasos

1. Clonar el repo en un directorio deseado, para esto utilizas el comando:
    > git clone https://github.com/Emanuel684/tadb_202410_ex03.git
2. Abrir el proyecto con tu IDE preferido
3. Crear un entorno virtual de python 
4. Es necesario que cuentes con una version de python 3.11 o mayor para su funcionamiento
5. Es necesario que tengas la base de datos corriendo en local, de esto hablaremos mas adelantes
6. En el directorio raiz de la aplicacion corres el siguiente comando
    > python3 -m venv ./venv
7. Ya con tu entorno creado es necesario ingresar a este
    > venv\Script\activate (Este comando cambia dependiendo de la shell que utilices y el sistema operativo)
8. Instalamos todas las dependencias de este proyecto
    > pip install -r requirements.txt
9. Para correr el API corremos el siguiente comando
    > uvicorn main:app --reload

## DOCUMENTACION DE SWAGGER
Esta documentacion la puedes encontrar despues de iniciar el API en la siguiente
dirección 

http://127.0.0.1:8000/docs#/

## BASE DE DATOS DE ORACLE
Para implementar la base de datos de oracle tenemos una carpeta llamada
> **/implementacion_modelo_datos**

En esta carpeta puedes encontrar todo lo necesario para implementarla y correra
RECUERDA QUE SE IMPLEMENTO CON DOCKER COMPOSE.

### IMPLEMENTAR EL MODELO DE DATOS
Encontraras en la carpeta
> **/implementacion_modelo_datos**

Un archivo llamado **Documentacion_proceso.docx** y **Documentacion_proceso.pdf**
Aqui encontraras todos los pasos para implementarla

# Sobre el creador de esta API
<h1 align="center">Hola 👋, Soy Emanuel Acevedo Muñoz</h1>
<h3 align="center">Un apasionado desarrollador de software full stack, estudiante de ingeniería en ciencia de datos</h3>

- 🔭 Actualmente estoy trabajando en [Quipux](https://www.quipux.com/web/)

- 🌱 Actualmente estoy aprendiendo **Python, Aws**

- 👯 Estoy buscando colaborar en **data science projects**

- 🤝 Estoy buscando ayuda con **data science**

- 👨‍💻 Todos mis proyectos están disponibles en [https://emanuelacevedo.netlify.app/](https://emanuelacevedo.netlify.app/)

- 📝 Escribo regularmente artículos sobre [https://www.linkedin.com/in/emanuel-acevedo-mu%C3%B1oz-1b062b204/](https://www.linkedin.com/in/emanuel-acevedo-mu%C3%B1oz-1b062b204/)

- 💬 Preguntame sobre **React Native, Java Script, Aws, Flutter, React, NodeJS, MongoDB, MySQl, PostgreSQL**

- 📫 Como llegar a mi **emanuelacag@gmail.com**

- 📄 Conoce mis experiencias [https://www.linkedin.com/in/emanuel-acevedo-mu%C3%B1oz-1b062b204/](https://www.linkedin.com/in/emanuel-acevedo-mu%C3%B1oz-1b062b204/)

- ⚡ Fun fact **Creo que necesito aprender más.**

<h3 align="left">Conectate conmigo:</h3>
<p align="left">
</p>

<h3 align="left">Herramientas:</h3>
<p align="left"> <a href="https://aws.amazon.com/amplify/" target="_blank" rel="noreferrer"> <img src="https://docs.amplify.aws/assets/logo-dark.svg" alt="amplify" width="40" height="40"/> </a> <a href="https://angular.io" target="_blank" rel="noreferrer"> <img src="https://angular.io/assets/images/logos/angular/angular.svg" alt="angular" width="40" height="40"/> </a> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://dart.dev" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/dartlang/dartlang-icon.svg" alt="dart" width="40" height="40"/> </a> <a href="https://expressjs.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original-wordmark.svg" alt="express" width="40" height="40"/> </a> <a href="https://www.figma.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/figma/figma-icon.svg" alt="figma" width="40" height="40"/> </a> <a href="https://firebase.google.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/firebase/firebase-icon.svg" alt="firebase" width="40" height="40"/> </a> <a href="https://flutter.dev" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/flutterio/flutterio-icon.svg" alt="flutter" width="40" height="40"/> </a> <a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.java.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg" alt="java" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://nodejs.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/> </a> <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://pugjs.org" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/pug.svg" alt="pug" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://reactnative.dev/" target="_blank" rel="noreferrer"> <img src="https://reactnative.dev/img/header_logo.svg" alt="reactnative" width="40" height="40"/> </a> <a href="https://redux.js.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redux/redux-original.svg" alt="redux" width="40" height="40"/> </a> <a href="https://sass-lang.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sass/sass-original.svg" alt="sass" width="40" height="40"/> </a> <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/> </a> </p>


