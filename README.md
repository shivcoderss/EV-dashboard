# 🚗 Electric Vehicle Specs Dashboard (2025)

A Streamlit-based data visualization dashboard for exploring specifications of electric vehicles from various global brands.

## 📊 Features

* Filter EVs by brand
* View histograms of numeric features (e.g., range, battery capacity)
* Correlation heatmap for technical specs
* Scatter plots:

  * Battery Capacity vs Range
  * Acceleration vs Top Speed
* Boxplot: Range distribution by brand
* Bar chart: Vehicle count per brand
* Pairplot for feature exploration

## 🧰 Tech Stack

* Python
* Streamlit
* Pandas
* Seaborn
* Matplotlib

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivcoderss/ev-dashboard.git
cd ev-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## 📁 File Structure

```
ev-dashboard/
│
├── app.py                           # Streamlit application
├── electric_vehicles_spec_2025.csv.csv  # Dataset
├── README.md                        # This file
└── requirements.txt                # Python dependencies
```

## 📦 Deployment

This app is deployed on Streamlit Cloud:

**Live App URL**: [ev-dashboard on Streamlit](https://ev-dashboard-4g7u62a9ymbbjlgjj45yur.streamlit.app)

You can deploy your own version by pushing to GitHub and connecting to Streamlit Cloud.

---

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/d1dd2d41-f9a7-4cef-8ca1-7a812148d217)


---

## 📄 License

MIT License. Use freely with attribution.
