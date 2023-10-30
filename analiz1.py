import streamlit as st

# Initialize the session state
if 'init' not in st.session_state:
    st.session_state.init = True
    st.session_state.current_periyot = 1
    st.session_state.periyot_data = {}


saka_turleri = ["LPM", "Aforizma Cümle", "Şiirsellik", "Şaka Türleri", "Kendini Tanıtma", "İlginç Hikaye", "Anektod", "Mantık Hatası", "Bir Şeyi Çürütme",
                "Savunma", "Tespit", "Anlar", "Teknikler", "Küfür", "Komik Kelime", "İsim", "Benzetme", "Misdirection", "Detaylar", "Done",  "Jest", "Uzun Şaka",
                "Tahmin Edilebilirlik", "Sürpriz", "Rant", "Cinsellik",  "Tarihi Konular", "Entelektüellik","Politik Konular", "Ful Evrensellik"]

periyot_data = {}
current_periyot = 1

def periyot_analizi():
    current_periyot = st.session_state.current_periyot
    st.write(f"{current_periyot}. Periyot Analizi")
    
    counts = {}
    notes = {}
    
    for saka in saka_turleri:
        # Initialize or get current count
        if saka not in st.session_state or f"{saka}_count_{current_periyot}" not in st.session_state:
            st.session_state[f"{saka}_count_{current_periyot}"] = 0
        
        # Create a button to increment the count
        if st.button(f"Increment {saka}", key=f"{saka}_button_{current_periyot}"):
            if st.session_state[f"{saka}_count_{current_periyot}"] < 10:
                st.session_state[f"{saka}_count_{current_periyot}"] += 1
        
        # Display the current count
        st.write(f"{saka} Count: {st.session_state[f'{saka}_count_{current_periyot}']}")
        
        # Add to counts dictionary
        counts[saka] = st.session_state[f"{saka}_count_{current_periyot}"]
        
        # Notes input
        notes[saka] = st.text_input(f"{saka} için notlar", "", key=f"{saka}_notes_{current_periyot}")

    if st.button("Sonraki Periyot"):
        st.session_state.periyot_data[st.session_state.current_periyot] = {
            "notes": notes,
            "counts": counts
        }
        st.session_state.current_periyot += 1
        periyot_analizi()
    elif st.button("Analizi Bitir"):
        finish_analysis()


def finish_analysis():
    for periyot, data in st.session_state.periyot_data.items():
        st.write(f"{periyot}. Periyot İstatistikleri:")
        for saka, count in data["counts"].items():
            st.write(f"{saka}: {count} kez, Not: {data['notes'][saka]}")

    if st.button("Yeniden Başla"):
        st.session_state.init = True
        st.session_state.current_periyot = 1
        st.session_state.periyot_data = {}

# Check session state to determine which function to call
if st.session_state.init:
    periyot_analizi()
else:
    finish_analysis()

