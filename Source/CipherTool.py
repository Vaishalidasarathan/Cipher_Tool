from consolemenu import *
from consolemenu.items import *
from consolemenu.menu_component import Dimension

from secretpy import Caesar
from secretpy import Affine
from secretpy import Keyword
from secretpy import Rot13
from secretpy import Vigenere
from secretpy import Bifid


from secretpy import alphabets
from secretpy import CryptMachine

from secretpy.cmdecorators import SaveCase, SaveSpaces


def Encryp_ceaser():
    data = input("Enter data to be Encrypted with Ceaser algorithm : ")
    key = int(input("Enter key : "))
    cm = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_ceaser():
    data = input("Enter dtata to be Decrypted By Ceaser Algorithm : ")
    key = int(input("Enter key to be Ency : "))
    cm = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
    print(cm.decrypt(data))
    input("Copy if needed.............")

def Encryp_Affine():
    data = input("Enter data to be Encrypted with Affine algorithm : ")
    key1 = int(input("Enter key1 : "))
    key2 = int(input("Enter key2 : "))
    key=[key1,key2]

    cm = SaveSpaces(SaveCase(CryptMachine(Affine(),key)))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_Affine():
    data = input("Enter dtata to be Decrypted By Affine Algorithm : ")
    key1 = int(input("Enter key1 : "))
    key2 = int(input("Enter key2 : "))
    key=[key1,key2]
    cm = SaveSpaces(SaveCase(CryptMachine(Affine(),key)))
    print(cm.decrypt(data))
    input("Copy if needed.............")

