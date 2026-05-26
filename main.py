import customtkinter as ctk
from random import choice
from CTkMessagebox import CTkMessagebox
import config as cfg

class GreetingsPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Приветствую тебя!', cfg.TXT_COLOR_2),
            ('Я - магический шар', cfg.TXT_COLOR_1),
            ('Готов сыграть?', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel (
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 30)
            )
            label.place(relx = 0.5, rely = 0.25 + (idx * 0.2), anchor = 'c')

        button_data = [
            ('Не хочу', self.controller.end_game),
            ('Давай!', lambda: self.controller.switch_to('RulesPage'))
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                text = text,
                command = command,
                **cfg.BTN_PARAMS
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.85, anchor = 'c')

class RulesPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Задай мне любой вопрос...', cfg.TXT_COLOR_2),
            ('О прошлом, о будущем, о настоящем...', cfg.TXT_COLOR_1),
            ('И получи свой судьбоносный ответ', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel (
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 27)
            )
            label.place(relx = 0.5, rely = 0.2 + (idx * 0.2), anchor = 'c')

        button_data = [
            ('Не сейчас', self.controller.end_game),
            ('Поехали!', self.controller.create_game)
        ]

        for idx, (text, command) in enumerate (button_data):
            button = ctk.CTkButton (
                self,
                text = text,
                command = command,
                **cfg.BTN_PARAMS
            )
            button.place(relx = 0.35 + (idx * 0.3), rely = 0.8, anchor = 'c')

class GamePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        label_data = [
            ('Введи свой вопрос...', cfg.TXT_COLOR_1),
            ('...и нажми на шар...', cfg.TXT_COLOR_2)
        ]

        for idx, (text, color) in enumerate (label_data):
            label = ctk.CTkLabel (
                self,
                text = text,
                text_color = color,
                font = ('Constantia', 27)
            )
            label.place(relx = 0.5, rely = 0.15 + (idx * 0.25), anchor = 'c')

        self.entry = ctk.CTkEntry(self, **cfg.ENTRY_PARAMS)
        self.entry.place(relx = 0.5, rely = 0.28, anchor = 'c')

        self.button = ctk.CTkButton(
            self,
            **cfg.BALL_PARAMS,
            command = lambda: self.get_status(self.entry.get())
        )
        self.button.place(relx = 0.5, rely = 0.7, anchor = 'c')

    def get_status(self, user_input):
        status = self.controller.transfer_data(user_input)

        if status in cfg.ERROR_MESSAGES:
            error_message = CTkMessagebox(
                self.controller,
                **cfg.MSG_PARAMS,
                message = cfg.ERROR_MESSAGES[status]
            )
            app.wait_window(error_message)
            self.prepare_entry()
            return




    def prepare_entry(self):
        self.entry.delete (0, 'end')
        self.entry.focus_set()

    def update_game(self):
        self.prepare_entry()
        self.button.configure(fg_color = choice(cfg.COLORS))
        self.button.configure(hover_color = choice(cfg.COLORS))

class MessagePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color = cfg.FRM_COLOR)
        self.controller = controller

        self.message_label = ctk.CTkLabel(
            self,
            text = '',
            text_color = cfg.TEXT_COLOR_1,
            font = ('Constantia', 27)
        )
        self.message_label.place(relx = 0.5, rely = 0.5, anchor = 'c')

    def update_message(self, info):
        self.message_label.co

