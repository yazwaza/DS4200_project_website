# DS4200 Project Website

This repository contains our final DS4200 project website on pulmonary disease risk factors.

## Project topic
Our project looks at how health indicators, lifestyle-related factors, and symptoms relate to pulmonary disease risk. Using a synthetic lung cancer risk dataset, we built a small visualization system to show which indicators stand out most clearly, how disease outcomes differ across risk factors, and what broader patient profiles look like.

## Files included
This repo includes:
- `index.html` for the introduction, data overview, and references
- `visualizations.html` for the main visualization page
- visualization files:
  - `top_indicators_chart.html`
  - `viz_stacked_bar.html`
  - `viz_heatmap.html`
  - `viz_scatter.html`
  - `viz_radar.html`
- Python files used for analysis / chart generation:
  - `lung_cancer_analysis.py`
  - `leo_visualization.py`
- data files used in the project:
  - `cleaned_lung_cancer_data.csv`
  - `lung_cancer_prediction.csv`

## Visualization design notes
The visualizations were designed to move from broad overview to more detailed comparison:
1. an overview of which indicators are most associated with pulmonary disease
2. a comparison of disease outcomes across selected risk factors
3. a heatmap showing prevalence of symptom and indicator patterns across age groups
4. a scatter plot comparing age and oxygen saturation by disease status
5. a radar chart comparing broader patient profiles between disease-positive and disease-negative groups

We used different chart types on purpose so the figures would not feel repetitive and so each figure could support a different task. Bar charts support ranking and comparison, the heatmap supports structured prevalence comparison, the scatter plot supports relationship analysis, and the radar chart gives a broader profile view. We also revised several labels and framing choices to better separate risk factors from symptoms and to make the site more consistent overall.

## Interaction notes
The project includes multiple interactive features, mainly hover tooltips and dropdown filtering. These were used to make the charts easier to explore without overcrowding the page.

## Limitations
This dataset is synthetic, so the findings should be treated as patterns in the data rather than clinical proof. The goal of the project is to communicate relationships clearly and thoughtfully, not to make medical claims.

## Website link
Published website link:
(https://yazwaza.github.io/DS4200_project_website/visualizations.html)
