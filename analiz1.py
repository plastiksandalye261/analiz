import streamlit as st

# Kategoriler ve alt maddeler


saka_turleri = ["LPM", "Aforizma Cümle", "Şiirsellik", "Şaka Türleri", "Kendini Tanıtma", "İlginç Hikaye", "Anektod", "Mantık Hatası", "Bir Şeyi Çürütme",
                "Savunma", "Tespit", "Anlar", "Teknikler", "Küfür", "Komik Kelime", "İsim", "Benzetme", "Misdirection", "Detaylar", "Done",  "Jest", "Uzun Şaka",
                "Tahmin Edilebilirlik", "Sürpriz", "Rant", "Cinsellik",  "Tarihi Konular", "Entelektüellik","Politik Konular", "Ful Evrensellik"]

periyot_data = {}
current_periyot = 1

def periyot_analizi():
    global current_periyot, periyot_data
    
    st.write(f"{current_periyot}. Periyot Analizi")
    
    counts = {saka: st.slider(saka, 0, 10, 0) for saka in saka_turleri}
    notes = {saka: st.text_input(f"{saka} için notlar", "") for saka in saka_turleri}

    if st.button("Sonraki Periyot"):
        periyot_data[current_periyot] = {
            "notes": notes,
            "counts": counts
        }
        current_periyot += 1
        periyot_analizi()

    elif st.button("Analizi Bitir"):
        finish_analysis()

def finish_analysis():
    global periyot_data

    for periyot, data in periyot_data.items():
        st.write(f"{periyot}. Periyot İstatistikleri:")
        for saka, count in data["counts"].items():
            st.write(f"{saka}: {count} kez, Not: {data['notes'][saka]}")

    if st.button("Yeniden Başla"):
        kategorileri_goster()


