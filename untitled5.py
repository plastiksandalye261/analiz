# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1owVJZ9BIYRxOq6E9_RolXOK29Af2pmSa
"""

import ipywidgets as widgets
from IPython.display import display, clear_output
!pip install --upgrade google-api-python-client

from google.colab import auth
from googleapiclient.discovery import build



# Kategoriler ve alt maddeler
kategoriler = {
    "Önyargı": ["Dış Görünüş", "Sempatiklik", "Kıyafet", "Davranış", "Seyirci İlişkisi", "Ses Tonu", "Konuşma Şekli", "Agresiflik", "Kibir"],
    "Zanaat": ["Ses Kullanışı", "Tonlama", "Vurgulama", "Elini Kolu Kullanışı", "Sahne Hakimiyeti", "Seyirci İnteraktifi", "Hız", "Doğallık", "Spontanlık", "Diksiyon"],
    "Delivery": ["Jest", "Mimik", "Karakter Yaratma", "Taklit", "Mikrofon Kullanışı", "Timing", "LPM"]
}

score_boxes = {}
note_boxes = {}

# Şaka türleri ve teknikler
saka_turleri = ["LPM", "Aforizma Cümle", "Şiirsellik", "Şaka Türleri", "Kendini Tanıtma", "İlginç Hikaye", "Anektod", "Mantık Hatası", "Bir Şeyi Çürütme",
                "Savunma", "Tespit", "Anlar", "Teknikler", "Küfür", "Komik Kelime", "İsim", "Benzetme", "Misdirection" "Detaylar", "Done",  "Jest", "Uzun Şaka",
                "Tahmin Edilebilirlik", "Sürpriz", "Rant", "Cinsellik",  "Tarihi Konular", "Entelektüellik","Politik Konular", "Ful Evrensellik" ]

btns = {}
note_boxes_periyot = {}
periyot_data = {}
current_periyot = 1

def analiz_basla(btn):
    clear_output(wait=True)
    periyot_analizi()

def periyot_analizi():
    global btns, note_boxes_periyot
    clear_output(wait=True)
    print(f"{current_periyot}. Periyot Analizi")

    btns = {}
    note_boxes_periyot = {}

    for saka in saka_turleri:
        btn = widgets.Button(description=f"{saka} (0)")
        btn.count = 0

        note_box = widgets.Text(value="", placeholder="Notlar...")
        hbox = widgets.HBox([btn, note_box])
        display(hbox)

        btns[saka] = btn
        note_boxes_periyot[saka] = note_box

        def on_button_click(b, saka=saka):
            b.count += 1
            b.description = f"{saka} ({b.count})"

        btn.on_click(on_button_click)

    next_button = widgets.Button(description="Sonraki Periyot")
    finish_button = widgets.Button(description="Analizi Bitir")
    next_button.on_click(next_periyot)
    finish_button.on_click(finish_analysis)
    display(widgets.HBox([next_button, finish_button]))

def next_periyot(b):
    global current_periyot
    periyot_data[current_periyot] = {
        "notes": {name: note_box.value for name, note_box in note_boxes_periyot.items()},
        "counts": {name: btn.count for name, btn in btns.items()}
    }
    current_periyot += 1
    periyot_analizi()

def finish_analysis(b):
    global periyot_data
    periyot_data[current_periyot] = {
        "notes": {name: note_box.value for name, note_box in note_boxes_periyot.items()},
        "counts": {name: btn.count for name, btn in btns.items()}
    }
    clear_output(wait=True)
    for periyot, data in periyot_data.items():
        print(f"{periyot}. Periyot İstatistikleri:")
        for saka, count in data["counts"].items():
            print(f"{saka}: {count} kez, Not: {data['notes'][saka]}")
        print("-----------------------------")

    restart_button = widgets.Button(description="Yeniden Başla")
    restart_button.on_click(lambda x: kategorileri_goster())
    display(restart_button)

def kategorileri_goster():
    clear_output(wait=True)
    for kat, alt_maddeler in kategoriler.items():
        print(kat)
        for madde in alt_maddeler:
            score_box = widgets.IntText(value=0, description=madde, max=10, min=0)
            note_box = widgets.Text(value="", placeholder="Notlar...")
            display(widgets.HBox([score_box, note_box]))

            score_boxes[madde] = score_box
            note_boxes[madde] = note_box

    btn_analiz = widgets.Button(description="Analiz Başla")
    btn_analiz.on_click(analiz_basla)
    display(btn_analiz)

kategorileri_goster()


from google.colab import auth
from googleapiclient.discovery import build
import ipywidgets as widgets
from IPython.display import display, clear_output

auth.authenticate_user()

def write_to_google_docs(text):
    service = build('docs', 'v1')
    document = service.documents().create().execute()
    document_id = document['documentId']

    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }
    ]

    service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
    print(f"Veri yazdırıldı! Dokümanı şu linkten inceleyebilirsiniz: https://docs.google.com/document/d/{document_id}/edit")

# Geri kalan kodunuz
# (Önceki kodunuzı buraya ekleyin...)

def finish_analysis(b):
    global periyot_data
    periyot_data[current_periyot] = {
        "notes": {name: note_box.value for name, note_box in note_boxes_periyot.items()},
        "counts": {name: btn.count for name, btn in btns.items()}
    }
    clear_output(wait=True)

    doc_text = ""
    for periyot, data in periyot_data.items():
        doc_text += f"{periyot}. Periyot İstatistikleri:\n"
        for saka, count in data["counts"].items():
            doc_text += f"{saka}: {count} kez, Not: {data['notes'][saka]}\n"
        doc_text += "-----------------------------\n"

    write_to_google_docs(doc_text)

    restart_button = widgets.Button(description="Yeniden Başla")
    restart_button.on_click(lambda x: kategorileri_goster())
    display(restart_button)

kategorileri_goster()

"""# Yeni Bölüm"""

