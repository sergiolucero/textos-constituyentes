![image](https://user-images.githubusercontent.com/7134649/118342213-62f05380-b4f0-11eb-800b-365e7183820a.png)

# textos-constituyentes
propuestas electorales de los candidatos a constituyentes, Chile 2021

Programas descargados desde https://elecciones2021.servel.cl/informacion-general/


### Metodología/Programación
Inicialmente, bastaba con utilizar beautifulsoup + fitz en Python para descargar los archivos en formato PDF y extraer sus textos. Luego notamos que venían muchos vacíos, por corresponder a PDF escaneados (como el notable caso de una candidata del distrito 15 que subió su diploma). Para resolver este problema, recurrimos al servicio Transcribe de Amazon Cloud (con la librería boto3).
