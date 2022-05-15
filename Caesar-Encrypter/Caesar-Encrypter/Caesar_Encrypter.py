import tkinter
import os
import sys

class Caesar_encrypter:
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = '9043751268'
        self.encrypted_message = ''
        self.decrypted_message = ''
        self.binary_message = ''

    def get_path(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, filename) 
        else:
            return filename

    def caesar_encrypter(self):
        self.window()

    def window(self):
        def decrypt_message():
            original_message = tkinter.Entry.get(text)
            original_message = original_message.lower()
            layers = int(layers_num.get())
            for layer in range(0, layers):
                if layer > 0:
                    original_message = self.decrypted_message
                    self.decrypted_message = ''
                for letter in original_message:
                    if letter in self.letters:
                        letter_posicion = self.letters.find(letter)
                        if letter_posicion < 3:
                            if letter_posicion == 0:
                                self.decrypted_message += self.letters[23]
                            elif letter_posicion == 1:
                                self.decrypted_message += self.letters[24]
                            else:
                                self.decrypted_message += self.letters[25]
                        else:
                            self.decrypted_message += self.letters[letter_posicion - 3]

                    elif letter in self.numbers:
                        letter_posicion = self.numbers.find(letter)
                        if letter_posicion == 0:
                            self.decrypted_message += self.numbers[9]
                        else:
                            self.decrypted_message += self.numbers[letter_posicion - 1]
                    elif letter == '$':
                        self.decrypted_message += ' '
                    else:
                        self.decrypted_message += letter
            encrypted.delete(0, 10000)
            encrypted.insert(0, self.decrypted_message)
            self.encrypted_message = ''
            self.decrypted_message = ''

        def encrypt_message():
            original_message = tkinter.Entry.get(text)
            original_message = original_message.lower()
            layers = int(layers_num.get())
            for layer in range(0, layers):
                if layer > 0:
                    original_message = self.encrypted_message
                    self.encrypted_message = ''
                for letter in original_message:
                    if letter in self.letters:
                        letter_posicion = self.letters.find(letter)
                        if letter_posicion > 22:
                            if letter_posicion == 23:
                                self.encrypted_message += self.letters[0]
                            elif letter_posicion == 24:
                                self.encrypted_message += self.letters[1]
                            else:
                                self.encrypted_message += self.letters[2]
                        else:
                            self.encrypted_message += self.letters[letter_posicion + 3]
                    elif letter in self.numbers:
                        letter_posicion = self.numbers.find(letter)
                        if letter_posicion == 9:
                            self.encrypted_message += self.numbers[0] 
                        else:
                            self.encrypted_message += self.numbers[letter_posicion + 1]
                    elif letter == ' ':
                        self.encrypted_message += '$'
                    else:
                        self.encrypted_message += letter
            encrypted.delete(0, 10000)
            encrypted.insert(0, self.encrypted_message.upper())
            self.encrypted_message = ''
            self.decrypted_message = ''

        def encrypt_to_binary():
            original_message = tkinter.Entry.get(text)
            original_message = original_message.lower()
            self.binary_message =  [bin(ord(x))[2:].zfill(8) for x in original_message]
            encrypted.delete(0, 10000)
            encrypted.insert(0, self.binary_message)
            self.encrypted_message = ''
            self.decrypted_message = ''

        def binary_decrypt():
            original_message = self.binary_message
            self.binary_message = ''.join([chr(int(x,2)) for x in original_message])
            encrypted.delete(0, 10000)
            encrypted.insert(0, self.binary_message) 
            self.encrypted_message = ''
            self.decrypted_message = ''
            
        def reset():
            text.delete(0, 10000)
            layers_num.delete(0, 10000)
            encrypted.delete(0, 10000)
            self.encrypted_message = ''
            self.decrypted_message = ''

        root = tkinter.Tk()
        root.configure(bg = '#0E0E0E')
        root.iconbitmap(self.get_path('cesar.ico'))
        root.geometry('805x253')
        root.resizable(False, False)
        root.title('Caesar-Encrypter v1.1.0')
        cesar_image = tkinter.PhotoImage(file = self.get_path('cesar.jpg'))
        cesar_image_pack = tkinter.Label(root, image = cesar_image).place(x = 10, y = 10)
        cesar_image2 = tkinter.PhotoImage(file = self.get_path('cesar2.jpg'))
        cesar_image2_pack = tkinter.Label(root, image = cesar_image2).place(x = 640, y = 10)
        title = tkinter.Label(root, text = 'Caesar Encrypter', font = ('Arial', 20, 'bold'), bg = '#0E0E0E', fg = 'white').place(x = '280', y = '5')
        masterv = tkinter.Label(root, text = '-- By Bl4ckV --', font = ('Arial', 10, 'bold'), bg = '#0E0E0E', fg = 'white').place(x = '348', y = '40')
        text = tkinter.Entry(root, font = ('Arial', 15, 'bold'))
        text.place(x = '180', y = '80', width = '445')
        info = tkinter.Label(root, text = 'Message:', font = ('Arial', 10, 'bold'), bg = '#0E0E0E', fg = 'white').place(x = '180', y = '55')
        layers_text = tkinter.Label(root, text = 'Encryption layers:', font = ('Arial', 10, 'bold'), bg = '#0E0E0E', fg = 'white').place(x = '180', y = '115')
        layers_num = tkinter.Entry(root, font = ('Arial', 15, 'bold'))
        layers_num.place(x = '180', y = '140', width = '120')
        encrypted = tkinter.Entry(root, font = ('Arial', 15, 'bold'))
        encrypted.place(x = '180', y = '210', width = '445')
        button = tkinter.Button(root, text = 'Encrypt', command = encrypt_message)
        button.place(x = '320', y = '140')
        binary_button = tkinter.Button(root, text = 'Binary\nEncrypt', command = encrypt_to_binary)
        binary_button.place(x = '440', y = '140')
        binary_button2 = tkinter.Button(root, text = 'Binary\nDecrypt', command = binary_decrypt)
        binary_button2.place(x = '500', y = '140')
        button2 = tkinter.Button(root, text = 'Decrypt', command = decrypt_message)
        button2.place(x = '380', y = '140')
        reset_button = tkinter.Button(root, text = 'Reset', command = reset)
        reset_button.place(x = '560', y = '140')
        info2 = tkinter.Label(root, text = 'Encrypted/Decrypted message:', font = ('Arial', 10, 'bold'), bg = '#0E0E0E', fg = 'white').place(x = '180', y = '185')
        root.mainloop()

encrypter = Caesar_encrypter()
encrypter.caesar_encrypter()
