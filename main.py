import customtkinter as ctk
from random import choice
from tkinter import messagebox

ctk.set_appearance_mode ("dark")

app = ctk.CTk()
app.title ('the magic ball')
app.geometry ('700x500+700+350')
app.resizable (False, False)
app.config (bg='#000066')
app.attributes ('-alpha', 0.8)

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
waiting = ['Жду ответа от Вселенной...', 'Посылаю запрос в космос...', 'Звёзды просят немного подождать...', 'Дай-ка подумать...', 'Получаю твой ответ...']
colors = ['#e6194b', '#3cb44b', '#ffe119', '#f58231', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#808080']

def repeat():
    clear_all()
    label = ctk.CTkLabel (master = app, text = 'Отлично! Играем снова...', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after(5000, main)

def end():
    clear_all()
    label = ctk.CTkLabel (master = app, width = 500, text = 'Спасибо тебе за игру!', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
    app.after(5000, app.destroy)

def third_step():
    clear_all()
    label = ctk.CTkLabel (master = app, text = 'Хочешь сыграть снова?', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.4, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = 'Не хочу', bg_color = '#000066', fg_color = '#ffffff',
    text_color = '#000066', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command = end)
    button.place(relx = 0.4, rely = 0.6, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = 'Хочу', bg_color = '#000066', fg_color = '#ffffff',
    text_color = '#000066', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command=repeat)
    button.place(relx = 0.6, rely = 0.6, anchor = 'c')

def second_step():
    clear_all()

    label = ctk.CTkLabel (master = app, text = choice(answers), bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    app.after(5000, third_step)

def first_step(question):
    if len(question) == 0:
        messagebox.showinfo('Ошибочка', 'А где вопросик')
    else:
        clear_all()

        label = ctk.CTkLabel (master = app, text = choice(waiting), bg_color = '#000066',
        text_color = '#ffffff', font = ('Arial', 25, 'bold'))
        label.place(relx = 0.5, rely = 0.5, anchor = 'c')

        app.after (5000, second_step)

def check_name(name):
    if len(name) == 0:
        messagebox.showinfo('Ошибочка', 'А где имечко?')
    elif name.isalpha() == False:
        messagebox.showinfo('Ошибочка', 'Допускаются только буковки')
        entry.delete(0, ctk.END)
    elif len(name) > 10:
        messagebox.showinfo('Ошибочка', 'Слишком длинное имечко')
        entry.delete(0, ctk.END)
    else:
        rules(name)

def clear_all():
    for widget in app.winfo_children():
        widget.destroy()

def clear_input():
    entry.delete(len(entry.get()) - 1)

def main():
    clear_all()

    label = ctk.CTkLabel (master = app, text = 'Напиши свой вопрос...', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.15, anchor = 'c')

    entry = ctk.CTkEntry (master = app, width = 500, height = 50, border_width = 0,  corner_radius = 20, justify = 'c',
    fg_color = '#ffffff', bg_color = '#000066', text_color = '#000066', font = ('Arial', 20, 'bold'))
    entry.place(relx = 0.5, rely = 0.3, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = '...и нажми на магический шар', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.45, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 200, height = 200, text = '', corner_radius = 100,
    bg_color = '#000066', fg_color = choice(colors), hover_color = choice(colors), command = lambda: first_step(entry.get()))
    button.place(relx = 0.5, rely = 0.75, anchor = 'c')

def rules(name):
    clear_all()
    label = ctk.CTkLabel (master = app, text = f'Давай сыграем, {name}!', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.15, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = 'Задай мне любой вопрос', bg_color = '#000066',
    text_color = '#ffffff', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.3, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = 'О прошлом, о будущем, о настоящем...', bg_color = '#000066',
    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.45, anchor = 'c')

    label = ctk.CTkLabel (master = app, text = '...и получи свой судьбоносный ответ', bg_color = '#000066',
    text_color = '#ffffff', font = ('Arial', 25, 'bold'))
    label.place(relx = 0.5, rely = 0.6, anchor = 'c')

    button = ctk.CTkButton (master = app, width = 200, height = 50, corner_radius = 20, text = 'Начнем!', text_color = '#0099ff',
    bg_color = '#000066', fg_color = '#ffffff', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command = main)
    button.place(relx = 0.5, rely = 0.8, anchor = 'c')

label = ctk.CTkLabel (master = app, text = 'Приветствую тебя!', bg_color = '#000066',
text_color = '#00ff99', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.2, anchor = 'c')

label = ctk.CTkLabel (master = app, text = 'Я - магический шар', bg_color = '#000066',
text_color = '#00ff00', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.35, anchor = 'c')

label = ctk.CTkLabel (master = app, text = 'Назови свое имя...', bg_color = '#000066',
text_color = '#00ff99', font = ('Arial', 30, 'bold'))
label.place(relx = 0.5, rely = 0.5, anchor = 'c')

entry = ctk.CTkEntry (master = app, width = 200, height = 30, border_width = 0,  corner_radius = 20, justify = 'c',
fg_color = '#ffffff', bg_color = '#000066', text_color = '#000066', font = ('Arial', 20, 'bold'))
entry.place(relx = 0.5, rely = 0.65, anchor = 'c')

button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = '✅', text_color = '#000066',
bg_color = '#000066', fg_color = '#ffffff', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command = lambda:check_name(entry.get()))
button.place(relx = 0.6, rely = 0.8, anchor = 'c')

button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = '<', bg_color = '#000066', fg_color = '#ffffff',
text_color = '#000066', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command=clear_input)
button.place(relx = 0.4, rely = 0.8, anchor = 'c')

app.mainloop()
