import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd


def check_password():
    # Sprawdza, czy hasło podane przez użytkownika zgadza się z tym w Secrets
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct"):
        return True

    st.text_input("Podaj hasło dostępowe", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state:
        st.error("😕 Hasło nieprawidłowe")
    return False

if check_password():
    st.success("Zalogowano pomyślnie!")
    st.write("Witaj w zabezpieczonej aplikacji!")
    # Tutaj Twój kod dashboardu...


    st.title("Uniwersalny czytnik plików")

    # file_uploader z ograniczonymi rozszerzeniami
    uploaded_file = st.sidebar.file_uploader(
        "Wybierz plik (XLSX, CSV lub XML)",
        type=["xlsx", "csv", "xml"]
    )

    if uploaded_file is not None:
        # Pobieramy nazwę pliku, aby sprawdzić rozszerzenie
        file_name = uploaded_file.name
        st.info(f"Wczytano plik: {file_name}")

        try:
            # Logika rozpoznawania rozszerzenia
            if file_name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                st.success("Rozpoznano format CSV")

            elif file_name.endswith('.xlsx'):
                # Wymaga biblioteki: pip install openpyxl
                df = pd.read_excel(uploaded_file)
                st.success("Rozpoznano format Excel (XLSX)")

            elif file_name.endswith('.xml'):
                df = pd.read_xml(uploaded_file)
                st.success("Rozpoznano format XML")

            # Wyświetlenie danych
            st.write("Podgląd danych:")
            st.dataframe(df)

            # Prosta statystyka dla zachęty
            st.metric("Liczba wierszy", len(df))

        except Exception as e:
            st.error(f"Błąd podczas wczytywania pliku: {e}")
    else:
        st.warning("Czekam na plik...")

st.divider()