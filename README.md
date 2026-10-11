---
math: true
---

{% assign tp = site.data.trabajos.TP2 %}
{% capture fecha %}{{tp.entrega | date: "%e/%m"}}{% endcapture %}

# Trabajo Práctico 2: Programación Dinámica For The Win

El presente trabajo busca evaluar el desarrollo y análisis de un algoritmo 
de Programación Dinámica. 
La fecha de entrega del mismo es el 12/10/2026.

## Introducción

Seguimos con la misma situación planteada en el trabajo práctico anterior, pero ahora pasaron varios años. 
Mateo ahora tiene 7 años. Los mismos años que tenía Sophia cuando comenzaron a jugar al juego de las monedas. Eso quiere decir que Mateo también ya aprendió sobre algoritmos greedy, y lo comenzó a aplicar. Esto hace que ahora quién gane dependa más de quién comience y un tanto de suerte. 

Esto no le gusta nada a Sophia. Ella quiere estar segura de ganar siempre. Lo bueno es que ella comenzó a aprender sobre programación dinámica. Ahora va a aplicar esta nueva técnica para asegurarse ganar siempre que pueda. 

## Consigna

1. 	[**Obligatorio**]  Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente
	y proponer un algoritmo por programación dinámica 
	que obtenga la solución óptima al problema planteado: Dada la secuencia de monedas
	$$m_1, m_2, \cdots, m_n$$, sabiendo que Sophia empieza el juego y que Mateo siempre elegirá
	la moneda más grande para sí entre la primera y la última moneda en sus respectivos turnos, 
	definir qué monedas debe elegir Sophia para asegurarse obtener el **máximo valor acumulado posible**.
	Esto no necesariamente le asegurará a Sophia ganar, ya que puede ser que esto no sea posible, dado
	por cómo juega Mateo. Por ejemplo, para `[1, 10, 5]`, no importa lo que haga Sophia, Mateo ganará.
3. 	[**Obligatorio**] Demostrar que la ecuación de recurrencia planteada en el punto anterior en efecto nos lleva a
	obtener el **máximo valor acumulado posible**. 
4.	[**Obligatorio**] Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. 
5.	[**Opcional**] Analizar si (y cómo) afecta a los tiempos del algoritmo planteado la
	variabilidad de los valores de las monedas. Como caso particular, considerar casos en los que en el TP1 el algoritmo
	Greedy no permitía que Sophia gane (si que empate) cuando había alguna forma para que ella pudiera ganar. 
7. 	[**Opcional**] Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, 
	el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también. 
8. 	[**Opcional**] De las pruebas anteriores, hacer también mediciones de tiempos para corroborar la complejidad teórica 
	indicada. Realizar gráficos correspondientes. Generar todo set de datos necesarios para estas pruebas.
9.	[**Opcional**] Agregar cualquier conclusión que parezca relevante.  


## Entrega

Debe enviarse al corrector asignado, por mail o slack, el link
al repositorio donde se encuentre el código fuente, y donde debe encontrarse
el informe en formato PDF, que debe seguir los lineamientos establecidos en el TP1. 
En este caso, la forma de ejecutar el programa debe ser: 
```
python3 tp2.py data/listado-monedas.txt
```

El formato de salida debe ser parecido a los ejemplos de salidas brindados. No es necesario que sea exactamente igual, y pueden modificar algo en función de lo que analicen, pero debe mantenerse similar.

Nuevamente, la nota del trabajo práctico tendrá en cuenta tanto la presentación y calidad de lo presentado, 
como también el desarrollo del trabajo. No será lo mismo un trabajo realizado con lo mínimo
indispensable, que uno bien presentado, analizado, y probado con diferentes volúmenes, set de 
datos, o estrategias de generación de sets, en el caso que corresponda. 

Si bien nos parece que no debería ser necesario de aclarar, cualquier uso de "ayudas externas" para realizar el trabajo práctico, incluyendo el informe (por ejemplo, cualquier tipo de Inteligencia Artificial) resultará en la desaprobación del trabajo práctico, y de allí de la cursada. Nos interesa entender el proceso de análisis que hacen ustedes, personas. 

Sobre puntos obligatorios y opcionales: 
* La idea de hacer electivos algunos puntos es que aquellos grupos que consideren que estos trabajos no hacen a su formación, simplemente hagan lo mínimo, y quienes consideren que este desarrollo les puede aportar (especialmente para materias futuras) o bien quieran resolver un problema utilizando lo visto en la materia, tengan un lugar para hacerlo. 
* Los puntos opcionales no son necesarios para aprobar, pero cada uno contribuye a tener mejor nota.
* En caso que los puntos obligatorios no estén aprobables, se reenviará a reentrega. Si un punto opcional no está aprobable simplemente se considerará para la nota del trabajo práctico (eventualmente, según el detalle de lo que corresponda, podría reentregarse para mejorar nota). 
* Para la fecha de entrega, los puntos obligatorios deben estar hechos. En caso de no hacerse, se dará una única semana (sin posibilidad de extensión) para que estos puntos (y solo estos, no los electivos) estén completados para tener un máximo de 4 de nota, y en caso de no encontrarse en condiciones de aprobar, el trabajo quedará desaprobado (y de allí la cursada).
* Los puntos opcionales que no hayan estado implementados para la fecha de entrega, no se podrán implementar en una "reentrega" o a futuro. El trabajo práctico no se hace en cuotas. Si hay algo para ser corregido de un punto opcional ya hecho, se puede corregir eventualmente. 
