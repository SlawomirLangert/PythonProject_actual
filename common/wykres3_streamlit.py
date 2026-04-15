import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Miesiąc": ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec"],
    "Sprzedaż": [1200, 1500, 1700, 1600, 2100, 2300],
    "Koszty": [800, 900, 1000, 950, 1200, 1300],
})

df["Zysk"] = df["Sprzedaż"] - df["Koszty"]

st.set_page_config(
    page_title="Aplikacja finansowa",
    layout="wide",
)

# Tytuł i opis
st.title("Aplikacja finansowa")
st.write("Zaawansowany program dla księgowości")

# Panel boczny
st.sidebar.header("Opcje")
show_table = st.sidebar.checkbox("Pokaż tabelę z danymi", value=True)
selected_column = st.sidebar.selectbox(
    "Wybierz kolumnę do wykresu",
    ["Sprzedaż","Koszty","Zysk"]
)
uploaded_file = st.sidebar.file_uploader("Upload your file", type=["xlsx","csv"])

# Kafelki
col1, col2, col3 = st.columns(3)
with col1:
    col1_value = df["Sprzedaż"].sum()
    st.metric("Sprzedaż", f"{col1_value} zł")
with col2:
    col2_value = df["Koszty"].sum()
    st.metric("Koszty", f"{col2_value} zł")
with col3:
    col3_value = df["Zysk"].sum()
    st.metric("Zysk", f"{col3_value} zł")

# Wykres liniowy
st.subheader("Wykres liniowy")
st.write("Wybierz z opcji po lewej stronie ekranu")
st.line_chart(df, x="Miesiąc", y=selected_column)

# Wykres słupkowy
st.subheader("Wykres słupkowy")
st.bar_chart(df, x="Miesiąc", y=["Sprzedaż","Koszty"])

# Wykres obszarowy
st.subheader("Wykres area")
st.area_chart(df,x="Miesiąc", y=["Sprzedaż",selected_column])

# Tabelka
if show_table:
    st.subheader("Tabela danych")
    st.dataframe(df, use_container_width=True)


# Dane z wgranego pliku

if uploaded_file is not None:
    try:
        uploaded_df = pd.read_excel(uploaded_file)
        st.success("Udało się wgrać plik")

        st.subheader("Podgląd danych")
        st.dataframe(uploaded_df, use_container_width=True)
    except Exception as e:
        st.error("Wystąpił błąd")
else:
    st.info("Wgraj swój pierwszy plik")