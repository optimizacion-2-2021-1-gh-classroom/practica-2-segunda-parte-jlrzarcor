**Parte 2 de la práctica 2 del curso de Optimización 2 2021-1: reimplementación de secciones de código del paquete construído y preparación para la entrega de su práctica / proyecto final**

Antes de iniciar a trabajar: 


* **Sólo una persona de cada equipo debe darle click a la liga** que está indicada en la publicación del *google classroom*. Una vez que le dé click a la liga tal persona **invite** a sus integrantes de su equipo como **Admin**. Para invitar a su integrante ir dentro del repo a Settings -> Manage Access y enviar la invitación ingresando user de github de su integrante.

* **Su primer *commit* debe ser para renombrar este archivo `README.md` por `old_README.md` para que guarden su contenido y crear otro `README.md` donde me escriban la división de su equipo en una tabla que contenga en una columna *user* de github y en otra columna la tarea a realizar por tal persona (más detalles sobre las tareas en dinámica)**.    
   

# Dinámica

Dividir a su equipo para realizar las siguientes tres tareas. **Ustedes deciden qué integrante resuelve qué tarea (algunas personas tendrán que hacer más de una tarea)**:


1. 2 personas que realicen perfilamiento del código.  

2. 2 personas que realicen reimplementación / adición / eliminación de secciones al código de acuerdo al perfilamiento realizado. 

3. 1 persona que sea *project manager* (más detalles de este rol en las notas), cree nuevos *tests* para la reimplementación / adición / eliminación de secciones al código, haga actualización de documentación hecha con *Sphinx* y *software* en las imágenes de *docker*.

Entre todos los y las integrantes tienen que dar *feedback* si es necesario en la resolución de las tareas que haya duda entre ustedes. El *feedback* consiste en resolver/explicar las dudas que existan. **Las personas asignadas a la tarea correspondiente son las que realizan los *commits* una vez resueltas las dudas**.

Los puntos 1, 2 y 3 anteriores los realizan de forma iterativa hasta finalizar las tareas y que estén en acuerdo las y los integrantes de cada equipo con las soluciones.

**Deben usar `git` para llevar la historia de cambios en la realización de sus notebooks o cualquier otro archivo y subirlos a sus repos. No se revisarán aquellos archivos que tengan un commit con todas las respuestas. El trabajo es incremental.**

