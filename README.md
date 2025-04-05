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


 ### Relacion señal-ruido
<p>
  
La relación señal-ruido es una métrica fundamental en el procesamiento de señales, puesto que permite evaluar la calidad de una señal en presencia de ruido, esta medida  compara la potencia de la señal útil con la potencia del ruido presente en un sistema.

Se calculo el SNR de cada señal, asi mismo atraves de una función de la librería librosa y el siguiente comando librosa.load(), se identifica la frecuencia de muestreo del audio, posterior al proceso de análisis temporal y espectral (cuyas graficas desarrollaremos mas adelante) y el análisis de componentes independientes, igual a el análisis por Beamforming que permitirán asilar la señal de interés y asi calcular el SNR y comparar el desempeño de separación

![image](https://github.com/user-attachments/assets/4d15dde4-3835-419e-b3d5-2d3f4f4437f1)

**Implementación en el Código:**

`import librosa
archivo = r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab3\CedielSeñal.wav"  # Nombre del archivo
_, sr = librosa.load(archivo, sr=None)  # Carga sin modificar la frecuencia
print(f"Frecuencia de muestreo original: {sr} Hz")`


</p>

#### Frecuencia de muestreo.
<p>
Es la cantidad de muestras tomadas por unidad de tiempo, para convertir una señal análoga a digital. En audio la frecuencia de muestreo determina la precisión del audio digital.
Según el teorema de Nyquist, la frecuencia de muestreo debe ser al menos el doble de la frecuencia más alta contenida en la señal original. Dado que el oído humano puede percibir sonidos en un rango de 20 Hz a 20.000 Hz, se requiere una frecuencia de muestreo mínima de 40.000 Hz para capturar. para este laboratorio seleccionamos la frecuencia estandar de 44.1 kHz que cumple el teorema de nyquist, esta frecuencia es superior al doble de la frecuencia maxima audible de 20kHz. 
Por parte de la adquisición para el procesamiento de estas señales se realizo con una frecuencia de muestreo 48kHz, con esta información nos permite también saber que se puede capturar frecuencias de 24kHz, cumpliendo con el criterio de Nyquist para señales de audio, Ademas por tema de la cuantificación se siguió el estándar de los archivos WAV, la cual representa valores flotantes de 32 bits, lo que nos permite asegurar una buena conversión digital.

**Implementación en el Código:**

`audio1, sr1 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\CedielSeñal.wav',sr=48000)
audio2, sr2 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\lab3juanyAmb.wav',sr=48000)
ruido1, sr3 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\CedielAmb.wav',sr=48000)
ruido2, sr4 = librosa.load(r'C:\Users\Usuario\Downloads\Lab3\lab3juanyAmb.wav',sr=48000)`

El tiempo de captura como ya fue mencionado de cada señal fue de 39 a 40 segundos, por lo cual por medio de relleno de ceros (Padding) se igualo ambas señales que nos permitirá mezclar o separación sin perdidas de información. 

`longitud_max = max(len(audio1), len(audio2))
audio1 = np.pad(audio1, (0, longitud_max - len(audio1)))
audio2 = np.pad(audio2, (0, longitud_max - len(audio2)))
audio_mix = np.vstack((audio1, audio2)).T`

El calculo del SNR se calculo antes y despues de aplicar técnicas de procesamiento, como lo son (ICA) Y (BEAMFORMING), con el propósito de evaluar las voces y mejorar la calidad tras la reducción de interferencias y ruido.

`# Calcular la relación señal-ruido (SNR)
def snr_calculo(señal, ruido):
    pseñal = np.mean(señal ** 2)
    pruido = np.mean(ruido ** 2)
    snr = 10 * np.log10(pseñal / pruido)
    return snr`
`snr1 = snr_calculo(audio1, ruido1)
snr2 = snr_calculo(audio2, ruido2)
print(f"SNR Cediel: {snr1} dB")
print(f"SNR Juany: {snr2} dB")`

`# Asegurar que ambas señales de ruido tengan la misma longitud
longitud_max_ruido = max(len(ruido1), len(ruido2))
ruido1 = np.pad(ruido1, (0, longitud_max_ruido - len(ruido1)))
ruido2 = np.pad(ruido2, (0, longitud_max_ruido - len(ruido2)))
señal_suma = ruido1 + ruido2`

`# Calcular SNR final
SNR_FINAL_BEAM = snr_calculo(beamformed_signal, señal_suma)
SNR_FINAL_ICA = snr_calculo(señal_ica, señal_suma)`

</p>

### Filtrado de señales.
#### Ventanas
Son funciones matemáticas que se aplican cuando la señal no tenga un numero entero en un intervalo de adquisición, se encargan de reducir la amplitud de discontinuidades que distorcionen la señal.

- Ventana Hanning
Reduce al minimo las discontinuidades, es útil para minimizar la interferencia entre frecuencias cercanas, tiene un equilibrio entre resolución espectral y bajo nivel de fuga espectral, su función alcanza cero en ambos extremos.

- Ventana de Hamming
Es muy parecida a la ventana de Hanning, es útil para mantener la amplitud de la señal sin distorcionarla. Sus extremos no llegan a cero a diferencia de las ventanas hanning.  

##### Contraccion 1
![image](https://github.com/user-attachments/assets/605de27f-a096-4832-8dd0-7c0346e781e4)
![image](https://github.com/user-attachments/assets/06975a96-76ac-40f1-b3f4-f6bc82463f11)
![image](https://github.com/user-attachments/assets/dba93a8d-8cbf-4f48-b4d9-2c8c886cb7a8)
![image](https://github.com/user-attachments/assets/a78d4ebb-04ce-4239-babf-5f0734e1fd60)
![image](https://github.com/user-attachments/assets/8d540040-d21b-4266-acd4-93f28493664c)

##### Contraccion 2
![image](https://github.com/user-attachments/assets/f6c953b6-8b34-49dc-a44f-622ee05b09f5)
![image](https://github.com/user-attachments/assets/a44cf049-7857-4c21-a0f3-01bafbd0974d)
![image](https://github.com/user-attachments/assets/706e8189-3e42-4b5b-a331-c254ab071458)
![image](https://github.com/user-attachments/assets/9587ca2f-3f8f-4d70-b6a2-8490698d766d)
![image](https://github.com/user-attachments/assets/3b68146e-bc34-4103-b8b0-202bf22dc34a)

##### Contraccion 36
![image](https://github.com/user-attachments/assets/07fb4bdf-8133-4866-bbe6-03563804f42d)
![image](https://github.com/user-attachments/assets/9a21204d-1663-4e8d-8664-589ebe3c0628)
![image](https://github.com/user-attachments/assets/645d5b98-eaf3-453b-a863-23a0b6ea84d7)
![image](https://github.com/user-attachments/assets/ea5b4195-da2a-442b-ab03-1d6e7ae36f76)

##### Contraccion 37
![image](https://github.com/user-attachments/assets/480cf39e-13ce-43ae-92ed-e63cf7006eb7)
![image](https://github.com/user-attachments/assets/2cd3eeb3-7057-4847-8eab-a0fd78222a0c)
![image](https://github.com/user-attachments/assets/39ad9a1a-8205-4254-95c4-5476e5416671)
![image](https://github.com/user-attachments/assets/742eece3-d46a-4cbf-9e39-dcebc2a2a76c)










#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.
</p>
    
#### Transformada rapida de Fourier.

<P>
Esta transformación es una herramienta crucial para analizar y manipular el contenido espectral del audio, esto es fundamental para aplicaciones como la separación de fuentes.
Aplicación. La Transformada Rápida de Fourier (FFT) procesa una señal de audio en el dominio del tiempo, donde se representa la amplitud de la onda sonora a lo largo del tiempo, y la transforma en el dominio de la frecuencia. Esto permite visualizar la intensidad de cada componente de frecuencia presente en la señal original, es decir, identificar qué frecuencias conforman el sonido. En el caso del laboratorio, donde se analizan dos fuentes con diferentes timbres de voz, la FFT permite reconocer los rangos de frecuencia característicos de cada tipo de voz, donde una voz aguda ocuparia un rango de frecuencia alto, mientras que una voz gruesa ocuparia un rango de frecuencias bajas. 
</p>

#### Transformada de Fourier.
<P>
Una transformacion es una operacion que convierte una señal desde un dominio a otro dominio, la transformada de fourier convierte una señal del dominio del tiempo hacie el dominio de la frecuencia. Lo cual permite analizar las señales en dominios alternativos lo cual permite identificar las caracteristicas como frecuencias.
</p>

![image](https://github.com/user-attachments/assets/e99929ac-96c2-49d6-a698-49534e1e54b7)
![image](https://github.com/user-attachments/assets/88e9aaf2-18df-4590-8c21-bdc98815744e)

![image](https://github.com/user-attachments/assets/654d9a8a-8856-4f38-9b46-acaa4eee6157)
![image](https://github.com/user-attachments/assets/ee5c9486-1435-4d9e-8af1-fdb47ac1f634)

![image](https://github.com/user-attachments/assets/ecf733fa-216f-441c-8285-62baba6ab65c)
![image](https://github.com/user-attachments/assets/8a446bea-2efc-49e2-a544-22376ce016fd)

![image](https://github.com/user-attachments/assets/9c2faa2f-9f10-4754-b91a-e56a0c52c90f)
![image](https://github.com/user-attachments/assets/a4ee11d4-d5ab-4174-bce8-526caeb83dd9)









#### Densidad espectral.

Mide la distribucion de energia de la señal en funcion de la frecuencia. se espera que nos muestre la contribucion de mas frecuencias en la señal.



observando la PSD podemos interpretar que la señal Beamforming conserva más energía en altas frecuencias lo que podemos interpretar como una menor pérdida de información.

    
</p>



### Analisis temporal y frecuencial de las señales.

<p>
  
#### Dominio del tiempo.
- Las señales presentan variaciones de amplitud a lo largo del tiempo, mostrando características propias de cada fuente de audio.
- La señal de Juany tiene mayor variabilidad en amplitud en comparación con la de Cediel, lo que podría indicar diferencias en la 
 intensidad del sonido o en la presencia de ruido.
- En las muestras se observan fluctuaciones, lo que indica la influencia de interferencias o ruido ambiental.

#### Dominio de la frecuencia.
- Se utilizaron escalas lineales y logarítmicas, para representar el espectro de las señales. 
- En el espectro lineal, se identifican picos dominantes en bajas frecuencias, lo que muestra la mayor parte de la energía concentrada en componentes graves.
- El espectro logarítmico se visualiza las diferencias en niveles de energía en distintas bandas de frecuencia, donde se destaca la presencia de ruido en altas frecuencias.

![image](https://github.com/user-attachments/assets/3aea22ea-760e-4564-af04-aaf41beb1e90)

![image](https://github.com/user-attachments/assets/eddca05d-8318-43b9-8736-378e49e10859)

#### Dominio del tiempo.
- Las señales iniciales muestran variaciones en su amplitud, influenciadas por el ruido presente.
- La señal después de beamforming evidencia una reducción del ruido, al mejorar la alineación de las fuentes de interés.
- La señal tras ICA logra una separación efectiva de componentes, reduciendo aún más la interferencia y resaltando patrones más claros.

#### Dominio de la frecuencia.
- En el espectro lineal, tanto la señal de beamforming como la de ICA tienen componentes de baja frecuencia.
- En el espectro logarítmico, ICA muestra una distribución más uniforme en altas frecuencias, mostrando una mejor preservación del contenido espetral.
- Beamforming atenuó algunas frecuencias,logrando una señal más enfocada, pero ICA obtuvo una mayor mejora en la SNR.

![image](https://github.com/user-attachments/assets/defc5ea7-9826-4d82-96ee-2a34de3196b7)

![image](https://github.com/user-attachments/assets/662612e4-d1bb-4456-9d5b-7daf0283e43a)


</p>

### Análisis de resultados
<p>
Para el análisis de los resultados proporcionados, analizamos los valores de SNR respecto a los originales, los cuales fueron SNR de Cediel: 13.30 dB, lo cual nos habla que tiene una relación señal/ruido moderada, es decir que presenta ruido, sin embargo la señal es reconocible, SNR de Juany: 20.97 dB, esta tiene mejor calidad en comparación la de Cediel, ya que su SNR es mayor, indica que la señal es clara y el ruido no posee un impacto importante, la SNR FINAL después de Beamforming: 10.22 dB esto nos quiere decir que este método no mejoro la señal sino que empeoro, se atribuye a alguna interferencia de los micrófonos, la técnica no fue adecuada respecto a la distribución espacial de las fuentes de sonido ya que ambos celulares tuvieron la misma orientación y no había diferencia entre distancia del colaborador.
Ademas por parte del análisis de las graficas de beaforming  se observan variaciones en la amplitud, con algunos picos pronunciados, la señal parece haber sido procesada, probablemente mejorando la relación señal-ruido pero no lo suficiente ya que se percibe una especie de eco en el audio final.
  
![image](https://github.com/user-attachments/assets/d8645396-2185-4a2c-aea5-a8eda78f764b)

La SNR FINAL después de ICA: 28.53 dB, Esta mejoro significativamente la relación señal / ruido, nos indica que la separación fue buena y la señal resultante es mucho mas limpia que la original, Tambien podemos inferir que esta técnica fue mejor que la técnica de beaforming, separando correctamente las fuentes.

![image](https://github.com/user-attachments/assets/71e2859d-bbc0-4fc9-899b-18eca6654c47)

cuyos resultados se puede evidenciar en los audios finales.

"C:\Users\Usuario\Downloads\Lab3JJ\señal_beamformed.wav"
"C:\Users\Usuario\Downloads\Lab3JJ\señal_ica.wav"
  
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
- import soundfile as sf
- from colorama import Fore, init
- import shutil
- from sklearn.descomposition import
- FastICA
  
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Estructura del proyecto

- tfourier(): Transformada de fourier.
- 01.dat y 01.hea: Archivos de datos de la señal EMG.
- sklearn.decomposition.FastICA: separa las fuentes de audio mezcladas.  
- numpy: permite realizar operaciones matemáticas eficientes en matrices y arreglos.
- matplotlib: biblioteca estándar para crear visualizaciones.
- scipy: funciones para el diseño y aplicación de filtros.
- pyroomacoustics.Beamformer: enfoca la captura de audio en una direccion especifica. 


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

