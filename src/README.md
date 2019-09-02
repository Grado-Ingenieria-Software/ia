# POMPDP | IA | 2018/19
## Requisitos
El programa debe ejecutarse desde el prompt de Anaconda, usando el comando
`$ pip install -r requirements.txt`
En caso de error con la librería graphviz. Instalar esta por separado. Todas las ejecuciones se han realizado sobre el prompt de Anaconda.
Se recomienda el uso de Python 3.5.2
## Ejecución
La información puede ser introducida mediante interfaz gráfica o mediante consola.
```
    //Mediante consola
    $ python ./main.py

    //Mediante interfaz gráfica
    $ python ./interfaz.py	
```
## MODO DE USO
### Modo Consola
Cuando se ejecuta la terminal en modo consola aparecerán varios mensajes que indicaran opciones a elegir. Estas opciones deberán ser seleccionadas introduciendo el numero situado a su izquierda y pulsando "Enter".

Otras opciones como el presupuesto o el máximo de acciones permitidas son insertadas el valor. En caso de pulsar "Enter" sin ningún valor, estas tomaran un valor por defecto mencionado en el comentario bajo la cabecera.


### Modo gráfico

En La interfaz gráfica existe la posibilidad de introducir las mismas opciones que en el modo consola, solo que esta dispone de tres desplegables(Problema, Algoritmo y Tipo de simulación) y dos campos numéricos para el presupuesto y máximo de pasos.

Las confirmaciones de ejecución y resultados aparecen en la terminal.

## Salir de la ejecución
En cualquier momento el usuario puede pulsar Ctrl + C para salir de la simulación/programa.
