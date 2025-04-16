import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta
import os
import shutil

docs_dir = os.path.join(os.getcwd(), 'docs')
os.makedirs(docs_dir, exist_ok=True)

# Also keep figures directory for backward compatibility
figures_dir = os.path.join(os.getcwd(), 'figures')
os.makedirs(figures_dir, exist_ok=True)

dates = [datetime.now() - timedelta(days=i) for i in range(90)]
dates.reverse()

np.random.seed(42)
dust = np.random.random(90) * 8
efficiency = 100 - dust * 5 + np.random.normal(0, 5, 90)  

df = pd.DataFrame({
    'Date': dates,
    'Efficiency': efficiency,
    'Dust': dust
})

def create_plots():
    scatter_fig = px.scatter(
        df, 
        x='Dust', 
        y='Efficiency',
        title='Solar Panel Efficiency vs Dust Accumulation',
        labels={'Dust': 'Dust Accumulation (g/m²)', 'Efficiency': 'Panel Efficiency (%)'},
        template='plotly_dark'
    )
    
    scatter_fig.update_layout(
        width=900,
        height=500,
        xaxis_title='Dust Accumulation (g/m²)',
        yaxis_title='Panel Efficiency (%)',
    )
    
    time_fig = px.line(
        df,
        x='Date',
        y=['Efficiency', 'Dust'],
        title='Efficiency and Dust Over Time',
        labels={'value': 'Value', 'variable': 'Metric'},
        template='plotly_dark'
    )
    
    time_fig.update_layout(
        width=1000,
        height=600,
        xaxis_title='Date',
        yaxis_title='Value',
        legend_title='Metric'
    )
    
    scatter_file = os.path.join(figures_dir, 'dust_efficiency.html')
    time_file = os.path.join(figures_dir, 'time_series.html')
    scatter_fig.write_html(scatter_file)
    time_fig.write_html(time_file)
    
    docs_figures_dir = os.path.join(docs_dir, 'figures')
    os.makedirs(docs_figures_dir, exist_ok=True)
    scatter_fig.write_html(os.path.join(docs_figures_dir, 'dust_efficiency.html'))
    time_fig.write_html(os.path.join(docs_figures_dir, 'time_series.html'))
    
    if os.path.exists('index.html'):
        shutil.copy('index.html', os.path.join(docs_dir, 'index.html'))
    
    print(f"Visualizations created in:")
    print(f"  - {figures_dir}")
    print(f"  - {docs_figures_dir} (for GitHub Pages)")
    print("\nFiles generated:")
    print(f"  - dust_efficiency.html")
    print(f"  - time_series.html")

if __name__ == "__main__":
    create_plots()