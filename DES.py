import pyDes
import base64
import sys
import io
from tkinter import *
from tkinter import filedialog
from pyDes import *

root = Tk()
root.geometry("400x400")
root.title("Image Encryption")
ivInt = bytearray("AStringOfIV=", "utf-8")                                 #key1
keyInt = bytearray("aKeyOfSomeKindThat+IWillNotShare", "utf-8")            #key2
lst = []
string1 = StringVar()
string2 = StringVar()


def select_image():
    imgToEncrypt = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'), ('png file', '*.png')])         
b = Button(root, text="Select Image", command=select_image)
b.place(x=130, y=60)

def encrypt_image():
    with open('image.jpg', 'rb') as f:
        jpgdata=f.read()
    for f1 in jpgdata:
        lst.append(f1)
        f.close()
        data = jpgdata
    k = pyDes.triple_des(base64.b64decode(keyInt), mode=pyDes.CBC, IV=base64.b64decode(ivInt),pad=None, padmode=pyDes.PAD_PKCS5)    #encryption
    print ("please wait for a moment")
    jpgdata = k.encrypt(data)
    with open('Encrypted.jpg', 'wb') as f:
        f.write(jpgdata)
    print("Encryption Complete")
b = Button(root, text="Encrypt", command=encrypt_image)
b.place(x=100, y=210)

def decrypt_image():
    with open('Encrypted.jpg', 'rb') as f:
        jpgdata=f.read()
    for f1 in jpgdata:
        lst.append(f1)
        f.close()
        data = jpgdata
    k = pyDes.triple_des(base64.b64decode(keyInt), mode=pyDes.CBC, IV=base64.b64decode(ivInt), padmode=pyDes.PAD_PKCS5)       #decryption
    print ("please wait for a moment")
    jpgdata = k.decrypt(data)
    with open('Decrypted.jpg', 'wb') as f:
        f.write(jpgdata)
    print("Decryption Complete")
b = Button(root, text="Decrypt", command=decrypt_image)
b.place(x=210, y=210)
entry1 = Entry(root, textvariable=string1, width=24)
entry1.place(x=95, y=120)
label1 = Label(root, text="Key 1:").place(x=40, y=120)
label1Result = Label(root)
entry2 = Entry(root, textvariable=string2, width=24)
entry2.place(x=95, y=160)
label2 = Label(root, text="Key 2:").place(x=40, y=160)
label2Result = Label(root)

root.mainloop()
