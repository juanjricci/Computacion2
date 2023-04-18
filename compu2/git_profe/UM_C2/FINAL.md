
## Requisitos examen final

Para poder rendir el examen final es requisito haber regularizado la materia a fin del semestre.

El examen final consistirá en la exposición de un código integrador desarrollado por el alumno, cuyo tema será acordado previamente con el profesor.

### Consideraciones del código:
El código debe solucionar un problema haciendo uso de las herramientas vistas en clase. Debe incluir aspectos como:
* Uso de Sockets con conexión de clientes múltiples de manera concurrente.
* Uso de mecanismos de IPC
* Uso de asincronismo de I/O
* Uso de cola de tareas distribuidas

Como aspectos opcionales adicionales puede considerarse:
* Despliegue en contenedores Docker
* Parseo de argumentos por línea de comandos
* Almacenamiento de datos en bases de datos

### Presentación
La aplicación a desarrollar deberá ser acordada previamente con el profesor de la cátedra.
Una vez desarrollada, deberá ser presentada al profesor al menos una semana antes de la mesa de examen final, para que éste pueda visarla y dar el visto bueno al alumno.
El código deberá ser presentado en un repositorio GIT (o un subdirectorio del repositorio git del alumno), bien organizado, y con el agregado de los siguientes archivos markdown:
* **INSTALL**: contendrá las instrucciones para clonar e instalar/lanzar la aplicación.
* **README**: contendrá la ayuda y uso básico de la aplicación.
* **README.info**: contendrá un breve informe sobre las decisiones principales de diseño del sistema, y su justificación (ej, por qué un determinado modelo de datos, o tipo de almacenamiento, o uso de multiproceso/multithread, etc).
* **README.todo**: contendrá una lista detallada de mejoras y posibles nuevas características/features del sistema para futuras versiones.

Durante la presentación, el alumno expondrá el funcionamiento de la aplicación, explicará el código fuente y tecnologías utilizadas, y el tribunal de la mesa de examen podrá realizar preguntas teóricas sobre los contenidos prácticos expuestos por el alumno.
El tribunal también podrá solicitar pequeños *fixes* de bugs detectados durante la presentación, y pequeñas modificaciones del código.

### Nota:
El código deberá ser desarrollado de manera incremental, por lo que se valoran cambios progresivos (commits) en el repositorio de software durante todo el proceso de desarrollo.
