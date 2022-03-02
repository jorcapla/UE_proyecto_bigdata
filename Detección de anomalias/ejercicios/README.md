# Detección de anomalías
[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)



## Contenido

Este carpeta contiene todos los ejemplos realizados en la detección de anomalias de una máquina batidora o mixer.
La caracteristica principal de esta máquina es que trabaja de forma discontinua en intervalos de una a dos horas.

## Datos

Los datos para el estudio comprenden desde el 1 de septiembre del 2018 hasta el 01/05/2019 de las siguientes variables:

-	1H. Vibración horizontal en el rango 10-1000 Hz en velocidad de vibración (mm/s).
-	1H_G. Vibración horizontal en el rango 10-5000 Hz en aceleración (G´s).
-	1V. Vibración vertical en el rango 10-1000 Hz en velocidad de vibración (mm/s).
-	1H_G. Vibración vertical en el rango 10-5000 Hz en aceleración (G´s).
-	1C. Intensidad en fase de alimentación al motor.

>Las vibraciones en velocidad de vibración (mm/s) son el estándar de la norma (ISO10816), y dan una visión global muy buena del estado de máquina, pero no tienen en cuenta los efectos de la alta frecuencia, para ello se utiliza la aceleración (G´s).

---
## Sobre la detección de anomalías 

La detección de anomalías es una técnica utilizada para identificar patrones inusuales que no se ajustan al comportamiento esperado, llamados valores atípicos. Tiene muchas aplicaciones en el negocio, desde detección de intrusos (identificando patrones extraños en el tráfico de red que podrían indicar un ataque) hasta monitoreo del estado del sistema (detectando un tumor maligno en una exploración de MRI), y desde detección de fraude en transacciones con tarjeta de crédito hasta detección de averías en Entornos operativos.

### ¿Qué es la detección de anomalías?

Existen tres tipos de anomalías:

- **Anomalías puntuales**. Si una instancia de datos individuales puede considerarse anómala con respecto al resto de los datos (por ejemplo, compras con un gran valor de transacción)
  
- **Anomalías contextuales**, si una instancia de datos es anómala en un contexto específico, pero no de otra manera (anomalía si se produce en un momento determinado o en una determinada región. Por ejemplo, un pico grande en medio de la noche)
  
- **Anomalías colectivas**. Si una recopilación de instancias de datos relacionadas es anómala con respecto al conjunto de datos completo, pero no a valores individuales. Tienen dos variaciones.
    - Anomalias detectadas en eventos ordenados (por ejemplo, rompiendo el ritmo en ECG)
    - Anomalias detectadas en eventos no ordenados ( por ejemplo precios excesivamente altos en el precio de una habitación de hotel)

Esta documento explica qué es la detección de anomalías, las técnicas más comunes en detección de anomalías, las claves detrás de esas técnicas y concluye con una discusión sobre cómo hacer uso de esos resultados.

### Técnicas de detección de anomalías

Existen dos tipos bien diferenciados para detectar anomalías en los datos. Por una parte están los métodos estadisticos tradicionales y por otrar parte la inteligencia artificial.

Las técnicas mas comunes para la detección de anomalias son las siguientes

1. Métodos estadísticos ( Simple Statistical Methods)
   - Point Anomalies [https://www.datascience.com/blog/python-anomaly-detection]
   - Low pass filter [https://www.datascience.com/blog/python-anomaly-detection]
   - Kalman filter [http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/]
2. Machine Learning
   - Density-Based Anomaly Detection
     - K-nearest neighbor **KNN**
     - Relative density of data **LOF**
   - Markov chains and Hidden Markov chains
   - Clustering-Based Anomaly Detection 
     - K-means
   - Isolation Forest
   - Support Vector Machine-Based Anomaly Detection 
   - TimeSeries methods
   - Deep Learning RNN -->LSTMs


Antes de seleccionar el método/técnica para la detección de anomalias hay que realizarse las siguientes preguntas
- ¿Tengo datos suficientes?
- ¿Los datos siguen algún patrón que pueda apreciarse visualmente?
- ¿Los datos están categorizados entre normales y anomalos?
- ¿Tengo datos de entrenamiento?
- ¿El orden de los datos es relevante?

Las respuestas a estas preguntas nos guiarán en la técnica a utilizar tal y como muestra la imagen siguiente.

>Las técnicas de machile learning podemos subclasificarlas según la existencia de datos de entrenamiento según esta clasificación:
>- Técnicas supervisadas ( con datos de entrenamiento y clasificados)
>- Técnicas semi-supervisadas
>- Técnicas no supervisadas o Detección automática de anomalías (sin datos de entrenamiento)
>


![N|Solid](https://iwringer.files.wordpress.com/2015/11/anomelydetectionmethods.jpg)


### Comparando modelos y actuando sobre los resultados

Con la detección de anomalías, es natural pensar que el objetivo principal es detectar todas las anomalías. Sin embargo, a menudo es un error.

El mayor problema con la detección de anomalias son los falsos positivos 

Si ignora este problema, puede causar daños de varias maneras.

- **Reducir la confianza en el sistema**: cuando las personas pierden la confianza, se necesitará mucho esfuerzo para recuperar la confianza
- **Sobrecoste por reparación innecesaria** 
- **Reducir el tiempo de producción de una máquina**

Por lo tanto, debemos tratar de encontrar un equilibrio en el que intentemos detectar lo que podamos mientras mantenemos la precisión del modelo dentro de límites aceptables.

Otra parte del mismo problema es que los modelos son solo una sugerencia para la investigación, pero no evidencia para incriminar a alguien. Este es otro giro de la correlación contra la causalidad. Por lo tanto, los resultados del modelo nunca deben usarse como evidencia y el investigador debe encontrar evidencia independiente del problema (por ejemplo, fraude con tarjeta de crédito).

Debido a estas dos razones, es primordial que el investigador pueda ver la anomalía dentro del contexto para verificarla y también para encontrar evidencia de que algo está mal.

---

## Modelos implementados para la detección de anomalías ##

El primer paso a realizar en este estudio es un análisis de los datos.
Una vez realizado el estudio vamos a intentar utilizar métodos estadisticos para detecctar anomalias
- [x] Point Anomalies
   
El segundo paso, dado que no tenemos datos clasificados y el orden es importante vamos a realizar los siguientes modelos

- [X] Clustering-Based Anomaly Detection 
- [X] Isolation Forest
- [ ] RNN


Todavía no sé como voy a evaluar los modelos

---
## Referencias ##

- https://www.datascience.com/blog/python-anomaly-detection