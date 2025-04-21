import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")

def gerar_senha():
    senha = []
    
    Int = '0123456789'
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(0,4):
        senha.append(random.choice(Int))

    for c in range(0,4):
        senha.append(random.choice(char))

    senha = ''.join(random.sample(senha, len(senha)))
  
    Resultado_senha.configure(text = senha, text_color = '#F0FFFF')

app = ctk.CTk()
app.title("Gerador de Senhas")
app.geometry("300x300")

campo_gerador = ctk.CTkLabel(app, text="⬇⬇ Senha ⬇⬇ ", text_color = '#7B68EE', font = ('Impact', 20))
campo_gerador.pack(pady = (70,20))

container_senha = ctk.CTkFrame(app, width = 200, height = 50, corner_radius = 10)
container_senha.pack(pady = (10,20,), padx = 50, fill = "both", expand = False)

Resultado_senha = ctk.CTkLabel(container_senha, text = '' ,font = ('Impact', 18))
Resultado_senha.pack()

botao_gerador = ctk.CTkButton(app, text="Gerar Senha",font = ('Arial', 15) ,command = gerar_senha, fg_color = '#7B68EE',hover_color = '#4B0082', text_color = 'white')
botao_gerador.pack()

app.mainloop()

# Esse é um gerador de senhas com interface gráfica feito com a biblioteca customtkinter.
# O código gera uma senha aleatória composta por 4 números e 4 letras maiúsculas, misturadas aleatoriamente.
# A senha gerada é exibida em um rótulo na interface gráfica. O botão "Gerar Senha" chama a função que gera a senha e atualiza o rótulo com a nova senha.
# A interface é estilizada com cores e fontes personalizadas para melhorar a aparência.