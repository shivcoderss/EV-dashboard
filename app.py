import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EV Specs Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("electric_vehicles_spec_2025.csv.csv")
    df.columns = [col.lower() for col in df.columns]
    return df

df = load_data()
st.title("🚗 Electric Vehicle Specs Dashboard (2025)")

brands = st.sidebar.multiselect("Select Brand(s):", df["brand"].dropna().unique(), default=df["brand"].dropna().unique())
filtered_df = df[df["brand"].isin(brands)]

st.subheader("📊 Dataset Preview")
st.dataframe(filtered_df.head())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
selected_col = st.selectbox("Choose a column for histogram:", numeric_cols)

fig1, ax1 = plt.subplots()
sns.histplot(filtered_df[selected_col].dropna(), kde=True, ax=ax1)
ax1.set_title(f'Distribution of {selected_col}')
st.pyplot(fig1)

st.subheader("🔗 Feature Correlation Heatmap")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax2)
st.pyplot(fig2)

if {'range_km', 'battery_capacity_kwh'}.issubset(filtered_df.columns):
    st.subheader("🔋 Battery Capacity vs. Range")

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    scatter = sns.scatterplot(data=filtered_df, x='range_km', y='battery_capacity_kwh', hue='brand', ax=ax3)

    ax3.set_xlabel('Range (km)')
    ax3.set_ylabel('Battery Capacity (kWh)')
    ax3.set_title('Battery Capacity vs. Range')

    
    ax3.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Brand", borderaxespad=0)
    st.pyplot(fig3)

if {'range_km', 'brand'}.issubset(filtered_df.columns):
    st.subheader("📦 Range Comparison by Brand")

    fig4, ax4 = plt.subplots(figsize=(16, 8)) 
    sorted_brands = filtered_df.groupby('brand')['range_km'].median().sort_values().index

    sns.boxplot(data=filtered_df, x='brand', y='range_km', order=sorted_brands, ax=ax4)

    ax4.set_xlabel("Brand")
    ax4.set_ylabel("Range (km)")
    ax4.set_title("Range Distribution by Brand")
    ax4.tick_params(axis='x', labelrotation=60) 
    st.pyplot(fig4)

if 'brand' in filtered_df.columns:
    st.subheader("📈 Vehicle Count per Brand")

    fig5, ax5 = plt.subplots(figsize=(12, 10)) 
    brand_counts = filtered_df['brand'].value_counts()

    brand_counts.plot(kind='barh', ax=ax5)
    ax5.set_xlabel("Count")
    ax5.set_ylabel("Brand")
    ax5.set_title("Number of Vehicles per Brand")

    st.pyplot(fig5)


if {'acceleration_0_100_s', 'top_speed_kmh'}.issubset(filtered_df.columns):
    st.subheader("⚡ Acceleration vs. Top Speed")

    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=filtered_df,
        x='acceleration_0_100_s',
        y='top_speed_kmh',
        hue='brand',
        ax=ax6
    )

    ax6.set_xlabel("0–100 km/h Acceleration (s)")
    ax6.set_ylabel("Top Speed (km/h)")
    ax6.set_title("Acceleration vs. Top Speed")

    
    ax6.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Brand", borderaxespad=0)
    st.pyplot(fig6)


pairplot_cols = st.multiselect("Select up to 4 columns for pairplot:", numeric_cols, default=numeric_cols[:3])
if len(pairplot_cols) >= 2:
    st.subheader("📌 Pairplot of Selected Features")
    fig7 = sns.pairplot(filtered_df[pairplot_cols].dropna())
    st.pyplot(fig7)