**Deben usar la funcionalidad de github**: *issues*, *milestones*, *projects*, *reviewers*, *asignees* o lo que ustedes consideren de github que les ayudará a comunicarse/organizarse (no tienen que usar todas las funcionalidades anteriores y cada equipo decide qué usar). Ver por [ejemplo video para crear proyectos en github](https://youtu.be/z4Xpif7HI04).

# Lenguajes de programación

Ustedes eligen el lenguaje de programación a usar.

# Calificación

La calificación de esta segunda parte es la mitad de la práctica 2. Se asgina una calificación individual por tarea asignada y una calificación por equipo. Se calificará de acuerdo a los *commits* realizados y a los avances que realizan en su trabajo incremental. 

**Tomaré la calificación de esta segunda parte para el % correspondiente del rubro de avances de la** [práctica/proyecto final](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/tree/optimizacion-2-2021-1/proyecto_final). Ver [indicaciones-prácitca/proyecto final](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/tree/optimizacion-2-2021-1/proyecto_final/indicaciones#indicaciones).

# AWS

Adjunten *screenshots* en un directorio de su repo para mostrar su uso de AWS, debe aparecer en el *screenshot* su nombre, clave única u otra forma de identificar su trabajo. En los *screenshots* incluyan la ejecución de su código.

Pueden usar las cuentas de *Educate* si no usan GPUs, si quieren usar GPUs envíenme un mensaje por gitter para usar la cuenta no de *Educate*. 

# Referencias

Notas del capítulo V del [libro de optimización](https://itam-ds.github.io/analisis-numerico-computo-cientifico/README.html)

# ¿Qué hay que entregar/mostrar?

El objetivo es reimplementar los métodos que escribieron en su paquete para hacerlo más eficiente en algún recurso: uso de procesador, memoria o I/O (uds deciden el recurso). Estos cambios de implementación deben de reflejarse automáticamente con *github actions* en la documentación del paquete, *tests* y en sus imágenes de *docker*.

Para hacer más eficiente los métodos de su paquete deben realizar perfilamiento en instancias de AWS. Incluyan características de la instancia en la que lo realizan. El perfilamiento lo realizan a los códigos que ya robustecieron con la parte 1 de la práctica 2 (minikube, kubeflow y kale). 

Una vez realizado el perfilamiento deben evaluar qué utilizarán para hacer más eficiente sus métodos:

* Uso de niveles 2 o 3 de BLAS (preferiblemente nivel 3 de BLAS).

* Uso de compilación a C para secciones de su código.

* Cómputo en paralelo.

* Cómputo concurrente (no lo revisamos en clase pero en la nota 5.1 se dieron referencias de paquetes para realizarlo y lo pueden usar).

* Cómputo distribuido. Por ejemplo, si deben procesar x cantidad de archivos una buena propuesta es procesarlos repartiéndolos en un clúster de máquinas. En este caso una tarea adicional que se debe asignar a una persona es el *setup* del clúster.

Al menos una de las opciones anteriores **deben usar**.

Esta parte 2 utilícenla como preparación para su práctica final. Utilicen los *datasets* que han revisado anteriormente y vayan probando su paquete para el *dataset* que eligieron para su práctica final.

Coloquen su botón de *binder* en su `README.md`.


# Notas

* El código de su paquete lo hicieron en el repo de la parte 2 para la práctica 1. Pueden realizar los cambios en ese repo para no tener su paquete repartido en diferentes repositorios. Uds deciden si quieren tomar esta opción o bien copiar y pegar lo necesario en los repos de esta parte 2.

* Los cambios que realizan al código deben de automáticamente reflejarse en la documentación de su paquete (incluyendo los archivos `.rst` correspondientes o modificándolos de acuerdo a la reimplementación / adición / eliminación de las secciones de su código), pasar *tests*, construcción de sus imágenes de docker de forma automática con *github actions* sin ningún problema.

* Añadan referencias utilizadas para la reimplementación / adición / eliminación de las secciones de su código. Por ejemplo si están basándose en *papers* o páginas para realizar compilación a C o cómputo en paralelo inclúyanlas en su `README.md` o directamente el *paper*.

* **Para la entrega crear un archivo con nombre:** `reporte_equipo_<aquí colocar_número>_parte_2_practica_2.ipynb` que contiene ejecución del paquete en el que se muestra el mejoramiento realizado para el recurso elegido (procesador, memoria u I/O).

* *Project manager*: es la persona más importante para el éxito del proyecto. Conoce el/los objetivo(s) a resolver, detalla las tareas que realizarán el grupo de programación y el grupo de revisión (creación de *tests* en nuestro caso), organiza y asigna a personas a ambos grupos, crea tarjetas en el [project board de github](https://help.github.com/en/github/managing-your-work-on-github/creating-a-project-board) y [milestones](https://help.github.com/en/github/managing-your-work-on-github/tracking-the-progress-of-your-work-with-milestones) para dar seguimiento a [issues](https://help.github.com/en/github/managing-your-work-on-github/creating-an-issue). Mantiene un contacto directo con el prof para dudas que tengan y para avisar en qué fase se encuentran. Les explica a su equipo de trabajo la correcta creación de *issues*, solución de los mismos y el uso de *milestones* y del *project board*.

* La división de las tareas y roles está está inspirada en el *framework* [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) en un ambiente laboral real (y en esta práctica estamos super-simplificando tal *framework*).

* Añadan referencias utilizadas para su trabajo en su `README.md`.

* **Los commits deben tener un mensaje explicatorio, no hacer lo siguiente:**

```
git commit -m "create 1" -i archivo1.txt

git commit -m "update 1" -i archivo1.txt #qué es update 1?

git commit -m "update 2" -i archivo1.txt #qué es update 2?

git commit -m "update 3" -i archivo1.txt #qué es update 3?
```

**así también para los *issues*, *projects*, *milestones*...**

* Esta organización es nuestro *playground* utilicen los repos de aquí para practicar :)

* Recuerden:

    * usar `git` para llevar la historia de sus cambios en sus repos :)
    * poner las referencias que utilizan (aún si le preguntan a una compañera o compañero de la clase coloquen esto en su entrega) pues no está permitido copiar y escribir que lo hicieron sin citar sus fuentes.


* Para dudas creen un *room* de gitter e ínvitenme :) (si ya lo hicieron omitan este enunciado)

* **Su trabajo individual y su tiempo es muy valioso e importante, también el trabajo en equipo. Si alguna persona del equipo no realizó su tarea asignada, esperaría que lo resolvieran entre ustedes, si no lo resuelven avísenme y no realicen su tarea asignada. Si tienen algún problema (familiar, salud,...) infórmenme con tiempo para ver qué podemos hacer :)**


