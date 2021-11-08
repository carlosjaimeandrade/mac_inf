import uuid
from getmac import get_mac_address
from tkinter import * #
from ttkthemes import *
mac_add = get_mac_address()
print("MAC VARIEANTE " + mac_add)
print (hex(uuid.getnode()))


print("The MAC address in formatted way is FIXO : ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))

texto = "MAC VARIANTE " + str(mac_add) + " / MAC FIXO = " + str(hex(uuid.getnode()))
root = ThemedTk("aqua")
root.title("MAC")
root.geometry("400x110+100+200")
root.resizable(0, 0)
root.iconbitmap(".icon/logoF.ico")

frame = Frame(root, pady=20)
frame.pack()

mensagem = Label(frame, text=texto)
mensagem.pack()




root.mainloop()