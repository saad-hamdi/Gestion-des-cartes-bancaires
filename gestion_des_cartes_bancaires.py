from tkinter import *
from PIL import Image,ImageTk
from tkinter import simpledialog, messagebox
import random
class Bank:
    def __init__(self,window):
        self.window=window
        self.window.iconbitmap("bank.ico")
        self.window.title("la gestion des cartes bancaires")
        self.window.geometry('1920x1080+0+0')
        self.window.state("zoomed")

        self.frametop=Frame(self.window)
        self.frametop.pack(fill=X)

        self.lbl=Label(self.frametop,text="La Gestion Des Cartes Bancaires",bg="#4666FF",fg="white",font=("tahoma",50),pady=50)
        self.lbl.pack(fill=X)

        self.centerFrame=Frame(self.window,height=300)
        self.centerFrame.pack(fill=X)

        self.agent=Frame(self.centerFrame,pady=100,padx=100)
        self.agent.grid(row=0,column=0)
        self.img=Image.open("agent.png")
        self.img.thumbnail((150,150))
        self.new_image=ImageTk.PhotoImage(self.img)
        self.imgagent=Label(self.agent,image=self.new_image)
        self.imgagent.pack()
        self.Buttonagent=Button(self.agent,command=self.openagent,text="AGENT COMPTE",font="tahoma",bg="#4666FF",fg="white")
        self.Buttonagent.pack()

        self.client=Frame(self.centerFrame,pady=100,padx=100)
        self.client.grid(row=0,column=1)
        self.img2=Image.open("client.png")
        self.img2.thumbnail((150,150))
        self.new_image2=ImageTk.PhotoImage(self.img2)
        self.imgclient=Label(self.client,image=self.new_image2)
        self.imgclient.pack()
        self.Buttonclient=Button(self.client,command=self.openclient,text="CLIENT COMPTE",font="tahoma",bg="#4666FF",fg="white")
        self.Buttonclient.pack()

        self.developer=Frame(self.centerFrame,pady=100,padx=100)
        self.developer.grid(row=0,column=2)
        self.img3=Image.open("developer.png")
        self.img3.thumbnail((150,150))
        self.new_image3=ImageTk.PhotoImage(self.img3)
        self.imgprogrammer=Label(self.developer,image=self.new_image3)
        self.imgprogrammer.pack()
        self.Buttonprogrammer=Button(self.developer,command=self.opendeveloper,text="ABOUT DEVELOPER",font="tahoma",bg="#4666FF",fg="white")
        self.Buttonprogrammer.pack()

        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1,weight=1)
        self.centerFrame.grid_columnconfigure(2,weight=1)

        self.accounts={}
        self.pin_codes={}
        self.numeros_comptes={}
#agent window
    def openagent(self):
        self.window=Toplevel()
        self.window.iconbitmap("agent.ico")
        self.window.title("Agent")
        self.window.geometry("1920x1080+0+0")
        self.window.state("zoomed")
        #top frame
        self.topframeagent=Frame(self.window)
        self.topframeagent.pack(fill=X)
        self.lblagent=Label(self.topframeagent,text="L'AGENT",bg="#4666FF",fg="white",font=("tahoma",50),pady=50)
        self.lblagent.pack(fill=X)
        #center frame
        self.centerFrameagent=Frame(self.window)
        self.centerFrameagent.pack(fill=X)
        #generer numero de compte
        self.genererframe=Frame(self.centerFrameagent,pady=100,padx=100)
        self.genererframe.grid(row=0,column=0)
        self.imggenerer=Image.open("search1.png")
        self.imggenerer.thumbnail((150,150))
        self.new_imagegenerer=ImageTk.PhotoImage(self.imggenerer)
        self.imggenererlbl=Label(self.genererframe,image=self.new_imagegenerer)
        self.imggenererlbl.pack()
        self.Buttongenerer=Button(self.genererframe,command=self.generer,text="GENERER",font="tahoma",bg="#4666FF",fg="white")
        self.Buttongenerer.pack()
        
        #voir les numeros de clients et leurs codes secrets
        self.voirframe=Frame(self.centerFrameagent,pady=100,padx=100)
        self.voirframe.grid(row=0,column=1)
        self.imgvoir=Image.open("generer.png")
        self.imgvoir.thumbnail((150,150))
        self.new_imagevoir=ImageTk.PhotoImage(self.imgvoir)
        self.imgvoirlbl=Label(self.voirframe,image=self.new_imagevoir)
        self.imgvoirlbl.pack()
        self.Buttonvoir=Button(self.voirframe,command=self.numeros_codes,text="NUMEROS ET CODES",font="tahoma",bg="#4666FF",fg="white")
        self.Buttonvoir.pack()
        #voir les comptes
        self.comptesframe=Frame(self.centerFrameagent,pady=100,padx=100)
        self.comptesframe.grid(row=0,column=2)
        self.imgcomptes=Image.open("manipsts.png")
        self.imgcomptes.thumbnail((150,150))
        self.new_imagecomptes=ImageTk.PhotoImage(self.imgcomptes)
        self.imgcompteslbl=Label(self.comptesframe,image=self.new_imagecomptes)
        self.imgcompteslbl.pack()
        self.Buttoncomptes=Button(self.comptesframe,command=self.show_info_all,text="LES COMPTES",font="tahoma",bg="#4666FF",fg="white")
        self.Buttoncomptes.pack()

        self.centerFrameagent.grid_columnconfigure(0,weight=1)
        self.centerFrameagent.grid_columnconfigure(1,weight=1)
        self.centerFrameagent.grid_columnconfigure(2,weight=1)

