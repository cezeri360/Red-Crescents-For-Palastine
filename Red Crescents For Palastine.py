import tkinter
import tkinter as tk
import webbrowser
r= tk.Tk()
r.title("Red Crescents")
r.geometry("500x500+300+100")
r.configure(background="green")
yazi=tkinter.Label(
    text="For Palastine",
    fg="red",
    bg="black",
    width=20,
    height=3,
    font="Algerian"
)
yazi.pack()
def list_ok(event):
    secilen = liste.get(liste.curselection())
    if secilen == "İHH":
        url = "https://ihh.org.tr/filistin-gazze"
        webbrowser.open(url)
    elif secilen == "Turkey Red Crescent":
        url = "https://bagis.kizilay.org.tr/tr/bagis/bagisyap/32/filistin-genel-bagisi"
        webbrowser.open(url)
    elif secilen == "Cyrps Red Crescent":
        url = "https://www.kktkizilayi.org/bagis-online/gazzede-insanlik-olmesin"
        webbrowser.open(url)
    elif secilen == "Palastine Red Crescent":
        url = "https://www.palestinercs.org/ar"
        webbrowser.open(url)
    elif secilen == "Egyptian Red Crescent":
        url = "https://www.egyptianrc.org/Arabic/ERC-Activities/Activities/ActivityDetails/84"
        webbrowser.open(url)
liste=tk.Listbox(r)
liste.pack()
liste.insert(tk.END,"İHH")
liste.insert(tk.END,"Turkey Red Crescent")
liste.insert(tk.END,"Cyrps Red Crescent")
liste.insert(tk.END,"Palastine Red Crescent")
liste.insert(tk.END,"Egyptian Red Crescent")
liste.bind("<ButtonRelease-1>", list_ok)
r.mainloop()
###Free_Palastine###
###Love_Palastine###
#I'm from Turkey.#
