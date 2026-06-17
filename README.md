<div align="center">

```
▀█▀ █▀▀ █▀▀ █░█   ░░█ █▀█ █▄▄ █▀   █▀ █▀█ █▀█ █ █▄░█
░█░ ██▄ █▄▄ █▀█   █▄█ █▄█ █▄█ ▄█   ▄█ █▀▀ █▀█ █ █░▀█
```

### 📊 Mercado Laboral Tech
#### ETL Pipeline · Dashboard Interactivo · Datos Abiertos

![Python](https://img.shields.io/badge/Python-3.13-ff6b35?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-ETL-ff9a3c?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-ff4b6e?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20construcción-ff6b35?style=for-the-badge)

</div>

---

## 🌆 ¿De qué va esto?

Pipeline ETL completo que extrae, transforma y carga datos del mercado laboral tech a nivel internacional, para responder preguntas como:

- 🔥 ¿Qué roles tech están mejor pagados en Europa?
- 📡 ¿Ha crecido el trabajo remoto en los últimos años?
- 🎯 ¿Qué nivel de experiencia tiene más demanda?
- 📈 ¿Cómo han evolucionado los salarios desde 2020?

> 🔎 **Nota metodológica:** este proyecto evaluó inicialmente cruzar estos datos con estadísticas oficiales del mercado laboral español (SEPE), pero la fuente abierta disponible solo desagrega por sector macro (Agricultura/Industria/Construcción/Servicios), sin granularidad suficiente para aislar el sector tech. Se descartó esa integración para no forzar conclusiones poco rigurosas — documentado en `notebooks/02_sepe_eda.ipynb`.

---

## ⚡ Stack

| Capa | Tecnología |
|------|-----------|
| **Extracción** | Python · pandas |
| **Transformación** | pandas · numpy |
| **Visualización** | matplotlib · seaborn |
| **Dashboard** | Streamlit |
| **Entorno** | venv |

---

## 🗂️ Fuente de datos

| Fuente | Descripción |
|--------|-------------|
| [Jobs in Data – Kaggle](https://www.kaggle.com/datasets/hummaamqaasim/jobs-in-data) | 9.355 registros de empleos tech internacionales (2020-2023) |

---

## 🏗️ Estructura del proyecto

```
tech-jobs-spain-analysis/
├── 📂 data/
│   ├── raw/               ← datasets originales sin tocar
│   └── processed/         ← datos limpios listos para análisis
├── 📓 notebooks/
│   ├── 01_eda.ipynb       ← exploración inicial
│   └── 02_sepe_eda.ipynb  ← fuente evaluada y descartada (ver nota metodológica)
├── ⚙️ src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── 📊 dashboard/
│   └── app.py             ← Streamlit app
└── requirements.txt
```

---

## 🚀 Cómo ejecutarlo

```bash
# 1. Clona el repo
git clone https://github.com/OnisaDev/tech-jobs-spain-analysis.git
cd tech-jobs-spain-analysis

# 2. Activa el entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Lanza el dashboard
streamlit run dashboard/app.py
```

---

## 📈 Insights principales

> 🔄 *En construcción — se actualizará al finalizar el análisis*

---

## 👾 Autora

<div align="center">

**Mari · OnisaDev**
*DAM Graduate · Data & Backend · Málaga*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conecta-ff6b35?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mari-c-pastor-torres/)
[![GitHub](https://img.shields.io/badge/GitHub-OnisaDev-ff9a3c?style=for-the-badge&logo=github&logoColor=white)](https://github.com/OnisaDev)

</div>

---

<div align="center">
<sub>Construido con muchas horas de pandas</sub>
</div>
