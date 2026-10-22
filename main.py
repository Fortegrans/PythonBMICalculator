from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Vücut kitle indeksi")
window.minsize(500,500)
window.config(padx=20,pady=20)

def button_clicked():
    kilo_text = my_entry.get()
    boy_text = my_entry2.get()
    if kilo_text =="" or boy_text=="":
        sonuc_label.config(text="Lütfen boy ve kilo endeksinizi doğru giriniz")
    else:
        try:
            kilo = float(kilo_text)
            boy = float(boy_text.replace(",","."))
            if boy > 3:
                boy=boy /100

            bmi = round(kilo / (boy ** 2), 2)



            #BMI değerine göre kategori belirleme
            if bmi <= 18.4:
                durum ="zayıf"
            elif 18.4 < bmi <= 24.9:
                durum ="normal"
            elif 24.9 < bmi <= 26.9:
                durum ="biraz kilolu"
            elif 26.9 < bmi <= 29.9:
                durum ="fazla kilolu"
            elif 30 <= bmi < 35:
                durum = "1. Derece Obez"
            elif 35 <= bmi < 40:
                durum = "2. Derece Obez"
            else:
                durum = "3. Derece Obez (Aşırı Obez)"

            #sonucu ekrandaki etikete yazdırmak için;
            sonuc_label.config(text=f"bmi: {bmi}\nDurum: {durum}")
        except ValueError:
            messagebox.showerror("Hata!",message="Lütfen geçerli bir sonuç giriniz")



my_label = Label(text="Vücut ağırlığınızı giriniz (kg)")
my_label.config(font=("Arial", 15, "bold"))
my_label.config(pady=10, padx=10)
my_label.pack()

my_entry =Entry()
my_entry.pack()

my_label2 = Label(text="Boyunuzu giriniz (cm)")
my_label2.config(font=("Arial", 15, "bold"))
my_label2.config(pady=10, padx=10)
my_label2.pack()
my_label2.pack()



my_entry2 = Entry()
my_entry2.get()
my_entry2.pack()



my_button = Button(text="Hesapla", command=button_clicked)
my_button.config(padx=20,pady=5)
my_button.config(font=("Arial", 10, "bold"))
my_button.pack()

sonuc_label =Label(text="Sonuc")
sonuc_label.config(font=("Arial", 15, "italic", "bold"))
sonuc_label.config(padx=20,pady=20)

sonuc_label.pack()


window.mainloop()