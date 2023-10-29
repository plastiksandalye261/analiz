import streamlit as st

# Kategoriler ve alt maddeler
kategoriler = {
    "Önyargı": ["Dış Görünüş", "Sempatiklik", "Kıyafet", "Davranış", "Seyirci İlişkisi", "Ses Tonu", "Konuşma Şekli", "Agresiflik", "Kibir"],
    "Zanaat": ["Ses Kullanışı", "Tonlama", "Vurgulama", "Elini Kolu Kullanışı", "Sahne Hakimiyeti", "Seyirci İnteraktifi", "Hız", "Doğallık", "Spontanlık", "Diksiyon"],
    "Delivery": ["Jest", "Mimik", "Karakter Yaratma", "Taklit", "Mikrofon Kullanışı", "Timing", "LPM"]
}

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

def kategorileri_goster():
    for kat, alt_maddeler in kategoriler.items():
        st.write(kat)
        for madde in alt_maddeler:
            st.slider(madde, 0, 10, 0)
            st.text_input(f"{madde} için notlar", "")

    if st.button("Analiz Başla"):
        periyot_analizi()

def main():
    kategorileri_goster()

if __name__ == "__main__":
    main()
