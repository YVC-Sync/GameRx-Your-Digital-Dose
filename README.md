# GameRx: Your Digital Dose  
**Relief Through Play**

<img src="GameRx case study logo.png" alt="GameRx Logo" width="130">

GameRx explores whether video games can be recommended like mood medicine, supporting emotional relief. 
Using player review data, emotional theory, and clustering, this project builds a hybrid recommendation framework that maps games to relief pathways such as Comfort, Catharsis, Distraction, and Validation.

The goal is to build a human-centered recommendation framework that connects how people feel with the kinds of games that may support emotional relief.

---

## 🚀 Fast Facts for Busy Reviewers

- **Tool Stack:** Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn), Jupyter Notebook, NLP (NRCLex)  
- **Methods:** NLP, emotion scoring, clustering, hybrid rule-based modeling  
- **Data Source:** 6M+ Steam reviews (Kaggle) + Steam game metadata  
- **Focus:** Emotional relief, behavioral patterns, human-centered systems  

**Key Wins:**  
- Applied emotion detection to large-scale player review text  
- Built normalized emotion intensity features  
- Defined and operationalized four emotional relief categories  
- Used clustering to uncover emotional play styles across games  
- Created an app-ready recommendation dataset 

---

## 🎯 The Challenge

Many players turn to video games to cope with stress, frustration, or emotional fatigue.   
Yet most recommendation systems focus on popularity, ratings, or genre, not emotional needs.

GameRx asks a different question:

> *Can emotional patterns in player reviews be measured, modeled, and translated into meaningful game recommendations?*

---

## 🔍 Questions I Explored

- What emotions dominate different types of games?
- Can emotions expressed in reviews be grouped into meaningful relief pathways?
- Can emotional signals be mapped to relief-based play needs?
- How do we design recommendations that are supportive, not escalatory?
- How can emotional data inform recommendation logic?

---

## 🛠 Tools Used

- **Python:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn 
- **NLP:** NRCLex emotion lexicon  
- **Modeling:** Feature engineering, KMeans clustering, evaluation metrics  
- **Jupyter Notebook:** End-to-end analytical pipeline 
- **App Prototype:** Streamlit  

---

## 🔁 Workflow Summary

This project followed a structured, multi-stage pipeline:

- Cleaned and standardized raw Steam review and metadata files
- Processed player reviews using emotion lexicon mapping
- Engineered emotion and relief-based features 
- Mapped emotions to four relief categories:
  - Comfort
  - Catharsis
  - Distraction
  - Validation
- Performed clustering to identify emotional play styles
- Built an app-ready dataset for recommendations

**Final app-ready dataset:** `17_games_hybrid_app_ready.csv` 

---

## 📊 What I Found

- Emotional signals in reviews are consistent and measurable at scale 
- Distraction games show the highest emotional diversity  
- Comfort and Validation are frequently misassigned without correction  
- Review language provides stronger emotional signal than metadata alone
- Clustering revealed distinct emotional play styles that cut across genres  

---

## 🤖 Machine Learning Insight

Clustering revealed that emotional experience does not strictly follow genre boundaries.  
Games with very different mechanics can serve similar emotional roles for players.

This reinforced the decision to use a hybrid approach that combines data-driven clustering with emotional theory, resulting in more stable and human-aligned recommendations.

---

## 💡 Business & Human Impact

GameRx demonstrates how data science can be applied ethically and intentionally:

- Supports more thoughtful, emotion-aware gaming choices    
- Enables recommendation systems that prioritize wellbeing   
- Bridges behavioral science with applied machine learning  
- Centers user experience alongside technical performance  

---

## 🗂 Repository Structure

```bash
GameRx-Your-Digital-Dose/
│
├── 01 Project Context/ # Concept, research, methodology
├── 02 Data/ # Data documentation (no large files)
├── 03 Notebooks/ # Full analytical pipeline
├── 04 Visuals/ # Saved charts and figures
├── 05 Case Study/ # Final written case study
├── 06 App/ # Streamlit app prototype
│
├── LICENSE
└── README.md
```
---

## 🔗 View the Full Case Study
[🌐 www.yariselvelacanto.com/data](http://www.yariselvelacanto.com/data)

## Copyright & Use

© 2026 Yarisel Velacanto. All rights reserved.

This project is shared publicly for portfolio review only. Please do not copy, reuse, modify, redistribute, or commercially use any part of this work without written permission.
