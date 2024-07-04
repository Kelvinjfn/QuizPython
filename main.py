import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo do Excel
df = pd.read_excel("questions.xlsx")

# Pegar as Perguntas Aleatóriamente
questions = df.sample(n=10).values.tolist()

# Variáveis Globais
score = 0
current_question = 0

# Função para Verificar a resposta
def check_answer(answer):
    global score, current_question
    if answer == correct_answer.get():
        score += 1
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        show_result()


# Função para Exibir a próxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))

    correct_answer.set(answer)

# Função para Exibir o Resultado final
def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você completou o quiz.\n\nPontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

# Função para jogar novamente
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()

janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x450")
#Definindo as Cores
background_color = "#2F4F4F"
text_color = "#D3D3D3"
button_color = "#483D88"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add("*Font", "Arial")


# Icon na Tela
app_icon = PhotoImage(file="Logo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Componentes da Interface
question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela, command=play_again, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
# play_again_btn.pack(pady=10)




display_question()
janela.mainloop()