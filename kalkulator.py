from tkinter import *

root = Tk()

root.title("Kalkulator vrka")
root.configure(bg="#FFFFFF")
root.geometry("300x365")
root.resizable(False, False)

def klik(angka):
    layar.insert(END, angka)

def hapus_semua():
    layar.delete(0, END)

def hapus_satu():
    isi_layar = layar.get() 
    layar.delete(0, END) 
    layar.insert(0, isi_layar[:-1]) 

def hitung():
    try:
        hitung_hitungan = layar.get() 
        layar.delete(0, END) 
        hasil = eval(hitung_hitungan) 
        layar.insert(0, hasil) 
    except:
        layar.delete(0, END)
        layar.insert(0, "Error") 

def tukar_tanda():
    isi_layar = layar.get() 
    if isi_layar != "": 
        if isi_layar[0] == "-":
            layar.delete(0, END)
            layar.insert(0, isi_layar[1:]) 
        else:
            layar.delete(0, END)
            layar.insert(0, "-" + isi_layar)
        
# Bikin Layar Kalkulator
layar = Entry(root, width=24, borderwidth=1, font=("Segoe UI", 14, "bold"), justify="right", relief="solid", bg="#f3f4f6")
layar.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

#kolom ataslh
btn_backspc = Button(root, text="⌫", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=hapus_satu, relief="flat", bg="#e5e5e5")
btn_ac = Button(root, text="C", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=hapus_semua, relief="flat", bg="#e5e5e5")
btn_persen = Button(root, text="%", padx=20, pady=10, font=("Segoe UI", 8,), command=lambda: klik("%"), relief="flat", bg="#e5e5e5")
btn_bagi = Button(root, text="÷", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik("/"), relief="flat", bg="#e5e5e5")

btn_backspc.grid(row=1, column=1, pady=8)
btn_ac.grid(row=1, column=2, pady=8)
btn_persen.grid(row=1, column=3, pady=8)
btn_bagi.grid(row=1, column=4, pady=8)

#kolom dan baris 789
btn_7 = Button(root, text="7", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(7), relief="flat", bg="#f3f3f3")
btn_8 = Button(root, text="8", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(8),relief="flat", bg="#f3f3f3")
btn_9 = Button(root, text="9", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(9), relief="flat", bg="#f3f3f3")
btn_x = Button(root, text="X", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik("*"), relief="flat", bg="#e5e5e5")

btn_7.grid(row=2, column=1, pady=8)
btn_8.grid(row=2, column=2, pady=8)
btn_9.grid(row=2, column=3, pady=8)
btn_x.grid(row=2, column=4, pady=8)

#kolom dan baris 456
btn_4 = Button(root, text="4", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(4), relief="flat", bg="#f3f3f3")
btn_5 = Button(root, text="5", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(5), relief="flat", bg="#f3f3f3")
btn_6 = Button(root, text="6", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(6), relief="flat", bg="#f3f3f3")
btn_kurang = Button(root, text="−", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik("-"), relief="flat", bg="#e5e5e5")

btn_4.grid(row=3, column=1, pady=8)
btn_5.grid(row=3, column=2, pady=8)
btn_6.grid(row=3, column=3, pady=8)
btn_kurang.grid(row=3, column=4, pady=8)

#kolom dan baris 123
btn_1 = Button(root, text="1", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(1), relief="flat", bg="#f3f3f3")
btn_2 = Button(root, text="2", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(2), relief="flat", bg="#f3f3f3")
btn_3 = Button(root, text="3", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(3),relief="flat", bg="#f3f3f3")
btn_tambah = Button(root, text="+", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik("+"), relief="flat", bg="#e5e5e5")

btn_1.grid(row=4, column=1, pady=8)
btn_2.grid(row=4, column=2, pady=8)
btn_3.grid(row=4, column=3, pady=8)
btn_tambah.grid(row=4, column=4, pady=8)

#kolom dan baris akhir
btn_negpos = Button(root, text="-/+", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=tukar_tanda, relief="flat", bg="#f3f3f3")
btn_0 = Button(root, text="0", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(0), relief="flat", bg="#f3f3f3")
btn_koma = Button(root, text=",", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=lambda: klik(","), relief="flat", bg="#f3f3f3")
btn_equal = Button(root, text="=", padx=20, pady=10, font=("Segoe UI", 8, "bold"), command=hitung, relief="flat", bg="#0078D7")

btn_negpos.grid(row=8, column=1, pady=8)
btn_0.grid(row=8, column=2, pady=8)
btn_koma.grid(row=8, column=3, pady=8)
btn_equal.grid(row=8, column=4, pady=8)

root.mainloop()