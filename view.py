import customtkinter as ctk
import tkinter
from PIL import Image
from controller import ControllerCadastro, ControllerLogin

image_pil = Image.open('python1.png')
image_tk = ctk.CTkImage(image_pil, size=(110,110))

x = 10

#função de registro
def button_register():

    def press_button():
        resultado = ControllerCadastro.cadastrar(nome=nameEntry.get(), email=emailEntry.get(), senha=senhaEntry.get())

        if resultado == 2:
            name_error = ctk.CTkLabel(register, text='Nome pequeno ou muito maior que o permitido', width=5)
            name_error.place(y=300, x=90)
            name_error.after(3000, name_error.destroy)
        if resultado == 3:
            email_error = ctk.CTkLabel(register, text='Email pequeno ou muito grande', width=5)
            email_error.place(y=300, x=130)
            email_error.after(3000, email_error.destroy)
        if resultado == 4:
            senha_error = ctk.CTkLabel(register, text='Senha pequena ou muito grande', width=5)
            senha_error.place(y=300, x=130)
            senha_error.after(3000, senha_error.destroy)

        if resultado == 6:
            email_error = ctk.CTkLabel(register, text='Email já existente', width=5)
            email_error.place(y=300, x=172)
            email_error.after(3000, email_error.destroy)


        if resultado == 1:
            cadastro_confirm = ctk.CTkLabel(register, text='Cadastro realizado com sucesso')
            cadastro_confirm.place(y=300, x=125)


            cadastro_close = ctk.CTkLabel(register, text='Janela fechando em 5 segundos')
            cadastro_close.place(y=330, x=125)

            register.after(5000, register.destroy)
    
    register = ctk.CTk()
    register.title('Cadastro')

    register_photo = ctk.CTkLabel(register, text='CADASTRO', height=20, width=2)
    register_photo.place(y=50, x=182)

    register_name = ctk.CTkLabel(register, text='Nome:')
    register_name.place(y=80, x=115)

    nameEntry = ctk.CTkEntry(register, width= 200)
    nameEntry.place(y=110, x=115)

    label_email = ctk.CTkLabel(register, text='Email:')
    label_email.place(y=140, x=115)

    emailEntry = ctk.CTkEntry(register, width= 200)
    emailEntry.place(y=170, x=115)

    label_senha = ctk.CTkLabel(register, text='Senha:')
    label_senha.place(y=200, x=115)

    senhaEntry = ctk.CTkEntry(register, width= 200)
    senhaEntry.place(y=230, x=115)

    button_cadastro = ctk.CTkButton(register, text='Enter', width=100, command=press_button)
    button_cadastro.place(y=270, x=169)


    register.geometry('400x400')

    root._set_appearance_mode('Dark')
    register.mainloop()

def button_login():
    resultado = ControllerLogin.login(email=root_entry_email.get(), senha=root_entry_passworld.get())
    
    if resultado == 1:
        root_login = ctk.CTkLabel(root, text='Login Efetuado com sucesso', width=3)
        root_login.place(y=350, x=165)
        root_login.after(3000, root_login.destroy)
        label_login = ctk.CTkLabel(root, text='Janela finalizando em 5 segundos', width=3)
        label_login.place(y=375, x=155)
        label_login.after(3000, label_login.destroy)
        root.after(5000, root.destroy)

    else:
        root_passworld = ctk.CTkLabel(root, text='Email ou senha incorretos', width=3)
        root_passworld.place(y=350, x=180)
        root_passworld.after(3000, root_passworld.destroy)



root = ctk.CTk()
root.title('Projeto Login')

root_photo = ctk.CTkLabel(root, image=image_tk, fg_color= 'transparent', text='')
root_photo.place(y=30, x=200)

root_email = ctk.CTkLabel(root, text='Email:')
root_email.place(y=180, x=150)

root_entry_email = ctk.CTkEntry(root, width= 200)
root_entry_email.place(y=210, x=150)

root_passworld = ctk.CTkLabel(root, text='Password:')
root_passworld.place(y=240, x=150)

root_entry_passworld = ctk.CTkEntry(root, width= 200)
root_entry_passworld.place(y=270, x=150)

root_acess = ctk.CTkButton(root, text='Access', width=97, command=button_login)
root_acess.place(y=310, x=150)

root_register = ctk.CTkButton(root, text='Register', width=100, command=button_register)
root_register.place(y=310, x=250)



root._set_appearance_mode('Dark')
root.geometry("500x500")
root.mainloop()



