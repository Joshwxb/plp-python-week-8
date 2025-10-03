# CORD-19 Research Data Explorer

This project explores the CORD-19 dataset (`metadata.csv`) and builds a simple interactive dashboard using Streamlit.

## Features
- Load and explore COVID-19 research metadata
- Clean and preprocess data (dates, missing values)
- Analyze trends by year, journals, and keywords
- Visualize publication trends with charts and a word cloud
- Interactive Streamlit app

## Setup Guidelines 

1. Clone the repo:
   ```bash
   git clone https://github.com/
   cd plp-python-template/week8
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Use the sidebar to filter by year, journal, or keywords.
- Explore the visualizations and word cloud for insights into COVID-19 research publications.

## File

- `app.py`: Main Streamlit application
- `metadata_sample.csv`: CORD-19 metadata file (not included; download from official source)
- `requirements.txt`: Python dependencies

## Notes

- Make sure `metadata.csv` (or `metadata_sample.csv`) is in the project directory before running the app.
- For more information about CORD-19, visit the [official website](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).
