#import module
import tkinter as tk
from tkinter import messagebox, colorchooser

#fungsi hasil prediksi
def hasil_prediksi():
    try: #looping buat meriksa apakah inpunya sesuai dengan apa yang diminta
        for entry in input_nilai:
            nilai = int(entry.get()) #mengambil nilai dari entry dan diubah ke interger
            if not (0 <= nilai <= 100):
                raise ValueError("Nilainya harus antara 0 sampai 100")
        label_hasil.config(text="Hasil Prediksi: Prodi Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input yang benar", "Pastikan semua inputnya itu angka yang benar 0 - 100")
#fungsi untuk ubah warna bg
def ubah_warna_bg():
    warna = colorchooser.askcolor()[1]  #memilih warna pake colour chooser
    if warna:
        root.config(bg=warna)  
        label_judul.config(bg=warna)  
        label_hasil.config(bg=warna)  
        for entry in input_nilai:
            entry.config(bg=warna)  
        button_prediksi.config(bg=warna)  


#membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("2000x500")

#tombol untuk mengubah warna
button_ubah_warna = tk.Button(root, text="Ubah Warna Latar Belakang", command=ubah_warna_bg)
button_ubah_warna.pack(pady=10)

#tomb
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
label_judul.pack(pady=20)

input_nilai = []
for i in range(10):
    #looping untuk membuat label dan entry mata pelajaran
    label_mata_pelajaran = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label_mata_pelajaran.pack(pady=5)
    
    #buat entry untuk input nilainya
    entry_nilai = tk.Entry(root)
    entry_nilai.pack(pady=5)
    
    #nambahin entry ke dalam list input_nilai
    input_nilai.append(entry_nilai)


#tombol untuk ngitung prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.pack(pady=20)

#membuat objek labe;
label_hasil = tk.Label(root, text="", font=("Arial", 14))
label_hasil.pack(pady=10)

#menjalankan aplikasi
root.mainloop()