class MainLogic():
    def check_input(self, user_input):
        cleaned_input = user_input.strip()

        if not cleaned_input:
            return 'empty'
        if len(cleaned_input) < 5:
            return 'too_short'
        if not any(c.isalpha() for c in cleaned_input):
            return 'not_alpha'
        if not cleaned_input.endswith('?'):
            return 'not_question'

        return 'success'

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title ('the magic ball')
        self.geometry ('700x500+700+350')
        self.resizable (False, False)
        self.attributes ('-alpha', 0.8)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill = 'both', expand = True)

        self.main_logic = MainLogic()

        self.transfer_data = self.main_logic.check_input

        self.pages = {}
        self.current_frame = None
        for F in (GreetingsPage, RulesPage, GamePage):
            page_name = F.__name__
            self.pages[page_name] = F(master = self.main_frame, controller=self)
        self.switch_to("GreetingsPage")

    def switch_to(self, page_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.pages[page_name]
        self.current_frame.pack(fill="both", expand=True)

    def show_message(self):


    def create_game(self):
        self.pages['GamePage'].update_game()
        self.switch_to('GamePage')

    def end_game(self):
        self.after(200, self.destroy)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()





#def repeat():
#    clear_all()
#    label = ctk.CTkLabel (master = app, text = 'Отлично! Играем снова...', bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#    app.after(5000, main)
#
#def end():
#    clear_all()
#    label = ctk.CTkLabel (master = app, width = 500, text = 'Спасибо тебе за игру!', bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#    app.after(5000, app.destroy)
#
#def third_step():
#    clear_all()
#    label = ctk.CTkLabel (master = app, text = 'Хочешь сыграть снова?', bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.4, anchor = 'c')
#
#    button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = 'Не хочу', bg_color = '#000066', fg_color = '#ffffff',
#    text_color = '#000066', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command = end)
#    button.place(relx = 0.4, rely = 0.6, anchor = 'c')
#
#    button = ctk.CTkButton (master = app, width = 100, height = 50, corner_radius = 20, text = 'Хочу', bg_color = '#000066', fg_color = '#ffffff',
#    text_color = '#000066', hover_color = '#00ff99', font= ('Arial', 20, 'bold'), command=repeat)
#    button.place(relx = 0.6, rely = 0.6, anchor = 'c')
#
#def second_step():
#    clear_all()
#
#    label = ctk.CTkLabel (master = app, text = choice(answers), bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#
#    app.after(5000, third_step)
#
#def first_step(question):
#    if len(question) == 0:
#        messagebox.showinfo('Ошибочка', 'А где вопросик')
#    else:
#        clear_all()
#
#        label = ctk.CTkLabel (master = app, text = choice(waiting), bg_color = '#000066',
#        text_color = '#ffffff', font = ('Arial', 25, 'bold'))
#        label.place(relx = 0.5, rely = 0.5, anchor = 'c')
#
#        app.after (5000, second_step)
#
#def check_name(name):
#    if len(name) == 0:
#        messagebox.showinfo('Ошибочка', 'А где имечко?')
#    elif name.isalpha() == False:
#        messagebox.showinfo('Ошибочка', 'Допускаются только буковки')
#        entry.delete(0, ctk.END)
#    elif len(name) > 10:
#        messagebox.showinfo('Ошибочка', 'Слишком длинное имечко')
#        entry.delete(0, ctk.END)
#    else:
#        rules(name)
#
#def clear_all():
#    for widget in app.winfo_children():
#        widget.destroy()
#
#def clear_input():
#    entry.delete(len(entry.get()) - 1)
#
#def main():
#    clear_all()
#
#    label = ctk.CTkLabel (master = app, text = 'Напиши свой вопрос...', bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.15, anchor = 'c')
#
#    entry = ctk.CTkEntry (master = app, width = 500, height = 50, border_width = 0,  corner_radius = 20, justify = 'c',
#    fg_color = '#ffffff', bg_color = '#000066', text_color = '#000066', font = ('Arial', 20, 'bold'))
#    entry.place(relx = 0.5, rely = 0.3, anchor = 'c')
#
#    label = ctk.CTkLabel (master = app, text = '...и нажми на магический шар', bg_color = '#000066',
#    text_color = '#00ff00', font = ('Arial', 25, 'bold'))
#    label.place(relx = 0.5, rely = 0.45, anchor = 'c')
#
#    button = ctk.CTkButton (master = app, width = 200, height = 200, text = '', corner_radius = 100,
#    bg_color = '#000066', fg_color = choice(colors), hover_color = choice(colors), command = lambda: first_step(entry.get()))
#    button.place(relx = 0.5, rely = 0.75, anchor = 'c')аа