def Encryp_Keyword():
    data = input("Enter data to be Encrypted with Keyword algorithm : ")
    key = input("Enter key : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Keyword(),key)))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_Keyword():
    data = input("Enter dtata to be Decrypted By Keyword Algorithm : ")
    key = input("Enter key : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Keyword(),key)))
    print(cm.decrypt(data))
    input("Copy if needed.............")


def Encryp_Rot_13():
    data = input("Enter data to be Encrypted with Rot-13 algorithm : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Rot13())))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_Rot_13():
    data = input("Enter dtata to be Decrypted By Rot-13 Algorithm : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Rot13())))
    print(cm.decrypt(data))
    input("Copy if needed.............")

def Encryp_Vigenere():
    data = input("Enter data to be Encrypted with Vigenere algorithm : ")
    key = input("Enter key : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Vigenere(),key)))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_Vigenere():
    data = input("Enter dtata to be Decrypted By Vigenere Algorithm : ")
    key = input("Enter key : ")
    cm = SaveSpaces(SaveCase(CryptMachine(Vigenere(),key)))
    print(cm.decrypt(data))
    input("Copy if needed.............")

def Encryp_Bifid():
    data = input("Enter data to be Encrypted with Bifid algorithm : ")
    key =int(input("Enter key : "))
    cm = SaveSpaces(SaveCase(CryptMachine(Bifid(),key)))
    print(cm.encrypt(data))
    input("Copy if needed.............")

def Decryp_Bifid():
    data = input("Enter dtata to be Decrypted By Bifid Algorithm : ")
    key =int(input("Enter key : "))
    cm = SaveSpaces(SaveCase(CryptMachine(Bifid(),key)))
    print(cm.decrypt(data))
    input("Copy if needed.............")

def Encryp_ceaser_t(arg1, arg2):
    data = arg1
    key = int(arg2)
    cm = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
    return(cm.encrypt(data))
    

def Decryp_ceaser_t(arg1, arg2):
    data = arg1
    key = int(arg2)
    cm = SaveSpaces(SaveCase(CryptMachine(Caesar(), key)))
    return(cm.decrypt(data))
    

def Encryp_Affine_t(arg1,arg2,arg3):
    data = arg1
    key1 = int(arg2)
    key2 = int(arg3)
    key=[key1,key2]

    cm = SaveSpaces(SaveCase(CryptMachine(Affine(),key)))
    return(cm.encrypt(data))
    

def Decryp_Affine_t(arg1,arg2,arg3):
    data = arg1
    key1 = int(arg2)
    key2 = int(arg3)
    key=[key1,key2]
    cm = SaveSpaces(SaveCase(CryptMachine(Affine(),key)))
    return(cm.decrypt(data))
    

def Encryp_Keyword_t(arg1,arg2):
    data = arg1
    key = arg2
    cm = SaveSpaces(SaveCase(CryptMachine(Keyword(),key)))
    return(cm.encrypt(data))
    

def Decryp_Keyword_t(arg1,arg2):
    data = arg1
    key = arg2
    cm = SaveSpaces(SaveCase(CryptMachine(Keyword(),key)))
    return(cm.decrypt(data))
    


def Encryp_Rot_13_t(arg1):
    data = arg1
    cm = SaveSpaces(SaveCase(CryptMachine(Rot13())))
    return(cm.encrypt(data))
    

def Decryp_Rot_13_t(arg1):
    data = arg1
    cm = SaveSpaces(SaveCase(CryptMachine(Rot13())))
    return(cm.decrypt(data))
    

def Encryp_Vigenere_t(arg1,arg2):
    data = arg1
    key = arg2
    cm = SaveSpaces(SaveCase(CryptMachine(Vigenere(),key)))
    return(cm.encrypt(data))
    

def Decryp_Vigenere_t(arg1,arg2):
    data = arg1
    key = arg2
    cm = SaveSpaces(SaveCase(CryptMachine(Vigenere(),key)))
    return(cm.decrypt(data))
    

def Encryp_Bifid_t(arg1,arg2):
    data = arg1
    key =int(arg2)
    cm = SaveSpaces(SaveCase(CryptMachine(Bifid(),key)))
    return(cm.encrypt(data))
    

def Decryp_Bifid_t(arg1,arg2):
    data = arg1
    key =int(arg2)
    cm = SaveSpaces(SaveCase(CryptMachine(Bifid(),key)))
    return(cm.decrypt(data))
    
def check_ceaser(arg1,arg2):
    if(type(arg1) == str and type(arg2)==int):
        return True




def main():
    
 

    menu = ConsoleMenu("Data Security", "Classical Cipher",prologue_text="A cipher uses a system of fixed rules -- an algorithm -- to transform plaintext, a legible message, into ciphertext, an apparently random string of characters.")

    submenu_Ceaser = ConsoleMenu("Ceaser Cipher", "", prologue_text="The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet.")
    encrypt_Menu = FunctionItem("Ceaser Encrypt", Encryp_ceaser, [])
    decrypt_Menu = FunctionItem("Ceaser Decrypt", Decryp_ceaser, [])
    submenu_Ceaser.append_item(encrypt_Menu)
    submenu_Ceaser.append_item(decrypt_Menu)
    subItem_Ceaser = SubmenuItem("Ceaser", submenu_Ceaser)

  
    submenu_Affine = ConsoleMenu("Affine Cipher", "", prologue_text="The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. The formula used means that each letter encrypts to one other letter, and back again, meaning the cipher is essentially a standard substitution cipher with a rule governing which letter goes to which.")
    encrypt_Menu = FunctionItem("Affine Encrypt", Encryp_Affine, [])
    decrypt_Menu = FunctionItem("Affine Decrypt", Decryp_Affine, [])
    submenu_Affine.append_item(encrypt_Menu)
    submenu_Affine.append_item(decrypt_Menu)
    subItem_Affine = SubmenuItem("Affine", submenu_Affine)

    submenu_Keyword = ConsoleMenu("Keyword Cipher", "", prologue_text="A keyword cipher is a form of monoalphabetic substitution. A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.")
    encrypt_Menu = FunctionItem("Keyword Encrypt", Encryp_Affine, [])
    decrypt_Menu = FunctionItem("Keyword Decrypt", Decryp_Affine, [])
    submenu_Keyword.append_item(encrypt_Menu)
    submenu_Keyword.append_item(decrypt_Menu)
    subItem_Keyword = SubmenuItem("Keyword", submenu_Keyword)

    submenu_Rot_13 = ConsoleMenu("Rot-13 Cipher", "", prologue_text="ROT13 cipher(read as – “rotate by 13 places”) is a special case of the Ceaser cipher in which the shift is always 13.So every letter is shifted 13 places to encrypt or to decrypt the message..")
    encrypt_Menu = FunctionItem("Rot-13 Encrypt", Encryp_Rot_13, [])
    decrypt_Menu = FunctionItem("Rot-13 Decrypt", Decryp_Rot_13, [])
    submenu_Rot_13.append_item(encrypt_Menu)
    submenu_Rot_13.append_item(decrypt_Menu)
    subItem_Rot_13 = SubmenuItem("Rot-13", submenu_Rot_13)

    submenu_Vigenere = ConsoleMenu("Vigenere Cipher", "", prologue_text="Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .The encryption of the original text is done using the Vigenère square or Vigenère table.")
    encrypt_Menu = FunctionItem("Vigenere Encrypt", Encryp_Vigenere, [])
    decrypt_Menu = FunctionItem("Vigenere Decrypt", Decryp_Vigenere, [])
    submenu_Vigenere.append_item(encrypt_Menu)
    submenu_Vigenere.append_item(decrypt_Menu)
    subItem_Vigenere = SubmenuItem("Vigenere", submenu_Vigenere)

    submenu_Bifid = ConsoleMenu("Bifid Cipher", "", prologue_text="This cipher technique considered more secure compared to other substitution algorithms reason being it breaks the message apart into two separate streams and then recombines them. It is a combination of the Polybius square with the transposition and uses fractionation to achieve diffusion. ")
    encrypt_Menu = FunctionItem("Bifid Encrypt", Encryp_Bifid, [])
    decrypt_Menu = FunctionItem("Bifid Decrypt", Decryp_Bifid, [])
    submenu_Bifid.append_item(encrypt_Menu)
    submenu_Bifid.append_item(decrypt_Menu)
    subItem_Bifid = SubmenuItem("Bifid", submenu_Bifid)


    menu.append_item(subItem_Ceaser)
    menu.append_item(subItem_Affine)
    menu.append_item(subItem_Keyword)
    menu.append_item(subItem_Rot_13)
    menu.append_item(subItem_Vigenere) 
    menu.append_item(subItem_Bifid)
  
    menu.show()




    


if __name__ == "__main__":
    main()