#client window
    def openclient(self):
        self.window=Toplevel()
        self.window.iconbitmap("client.ico")
        self.window.title("Client")
        self.window.geometry("1920x1080+0+0")
        self.window.state("zoomed")
        #top frame
        self.topframe=Frame(self.window)
        self.topframe.pack(fill=X)
        self.lbl=Label(self.topframe,text="Le Client",bg="#4666FF",fg="white",font=("tahoma",50),pady=50)
        self.lbl.pack(fill=X)
        #center frame
        self.centerFrame=Frame(self.window)
        self.centerFrame.pack(fill=X)
        #login frame
        self.picframe=Frame(self.centerFrame,pady=100,padx=100)
        self.picframe.grid(row=0,column=0)
        self.imgl1=Image.open("login.png")
        self.imgl1.thumbnail((200,200))
        self.new_imagel1=ImageTk.PhotoImage(self.imgl1)
        self.imglogin=Label(self.picframe,image=self.new_imagel1)
        self.imglogin.pack()
        #login frame
        self.loginframe=Frame(self.centerFrame)
        self.loginframe.grid(row=0,column=1)
        #les bouttons de login
        self.btn_open_account =Button(self.loginframe, text="Ouvrir un compte", command=self.ouvrircompte,font="tahoma",bg="#4666FF",fg="white")
        self.btn_open_account.pack(fill=X)

        self.btn_delete_account =Button(self.loginframe, text="Supprimer un compte", command=self.supprimercompte,font="tahoma",bg="#4666FF",fg="white")
        self.btn_delete_account.pack(fill=X)

        self.btn_modifier_code=Button(self.loginframe,text="Modifier le Code Secret", command=self.modifiercode,font="tahoma",bg="#4666FF",fg="white")
        self.btn_modifier_code.pack(fill=X)

        self.btn_deposit =Button(self.loginframe, text="Déposer de l'argent", command=self.deposer,font="tahoma",bg="#4666FF",fg="white")
        self.btn_deposit.pack(fill=X)

        self.btn_withdraw =Button(self.loginframe, text="Retirer de l'argent", command=self.retirer,font="tahoma",bg="#4666FF",fg="white")
        self.btn_withdraw.pack(fill=X)

        self.btn_show_info_single =Button(self.loginframe, text="Afficher les informations", command=self.show_info_single,font="tahoma",bg="#4666FF",fg="white")
        self.btn_show_info_single.pack(fill=X)

        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1,weight=1)

    def ouvrircompte(self):
        account_number = simpledialog.askinteger("Ouvrir un compte", "Entrez le numéro du compte:")
        if account_number in self.accounts:
            messagebox.showwarning("Erreur", "Le numéro du client est deja utilise!")
        else:
            if account_number is not None:
                q=random.randint(0,9)
                w=random.randint(0,9)
                e=random.randint(0,9)
                pin_code = int(str(q)+str(w)+str(e))
                if pin_code is not None:
                    n=random.randint(0,9)
                    a=random.randint(0,100)
                    nombrecompte=int(str(n)+str(a))
                    self.accounts[account_number] = 0
                    self.pin_codes[account_number] = pin_code
                    self.numeros_comptes[account_number]=nombrecompte
                    info_str = f"Compte ouvert avec succès!\nNuméro du client {account_number}:\nSolde = {self.accounts[account_number]}Dh\nNuméro du compte = {self.numeros_comptes[account_number]}\nCode secret = {pin_code}"
                    messagebox.showinfo("Succès", info_str)

    def supprimercompte(self):
        account_number = simpledialog.askinteger("Supprimer un compte", "Entrez le numéro du client à supprimer:")
        if account_number in self.accounts:
            numeros_comptes=simpledialog.askinteger("Supprimer un compte", "Entrez le numéro du compte à supprimer:")
            if numeros_comptes is not None and numeros_comptes==self.numeros_comptes.get(account_number):
                pin_code = simpledialog.askfloat("Supprimer un compte", "Entrez le code secret du compte:")
                if pin_code is not None and pin_code == self.pin_codes.get(account_number):
                    del self.accounts[account_number]
                    del self.pin_codes[account_number]
                    del self.numeros_comptes[account_number]
                    messagebox.showinfo("Succès", "Compte supprimé avec succès!")
                else:
                    messagebox.showwarning("Erreur", "Code secret incorrect!")
            else:
                messagebox.showwarning("Erreur", "le numéro du compte incorrect!")
        else:
            messagebox.showwarning("Erreur", "Le numéro du client n'existe pas!")

    def modifiercode(self):
        account_number = simpledialog.askinteger("Modifier le code secret", "Entrez le numéro du client:")
        if account_number in self.accounts:
            numeros_comptes=simpledialog.askinteger("Modifier le code secret", "Entrez le numéro du compte:")
            if numeros_comptes is not None and numeros_comptes==self.numeros_comptes.get(account_number):
                pin_code = simpledialog.askinteger("Modifier le code secret", "Entrez le code secret du compte:")
                if pin_code is not None and pin_code == self.pin_codes.get(account_number):
                    newpin_code = simpledialog.askinteger("Modifier le code secret", "Entrez le nouveau code secret:")
                    self.pin_codes[account_number] = newpin_code
                    messagebox.showinfo("Succès", "Votre code secret changé avec succès!")
                else:
                    messagebox.showwarning("Erreur", "Code secret incorrect!")
            else:
                messagebox.showwarning("Erreur", "le numéro du compte incorrect!")
        else:
            messagebox.showwarning("Erreur", "Le compte n'existe pas!")

    def deposer(self):
        account_number = simpledialog.askinteger("Déposer de l'argent", "Entrez le numéro du client:")
        if account_number in self.accounts:
            numeros_comptes=simpledialog.askinteger("Supprimer un compte", "Entrez le numéro du compte:")
            if numeros_comptes is not None and numeros_comptes==self.numeros_comptes.get(account_number):
                pin_code = simpledialog.askinteger("Déposer de l'argent", "Entrez le code secret du compte:")
                if pin_code is not None and pin_code == self.pin_codes.get(account_number):
                    amount = simpledialog.askfloat("Déposer de l'argent", "Entrez le montant à déposer:")
                    self.accounts[account_number] += amount
                    messagebox.showinfo("Succès", f"{amount}Dh déposés avec succès!")
                else:
                    messagebox.showwarning("Erreur", "Code secret incorrect!")
            else:
                messagebox.showwarning("Erreur", "le numéro du compte incorrect!")
        else:
            messagebox.showwarning("Erreur", "Le compte n'existe pas!")

    def retirer(self):
        account_number = simpledialog.askinteger("Retirer de l'argent", "Entrez le numéro du client:")
        if account_number in self.accounts:
            numeros_comptes=simpledialog.askinteger("Supprimer un compte", "Entrez le numéro du compte:")
            if numeros_comptes is not None and numeros_comptes==self.numeros_comptes.get(account_number):
                pin_code = simpledialog.askinteger("Retirer de l'argent", "Entrez le code secret du compte:")
                if pin_code is not None and pin_code == self.pin_codes.get(account_number):
                    amount = simpledialog.askfloat("Retirer de l'argent", "Entrez le montant à retirer:")
                    if amount <= self.accounts[account_number]:
                        self.accounts[account_number] -= amount
                        messagebox.showinfo("Succès", f"{amount}Dh retirés avec succès!")
                    else:
                        messagebox.showwarning("Erreur", "Solde insuffisant!")
                else:
                    messagebox.showwarning("Erreur", "le numéro du compte incorrect!")
            else:
                messagebox.showwarning("Erreur", "Code secret incorrect!")
        else:
            messagebox.showwarning("Erreur", "Le compte n'existe pas!")
    def show_info_single(self):
        account_number = simpledialog.askinteger("Afficher les informations d'un client", "Entrez le numéro du client:")
        if account_number in self.accounts:
            numeros_comptes=simpledialog.askinteger("Supprimer un compte", "Entrez le numéro du compte:")
            if numeros_comptes is not None and numeros_comptes==self.numeros_comptes.get(account_number):
                pin_code = simpledialog.askinteger("Afficher les informations d'un client", "Entrez le code secret du compte:")
                if pin_code is not None and pin_code == self.pin_codes.get(account_number):
                    info_str = f"Informations du client {account_number}:\nSolde = {self.accounts[account_number]}Dh\nNuméro du compte = {self.numeros_comptes[account_number]}\nCode secret = {pin_code}"
                    messagebox.showinfo(f"Informations du client {account_number}", info_str)
                else:
                    messagebox.showwarning("Erreur", "Code secret incorrect!")
            else:
                messagebox.showwarning("Erreur", "le numéro du compte incorrect!")
        else:
            messagebox.showwarning("Erreur", "Le compte n'existe pas!")
    
    def show_info_all(self):
        info_str = "Informations des clients:\n"
        for account_number, balance in self.accounts.items():
            info_str += f"Compte {account_number}: Solde = {balance}Dh, Numéro du compte = {self.numeros_comptes[account_number]} Code secret = {self.pin_codes[account_number]}\n"
        messagebox.showinfo("Informations des clients", info_str)
    
    def generer(self):
        account_number = simpledialog.askinteger("Obtenir le numéro de client par numéro de compte", "Entrez le numéro du compte:")
        if account_number in self.numeros_comptes:
            client_number = self.numeros_comptes[account_number]
            messagebox.showinfo("Numéro de compte", f"Le numéro de compte pour le client {account_number} est : {client_number}")
        else:
            messagebox.showwarning("Erreur", "Le compte n'existe pas!")
    
    def numeros_codes(self):
        info_str = "Informations des clients:\n"
        for account_number, balance in self.accounts.items():
            info_str += f"Compte {account_number}:  Numéro du compte = {self.numeros_comptes[account_number]} Code secret = {self.pin_codes[account_number]}\n"
        messagebox.showinfo("Informations des clients", info_str)
    #developer window
    def opendeveloper(self):
        self.window=Toplevel()
        self.window.iconbitmap("developer.ico")
        self.window.title("Developer")
        self.window.geometry("1920x1080+0+0")
        self.window.state("zoomed")
        #top frame
        self.topframedeveloper=Frame(self.window)
        self.topframedeveloper.pack(fill=X)
        self.lbldeveloper=Label(self.topframedeveloper,text="Le Développeur",bg="#4666FF",fg="white",font=("tahoma",50),pady=50)
        self.lbldeveloper.pack(fill=X)
        #center frame
        self.centerFramedeveloper=Frame(self.window)
        self.centerFramedeveloper.pack(fill=X)
        #pic frame
        self.developerframe=Frame(self.centerFramedeveloper,pady=100,padx=100)
        self.developerframe.grid(row=0,column=0)
        self.imgdeveloper=Image.open("programmer.png")
        self.imgdeveloper.thumbnail((200,200))
        self.new_imagedeveloper=ImageTk.PhotoImage(self.imgdeveloper)
        self.imglbldev=Label(self.developerframe,image=self.new_imagedeveloper)
        self.imglbldev.pack()
        #informations frame
        self.infoframe=Frame(self.centerFramedeveloper)
        self.infoframe.grid(row=0,column=1)
        self.label1=Label(self.infoframe,text="Bienvenu dans mon programme",font=("tahoma",20),pady=10,fg="#4666FF")
        self.label1.pack()
        self.label2=Label(self.infoframe,text="Je suis Saad Hamdi",font=("tahoma",20),pady=10,fg="#4666FF")
        self.label2.pack()
        self.label3=Label(self.infoframe,text="Stagair de Developement Digital 101",font=("tahoma",20),pady=10,fg="#4666FF")
        self.label3.pack()
        self.label4=Label(self.infoframe,text="ISTA Ben Guerir",font=("tahoma",20),pady=10,fg="#4666FF")
        self.label4.pack()
        self.label5=Label(self.infoframe,text="Telephone : 0631671465",font=("tahoma",20),pady=10,fg="#4666FF")
        self.label5.pack()
        #pc pic frame
        self.pcframe=Frame(self.centerFramedeveloper,pady=100,padx=100)
        self.pcframe.grid(row=0,column=2)
        self.imgpc=Image.open("pc.png")
        self.imgpc.thumbnail((200,200))
        self.new_imagepc=ImageTk.PhotoImage(self.imgpc)
        self.imglblpc=Label(self.pcframe,image=self.new_imagepc)
        self.imglblpc.pack()

        self.centerFramedeveloper.grid_columnconfigure(0,weight=1)
        self.centerFramedeveloper.grid_columnconfigure(1,weight=1)
        self.centerFramedeveloper.grid_columnconfigure(2,weight=1)

#le code principale
if (__name__=='__main__'):
    window=Tk()
    banc=Bank(window)
    mainloop()
