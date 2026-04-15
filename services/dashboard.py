import streamlit as st
import pandas as pd
from common.translate import paramsMapping

def render_dashboard(filepath):

    df = pd.read_excel(filepath)

    st.set_page_config(layout="wide", page_title="Aplikacja pogodowa")
    st.title("Aplikacja pogodowa")

    st.sidebar.header("Konfiguracja")
    selected_column = st.sidebar.selectbox(
        "Wybierz kolumnę do wykresu",
        ["Wilgotność", "Ciśnienie", "Prędkość Wiatru","Temperatura"]
    )


    st.sidebar.header("Konfiguracja")
    number = st.sidebar.slider("Pick a number", 0, 100)
    pets = ["Pies", "Kot", "Chomik", "Papuga"]

    pet = st.sidebar.radio("Wybierz zwierzę:", pets)

    color = st.sidebar.color_picker("Wskaż kolor:")
    date = st.sidebar.date_input("Wybierz datę:")

    file = st.sidebar.file_uploader("Wczytaj plik:")

    button = st.sidebar.button("Przycisk")

    last_row = df.iloc[-1]

    st.divider()

    st.subheader("Aktualne informacje")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        if "temp" in last_row:
            col1.metric("Temperatura", f"{last_row['temp']} °C")
    with col2:
        if "humidity" in last_row:
            col2.metric("Wilgotność", f"{last_row['humidity']} %")
    with col3:
        if "pressure" in last_row:
            col3.metric("Ciśnienie", f"{last_row['pressure']} hPa")
    with col4:
        if "wind_speed" in last_row:
            col4.metric("Wiatr", f"{last_row['wind_speed']} km/h")

    st.divider()

    st.subheader("Statystyki")

    stats_cols = st.columns(4)

    with stats_cols[0]:
        if "temp" in df.columns:
            stats_cols[0].info(
                f"Średnia temperatura: {df['temp'].mean():.2f}°C \n\n"
                f"Minimalna: {df['temp'].min():.2f}°C \n\n"
                f"Maksymalna: {df['temp'].max():.2f}°C \n\n"

            )

    with stats_cols[1]:
        if "humidity" in df.columns:
            stats_cols[1].info(
                f"Średnia ciśnienie: {df['humidity'].mean():.2f}hPa \n\n"
                f"Minimalna: {df['humidity'].min():.2f}hPa \n\n"
                f"Maksymalna: {df['humidity'].max():.2f}hPa \n\n"
            )

    with stats_cols[2]:
        if "pressure" in df.columns:
            stats_cols[2].info(
                f"Średnia ciśnienie: {df['pressure'].mean():.2f}hPa \n\n"
                f"Minimalna: {df['pressure'].min():.2f}hPa \n\n"
                f"Maksymalna: {df['pressure'].max():.2f}hPa \n\n"
            )

    with stats_cols[3]:
        if "wind_speed" in df.columns:
            stats_cols[3].info(
                f"Średnia prędkość wiatru: {df['wind_speed'].mean():.2f}km/h \n\n"
                f"Minimalna: {df['wind_speed'].min():.2f}km/h \n\n"
                f"Maksymalna: {df['wind_speed'].max():.2f}km/h \n\n"
            )

    st.divider()

    st.subheader("Wykresy")
    line_charts = st.columns(2)

    with line_charts[0]:
        if "temp" in df.columns:
            st.markdown("**Temperatura w czasie**")
            st.line_chart(
                df,
                x="timestamp",
                y=["temp", "feels_like"],
                color=["red", "blue"],
                x_label="Data",
                y_label="Temperatura",
            )

    with line_charts[1]:
        if paramsMapping(selected_column) in df.columns:
            st.markdown(f"**{selected_column} w czasie**")
            st.line_chart(
                df,
                x="timestamp",
                y=[paramsMapping(selected_column)],
                x_label="Data",
                y_label=paramsMapping(selected_column),
            )

    st.divider()
    st.subheader("Wykresy słupkowe")

    bar_charts = st.columns(2)

    with bar_charts[0]:
        if paramsMapping(selected_column) in df.columns:
            st.markdown(f"**{selected_column} w czasie**")
            st.bar_chart(
                df,
                x="timestamp",
                y=[paramsMapping(selected_column)],
                x_label="Data",
                y_label=paramsMapping(selected_column),
            )

    with bar_charts[1]:
        if paramsMapping(selected_column) in df.columns:
            st.markdown(f"**{selected_column} w czasie**")
            st.bar_chart(
                df,
                x="timestamp",
                y=[paramsMapping(selected_column)],
                x_label="Data",
                y_label=paramsMapping(selected_column),
            )


    st.divider()
    st.subheader("Tabelki")
    st.markdown("**Ostatnie 10 pomiarów**")
    st.dataframe(df.tail(10), use_container_width=True)

    st.markdown("**Opis statystyczny**")
    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe(), use_container_width=True)