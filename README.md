## Proyecto final Programación II: Análisis de 120 años de historia olímpica (1896–2016)

### Descripción
En este repositorio analizamos la evolución de los Juegos Olímpicos modernos a partir del conjunto de datos histórico de atletas y regiones olímpicas. El objetivo del trabajo es limpiar, cruzar y explorar estos registros usando Python y Pandas para entender cómo ha cambiado la participación por época, temporada, sexo, edad y características físicas, así como qué factores influyen en la obtención de medallas. 

### Objetivos
* Integrar y depurar las tablas de atletas y comités olímpicos nacionales (`athlete_events` y `noc_regions`).
* Analizar la representatividad de los datos a lo largo de la historia olímpica y el comportamiento de los valores faltantes.
* Evaluar mediante agrupaciones, tasas proporcionales y visualizaciones qué perfiles de atletas tienen mayor probabilidad de ganar medalla.
* Aplicar un flujo de trabajo colaborativo en GitHub usando ramas, Pull Requests y revisión de código entre pares.

### Integrantes y Roles
* **Juliana Mejía Fernández** – Líder de Repositorio y Procesamiento de Datos 
* **Samuel Garcia Cubides** – Líder de Análisis y Documentación 

### Instrucciones para ejecutar
1. Clona el repositorio.
2. Descarga `athlete_events.csv` y `noc_regions.csv` desde Kaggle y guárdalos en la carpeta `data/` (ver `data/README.md`).
3. Instala las librerías necesarias: `pip install pandas numpy matplotlib`.
4. Abre los notebooks de la carpeta `notebooks/` y ejecútalos en orden numérico, con Restart y Run All.


### Estructura del Proyecto
```text
taller-pandas-olimpiadas-grupo/
├── README.md               # Presentación general del proyecto
├── .gitignore              # Archivos excluidos del repositorio 
├── data/                   # Instrucciones de descarga de los CSV 
├── notebooks/              # Notebooks de Jupyter con el análisis exploratorio completo
├── src/                    # Scripts en Python (cargue_datos.py: carga y prepara los datos)
├── outputs/                # Resultados generados por el código
│   ├── tablas/             # Resúmenes y conteos en formato CSV
│   └── graficos/           # Gráficas del análisis
└── docs/                   # Informe final en PDF y evidencia 
```
