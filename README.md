# Laboratorio 4 Procesamiento digital de señales
## Señales Electromiograficas (EMG).
### Descripcion 
<p>
En este proyecto se estudia la fatiga muscular por medio del análisis espectral de señales electromiograficas(EMG). Captando la actividad eléctrica de los musculos a través del procesamiento aplicando el filtrado de señales continuas, con el fin de evaluar la variación de la frecuencia mediante se alcanza la fatiga.
</p>

### Electromiografia
Es una prueba médica que permite evaluar la salud de los músculos y los nervios. Esta técnica consiste en registrar la actividad eléctrica que genera los músculos, tanto en reposo como durante la contracción. Para desarrollar esta tecnica es necesario tener en cuenta factores como la preparacion del sujeto, un buen protocolo de preparacion minimiza el ruido e interferencias de la señal para garantizar la calidad de datos obtenidos.

![image](https://github.com/user-attachments/assets/a1f4a287-2691-41e6-bdbe-c122a7b21ca3)



### Sistema de adquisicion de datos (DAQ)
Es un conjunto de componentes que permite medir un fenomeno electrico o fisico, incluye sensores, convertidores analogo-digitales. Mide señales fisicas del mundo real y las convierte en datos digitales para su analisis. Este sistema es fundamental para capturar la actividad electrica del musculo en tiempo real, utilizando su capacidad para digitalizar las señales analogicas que vienen de los electrodos. garantizando que los datos sean confiables.

### Filtrado de señales.
#### Ventanas
Son funciones matemáticas que se aplican cuando la señal no tenga un numero entero en un intervalo de adquisición, se encargan de reducir la amplitud de discontinuidades que distorcionen la señal.

- Ventana Hanning
Reduce al minimo las discontinuidades, es útil para minimizar la interferencia entre frecuencias cercanas, tiene un equilibrio entre resolución espectral y bajo nivel de fuga espectral, su función alcanza cero en ambos extremos.

- Ventana de Hamming
Es muy parecida a la ventana de Hanning, es útil para mantener la amplitud de la señal sin distorcionarla. Sus extremos no llegan a cero a diferencia de las ventanas hanning.

En esta practica utilizamos ambas ventanas, pudimos observar la consistencia entre ambas ventanas, especificamente en las frecuencias de ambos metodos, la diferencia entre ambos es menor a 1Hz. Sin embargo la ventana Hamming mostro valores mas altos en la contraccion 1, evidenciando su mejor resolucion ante altas frecuencias.

##### Contraccion 1
![image](https://github.com/user-attachments/assets/605de27f-a096-4832-8dd0-7c0346e781e4)
![image](https://github.com/user-attachments/assets/06975a96-76ac-40f1-b3f4-f6bc82463f11)
![image](https://github.com/user-attachments/assets/a78d4ebb-04ce-4239-babf-5f0734e1fd60)


##### Contraccion 2
![image](https://github.com/user-attachments/assets/f6c953b6-8b34-49dc-a44f-622ee05b09f5)
![image](https://github.com/user-attachments/assets/a44cf049-7857-4c21-a0f3-01bafbd0974d)
![image](https://github.com/user-attachments/assets/9587ca2f-3f8f-4d70-b6a2-8490698d766d)

En las Contracciones 1 y 2 se evidencian frecuencias de 98HZ a 101Hz esto nos enseña una activacion muscular vigorosa, lo cual es comun en contracciones iniciales por medio de fibras rapidas tipo 2.  

##### Contraccion 36
![image](https://github.com/user-attachments/assets/07fb4bdf-8133-4866-bbe6-03563804f42d)
![image](https://github.com/user-attachments/assets/9a21204d-1663-4e8d-8664-589ebe3c0628)
![image](https://github.com/user-attachments/assets/645d5b98-eaf3-453b-a863-23a0b6ea84d7)


##### Contraccion 37
![image](https://github.com/user-attachments/assets/480cf39e-13ce-43ae-92ed-e63cf7006eb7)
![image](https://github.com/user-attachments/assets/2cd3eeb3-7057-4847-8eab-a0fd78222a0c)
![image](https://github.com/user-attachments/assets/39ad9a1a-8205-4254-95c4-5476e5416671)
![image](https://github.com/user-attachments/assets/742eece3-d46a-4cbf-9e39-dcebc2a2a76c)

En las contracciones 36 y 37 podemos observar frecuencias bajas menores a 30Hz indicando una fatiga muscular avanzada donde claramente se evidencia la actividad de las fibras lentas tipo 1.
</p>
    
#### Transformada rapida de Fourier.

<P>
Esta transformación es una herramienta crucial para analizar y manipular el contenido espectral del audio, esto es fundamental para aplicaciones como la separación de fuentes.
Aplicación. La Transformada Rápida de Fourier (FFT) procesa una señal de audio en el dominio del tiempo, donde se representa la amplitud de la onda sonora a lo largo del tiempo, y la transforma en el dominio de la frecuencia. Esto permite visualizar la intensidad de cada componente de frecuencia presente en la señal original, es decir, identificar qué frecuencias conforman el sonido. En el caso del laboratorio, donde se analizan dos fuentes con diferentes timbres de voz, la FFT permite reconocer los rangos de frecuencia característicos de cada tipo de voz, donde una voz aguda ocuparia un rango de frecuencia alto, mientras que una voz gruesa ocuparia un rango de frecuencias bajas. 
</p>

#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.


![image](https://github.com/user-attachments/assets/e99929ac-96c2-49d6-a698-49534e1e54b7)
![image](https://github.com/user-attachments/assets/88e9aaf2-18df-4590-8c21-bdc98815744e)

![image](https://github.com/user-attachments/assets/654d9a8a-8856-4f38-9b46-acaa4eee6157)
![image](https://github.com/user-attachments/assets/ee5c9486-1435-4d9e-8af1-fdb47ac1f634)

![image](https://github.com/user-attachments/assets/ecf733fa-216f-441c-8285-62baba6ab65c)
![image](https://github.com/user-attachments/assets/8a446bea-2efc-49e2-a544-22376ce016fd)

![image](https://github.com/user-attachments/assets/664a0529-c497-4751-be44-00c36b50ba20)
![image](https://github.com/user-attachments/assets/75da7548-4a08-4ae2-9ca9-60fbe488d075)

Podemos observar para la contraccion 1 y 37 de la transformada de furier en la ventana Hamming diferencias clave como la amplitud de la frecuencia, para la contraccion 1 la amplitud del pico principal es mayor a la amplitud de la contraccion 37, 220 es la amplitud en la contraccion 1 y 80 en la 37. Esto nos indica que la contraccion inicial tiene mayor potencia en la frecuencia dominante, Mientras que en la contraccion final la potencia ha disminuido significativamente lo que evidencia los indicios de fatiga muscular. Se obserba que mediante el musculo se fatiga la señal se vuelve mas dispersa en los espectros de potencia.

Si comparamos las ventanas hamming y hanning para las mismas contracciones se evidencia que la ventana Hamming mantiene mejor la energia del pico. Mientras que la ventana Hanning reduce la contamincion espectral. FFT con Hann tiene un pico principal de 75, es mas limpia y con menos ruido fuera del pico, FFT con Hamming tiene el pico ligeramente mayor (80) y tiene mayor presencia de los lobulos laterales.

</p>


### Analisis estadisticos.
<p>
 Por medio de este analisis validaremos los hallasgos fisiologicos, evidenciando que la disminucion de la frecuencia no sea aleatorea, sino que nos muestre su asociacion con la fatiga.
 
![image](https://github.com/user-attachments/assets/6e47d9f0-39ad-4e1a-994f-d8f2018011a9)

En la imagen podemos observar los resultados de un analisis de fatiga muscular basado en una frecuencia dominante, no aprobamos la hipotesis nula debido a la diferencia significativa entre frecuencias iniciales y frecuencias finales, lo que podria evidenciar la presencia de una fatiga muscular puesto a que la frecuencia dominante disminuye mediante aumenta el tiempo, reflejando los cambios en la conduccion neuromuscular y en la unidad motora.

</p>

### Análisis de resultados
<p>
Para el análisis de los resultados proporcionados, podemos evidenciar que la frecuencia de oscilacion es mayor en la contraccion 1 mostrando un patron de oscilaciones densas y uniformes, indicando que el musculo genera impulsos electricos con alta frecuencia, mientras que en la contraccion 37 la frecuencia se reduce de forma considerable, las oscilaciones son irregulares y menos frecuentes, lo que podriamos interpretar como una fatiga muscular donde lla unidad motora disminuye su tasa de disparo y coordinacion.
</p>

### Requisitos
<p>

  - Electrodos de superficie para EMG.
  - Sistema de adquisición de datos (DAQ).
  - Software de análisis (Python, NI-DAQmx).
  - Computador con acceso a internet.
    
Para ejecutar el código, es necesario instalar Python e importar las siguientes librerías:

- import librosa
- import numpy as np
- import matplotlib,pyplot as plt
- from sklearn.descomposition import
- iport scipy
  
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Estructura del proyecto

- tfourier(): Transformada de fourier.
- numpy: permite realizar operaciones matemáticas eficientes en matrices y arreglos.
- matplotlib: biblioteca estándar para crear visualizaciones.
- scipy: funciones para el diseño y aplicación de filtros.


### Ejecución

- Asegúrate de que los archivos de datos están en la misma carpeta que los scripts.
-	Ejecuta Lab4.py o LAB4final.py para analizar la señal:
- python Lab4.py
  


### Bibliografia

- Heras Rodríguez, MDL (2024). La transformada rápida de Fourier: fundamentos y aplicaciones (Tesis de licenciatura).
- Di Persia, LE (2017). Separación ciega de fuentes sonoras: revisión histórica y desarrollos recientes.
- González, J., Forero, E., Jiménez, F. y Mariño, I. (2013). Atenuación de rizado en la densidad espectral de potencia calculada en una señal de ritmo cardíaco. Matemática , 11 (2), 22-26.


### Licencia

Este proyecto es de uso académico y educativo.

### Contacto
<p>
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
</p>

- **Nombre:** [Juan David Cediel Farfan][Juan Yael Barriga Roa]
- **Email:** [est.juand.cediel@unimilitar.edu.co][est.juan.barriga@unimilitar.edu.co]
- **GitHub:** [David05Cediel][JuanYBR]

